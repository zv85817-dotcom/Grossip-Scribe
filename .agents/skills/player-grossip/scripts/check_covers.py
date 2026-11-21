"""核验两版 PNG、素材包和编号配图出处。"""

import argparse
import re
import struct
import sys
import zlib
from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile


COVERS = {
    "poster_1920x1080.png": (1920, 1080),
    "poster_522x652.png": (522, 652),
}


def check_size(path, expected):
    def invalid():
        return ValueError(f"{path.name} 不是完整的 PNG，或 PNG 数据已损坏")

    with path.open("rb") as image:
        if image.read(8) != b"\x89PNG\r\n\x1a\n":
            raise invalid()
        seen_header = False
        data_bytes = 0
        while True:
            chunk_header = image.read(8)
            if len(chunk_header) != 8:
                raise invalid()
            length, kind = struct.unpack(">I4s", chunk_header)
            if not seen_header and (kind != b"IHDR" or length != 13):
                raise invalid()
            checksum = zlib.crc32(kind)
            remaining = length
            while remaining:
                part = image.read(min(remaining, 65536))
                if not part:
                    raise invalid()
                remaining -= len(part)
                checksum = zlib.crc32(part, checksum)
            stored = image.read(4)
            if len(stored) != 4 or checksum != struct.unpack(">I", stored)[0]:
                raise invalid()
            if kind == b"IHDR":
                if seen_header:
                    raise invalid()
                width, height = struct.unpack(">II", part[:8])
                if (width, height) != expected:
                    raise ValueError(
                        f"{path.name} 实际为 {width}×{height}，要求 {expected[0]}×{expected[1]}"
                    )
                seen_header = True
            elif kind == b"IDAT":
                data_bytes += length
            elif kind == b"IEND":
                if length or not data_bytes or image.read(1):
                    raise invalid()
                return


def check_bundle(bundle_path, directory, full=False):
    with ZipFile(bundle_path) as bundle:
        names = bundle.namelist()
        if len(names) != len(set(names)):
            raise ValueError("素材包内有重名条目")
        if any(PurePosixPath(name).name == "poster_1080x1920.png" for name in names):
            raise ValueError("素材包内仍有旧版 1080×1920 封面")
        failed = bundle.testzip()
        if failed is not None:
            raise ValueError(f"素材包内文件 CRC 校验失败：{failed}")

        for name in COVERS:
            entries = [entry for entry in names if PurePosixPath(entry).name == name]
            if len(entries) != 1:
                raise ValueError(f"素材包内需要且只应有一份 {name}")
            if bundle.read(entries[0]) != (directory / name).read_bytes():
                raise ValueError(f"素材包内的 {name} 与交付文件内容不同")

        if full:
            check_full_bundle(bundle, names)


def check_full_bundle(bundle, names):
    # 支持现有两期的旧配图目录与出处文件名称，保持同一套验收规则。
    def require_file(*candidates):
        for candidate in candidates:
            if candidate in names and bundle.getinfo(candidate).file_size > 0:
                return candidate
        raise ValueError(f"素材包缺少有效文件：{' 或 '.join(candidates)}")

    scripts = (
        ("中文稿.txt", ("主标题", "副标题")),
        ("English_Script.txt", ("Title", "Subtitle")),
    )
    for name, labels in scripts:
        lines = bundle.read(require_file(name)).decode("utf-8-sig").splitlines()
        if (
            len(lines) < 4 or lines[2].strip()
            or any(
                not re.fullmatch(re.escape(label) + r"[ \t]*[：:｜|]\s*\S.*", line)
                for label, line in zip(labels, lines[:2])
            )
        ):
            raise ValueError(f"{name} 需要单独的主标题、副标题和一行空行")
        body = "\n".join(lines[3:]).rstrip()
        paragraphs = re.split(r"\n[^\S\n]*\n+", body) if body else []
        if not paragraphs or any(not re.match(r"^\u3000{2}\S", p) for p in paragraphs):
            raise ValueError(f"{name} 每段正文需以两个全角空格开头")

    for name in (
        "配图编号预览.jpg",
        "poster_prompt.txt",
        "poster_vertical_522x652_prompt.txt",
    ):
        require_file(name)

    number_pattern = re.compile(r"(?:photos|配图)/([0-9]{2,})\.(?:jpe?g|png|webp|gif|avif)", re.I)
    photo_ids = []
    for name in names:
        match = number_pattern.fullmatch(name)
        if match and bundle.getinfo(name).file_size > 0:
            photo_ids.append(int(match[1]))
    if not photo_ids:
        raise ValueError("素材包缺少单独保存的编号配图")
    if len(set(photo_ids)) != len(photo_ids):
        raise ValueError("素材包的配图编号重复")

    require_file("文稿核查.txt", "素材与核查说明.md")
    sources = require_file("配图出处.txt", "图片情节与出处.txt")
    content = bundle.read(sources).decode("utf-8-sig")
    entries = list(re.finditer(r"(?m)^([0-9]{2,})(?=[^\S\n])[^\n]+", content))
    mapped_ids = set()
    for index, entry in enumerate(entries):
        number = int(entry[1])
        end = entries[index + 1].start() if index + 1 < len(entries) else len(content)
        if number in mapped_ids:
            raise ValueError(f"出处表编号 {number:02d} 重复")
        if not re.search(r"(?im)^来源[：:\t 　]+https?://\S+", content[entry.end():end]):
            raise ValueError(f"配图 {number:02d} 的出处条目缺少来源页链接")
        mapped_ids.add(number)

    missing = sorted(set(photo_ids) - mapped_ids)
    extra = sorted(mapped_ids - set(photo_ids))
    if missing or extra:
        detail = []
        if missing:
            detail.append("缺少编号出处 " + "、".join(f"{n:02d}" for n in missing))
        if extra:
            detail.append("出处表列了包内不存在的编号 " + "、".join(f"{n:02d}" for n in extra))
        raise ValueError("；".join(detail))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="包含两张最终封面的当期目录")
    parser.add_argument("--bundle", type=Path, help="待检查的完整素材包 ZIP 路径")
    parser.add_argument("--full", action="store_true", help="同时检查完整交付所需的文稿和配图")
    args = parser.parse_args()
    if args.full and args.bundle is None:
        parser.error("--full 需要同时指定 --bundle")
    try:
        for name, expected in COVERS.items():
            check_size(args.directory / name, expected)
        if args.bundle is not None:
            check_bundle(args.bundle, args.directory, args.full)
    except (OSError, ValueError, BadZipFile, RuntimeError) as error:
        print(f"检查失败：{error}", file=sys.stderr)
        return 1
    print("PNG 结构和尺寸通过：横版 1920×1080，竖版 522×652")
    if args.bundle is not None:
        print("ZIP 完整性及包内外封面一致性通过。")
    if args.full:
        print("中英文稿格式、编号配图、出处、预览和封面提示词通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
