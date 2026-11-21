---
name: player-grossip
description: Use when producing or updating Player Grossip episodes or NBA entertainment gossip involving off-court relationships, viral moments, photos, and editorial covers. 适用于球员花边、场外八卦、截图选题、双语稿、猎奇配图以及新做或补做双尺寸封面。
---

# Player Grossip

从 [WORKFLOW_PROMPT.md](WORKFLOW_PROMPT.md) 读取栏目流程。只有一张可辨认的截图、一个链接或一句明确选题时，默认一次完成整套。全套制作时依次核查故事后续、写独立的中英文稿、找真实配图、做两版封面、验收并打包。只要求单项、指定照片编号或修改旧封面时，仅执行对应部分。

- 栏目名使用 `Player Grossip`，封面署名使用 `PLAYER GROSSIP`。口吻要像给朋友讲一个有反转的 NBA 花边故事，悬念和戏剧感来自可核实的细节。
- 最终横版为 **1920×1080**，竖版为 **522×652**，均为 PNG，按宽×高计。竖版独立构图。
- 打包前打开成图检查。环境可运行 Python 3 时，用 [scripts/check_covers.py](scripts/check_covers.py) 和 `--bundle ... --full` 检查整套文件；工具不可用时等效核对。
- 遇到找图、出图、像素导出或旧包替换时，看 [操作手册](references/production.md)。按当前环境选工具。已有对应技能时按它的说明操作。
- 上传、发帖或推送按本次用户明确指定的范围执行。
