# 第三方署名

**Player Grossip** 负责栏目工作流的编排、文稿规范、封面规格和交付校验。下列第三方项目保留原名和署名。

| 项目 | 作者或提供方 | 在工作流中的用途 |
| --- | --- | --- |
| FFmpeg 技能 | Digital Samba | 用于图像等比缩放和裁边的可选说明。收录上游的技能文件与 MIT 许可。 |
| Superpowers | Jesse Vincent | 维护工作流时使用的需求整理、计划、写作、审查和交付核验工具。日常做一期无需安装。 |
| imagegen、Browser、skill-creator、skill-installer、openai-docs | OpenAI | 分别用于出图、查看网页和维护技能。由当前 Codex 环境提供或按需启用。 |
| Pillow / FFmpeg 程序 | 各自的上游项目 | 可任选可用的图像工具导出指定像素和制作编号预览。安装和许可由各自项目提供。 |

- FFmpeg 技能的来源为 [Digital Samba 的 Claude Code Video Toolkit](https://github.com/digitalsamba/claude-code-video-toolkit/tree/ad8b4ecb912a9073be11e3d8aff7c158a883e1a2/.claude/skills/ffmpeg)，收录版本为提交 `ad8b4ecb912a9073be11e3d8aff7c158a883e1a2`。原始 [MIT 许可证](third_party/ffmpeg/LICENSE) 随技能保留。FFmpeg 程序可单独从[官网](https://ffmpeg.org/download.html)获取。
- Superpowers 的本地核对版本为 [v5.1.0](https://github.com/obra/superpowers/tree/v5.1.0)，对应提交 `f2cbfbefebbfef77321e4c9abc9e949826bea9d7`。如需维护时使用，按该版本的 [README](https://github.com/obra/superpowers/blob/v5.1.0/README.md) 里 Codex 的方式安装。[上游 MIT 许可](https://github.com/obra/superpowers/blob/v5.1.0/LICENSE)
- OpenAI 的技能发现、插件与安装说明见 [Codex Skills](https://developers.openai.com/codex/skills) 和 [Codex Plugins](https://developers.openai.com/codex/plugins)。Pillow 见[上游安装说明](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)。

可放进项目简介的署名文案：

> Player Grossip 由栏目团队整理并维护。感谢 Digital Samba 的 FFmpeg 技能、Jesse Vincent 的 Superpowers，以及 OpenAI 提供的 Codex 工具。第三方来源和许可见 THIRD_PARTY_NOTICES.md。
