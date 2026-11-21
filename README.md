# Player Grossip

Player Grossip 是面向 NBA 场外八卦的制作工作流。提供一句选题、一个链接或一张能看清事件的截图，一次完成文稿、配图、双版封面和素材包。

## 安装与运行

1. 从 GitHub 克隆仓库，或下载 ZIP 后完整解压。用 Codex 打开包含本 README 和 `.agents` 的项目根目录。项目自带 `player-grossip` 技能。
2. 确认当前会话能联网搜索、查找图片、生成或编辑图片，并在项目中保存文件。Codex 中有内置出图工具时用 `imagegen`。需要在内置浏览器里查看来源页时，启用 Browser 插件即可。
3. 文件检查需要 Python 3。先运行 `python --version`。若环境里的命令是 `python3`，或 Codex 提供了可用的 Python 解释器路径，替换下文命令的开头即可。导出和检查图片可用 Pillow。已有 Pillow 或等效图像工具就可以直接运行。

```sh
python -m pip install Pillow
```

也可用已有的 FFmpeg 程序导出图片，运行 `ffmpeg -version` 检查。FFmpeg 技能随包附带，属于可选工具说明。需要让它出现在 Codex 的技能列表时，将 [`third_party/ffmpeg`](third_party/ffmpeg) 整个复制到个人技能目录 `~/.agents/skills/ffmpeg`，保留 `LICENSE`。系统内置技能、Browser 插件与维护工具的来源见[第三方署名](THIRD_PARTY_NOTICES.md)。

## 制作一期

在 Codex 聊天中发下面这句，同时附上截图、链接或写明选题。

> 用 $player-grossip 做这期全套，主题见附件。

每次换题材即可。只做一项时，可以说「只给编号 1、2、7 的图」或「只补这期 522×652 的竖封面」。使用其他有联网和出图能力的助手时，复制[工作流提示词](.agents/skills/player-grossip/WORKFLOW_PROMPT.md)并附题材。

| 交付 | 内容 |
| --- | --- |
| 文稿 | 中文、英文各一份，分别有主副标题。正文每段缩进两个全角空格。用娱乐花边的口吻讲完起因、反应和后续。 |
| 配图 | 从网上找有故事的真实抓拍或事件图，附编号、独立原图、预览和出处。配图数量按能核实和获取的素材决定。 |
| 封面 | 横、竖各一张英文 PNG。横版 **1920×1080**，竖版 **522×652**，分别构图。 |
| 素材包 | 两份文稿、编号配图与出处、双版封面、核查说明及两版出图提示词。 |

各期成果默认保存在 `output/`。缺少联网、出图或落盘能力时，工作流会交付已完成的部分并标明缺项。

## 检查一期交付

从项目根目录运行校验，将命令里的 `episode` 替换成当期目录名。

```sh
python .agents/skills/player-grossip/scripts/check_covers.py "./output/episode" --bundle "./output/episode/本期完整素材包.zip" --full
```

校验器只用 Python 3 标准库，检查封面实际像素、稿件格式、配图与出处的对应关系和 ZIP 内容。成图还要打开检查主标题、栏目名、人物和道具。具体步骤见[操作手册](.agents/skills/player-grossip/references/production.md)，技能入口在 [SKILL.md](.agents/skills/player-grossip/SKILL.md)。

准备上传仓库时保留根目录的 `.gitignore` 和 `.agents`。提交前检查暂存文件，确认其中没有凭据、数据库、个人资料或当期素材。第三方技能的原作者和许可随项目保留。
