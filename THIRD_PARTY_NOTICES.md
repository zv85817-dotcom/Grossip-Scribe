# Third-party notices

Player Grossip assembles the editorial workflow, story formats, cover specifications, and delivery checks. Third-party components retain their original names and credits.

| Project | Author or provider | Role |
| --- | --- | --- |
| FFmpeg skill | Digital Samba | Optional instructions for proportional resizing and cropping. The bundled skill files retain their upstream MIT license. |
| Superpowers | Jesse Vincent | Planning, writing, review, and verification tools used to maintain the workflow. Optional for maintainers. |
| imagegen, Browser, skill-creator, skill-installer, and openai-docs | OpenAI | Tools for generating images, inspecting sources, or maintaining skills. Availability depends on the Codex environment. |
| Pillow and the FFmpeg executable | Their respective upstream projects | Optional tools for exact-size exports and contact sheets. Obtain the tools and their licenses from their upstream projects. |

- The bundled FFmpeg skill comes from [Digital Samba's Claude Code Video Toolkit](https://github.com/digitalsamba/claude-code-video-toolkit/tree/ad8b4ecb912a9073be11e3d8aff7c158a883e1a2/.claude/skills/ffmpeg), at commit `ad8b4ecb912a9073be11e3d8aff7c158a883e1a2`. Its original [MIT license](third_party/ffmpeg/LICENSE) is included. Download the separate FFmpeg executable from the [official FFmpeg site](https://ffmpeg.org/download.html).
- The verified Superpowers version is [v5.1.0](https://github.com/obra/superpowers/tree/v5.1.0), commit `f2cbfbefebbfef77321e4c9abc9e949826bea9d7`. See the upstream [Codex installation instructions](https://github.com/obra/superpowers/blob/v5.1.0/README.md) and [MIT license](https://github.com/obra/superpowers/blob/v5.1.0/LICENSE).
- For OpenAI tools, see [Codex Skills](https://developers.openai.com/codex/skills) and [Codex Plugins](https://developers.openai.com/codex/plugins). For Pillow, see the [upstream installation guide](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html).

Suggested project credit:

> Player Grossip is assembled and maintained by the editorial team. Thanks to Digital Samba for the FFmpeg skill, Jesse Vincent for Superpowers, and OpenAI for the Codex tools. See THIRD_PARTY_NOTICES.md for sources and licenses.
