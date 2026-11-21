# Player Grossip

Turn an NBA off-court story into a complete episode package. Start with a topic, link, or screenshot. The workflow checks what happened and what came next, writes separate English and Chinese stories, finds credited photos, and creates two editorial covers.

## Getting started

1. Clone this repository, or choose **Code → Download ZIP** on GitHub and extract the whole archive. Open the project root in Codex. The `.agents/skills/player-grossip/` folder contains the project skill.
2. Make sure your session can search the web and find images, generate or edit artwork, and save files to the workspace. Use the built-in image generation tool where available. If you need to inspect sources in Codex's browser, enable the Browser plugin.
3. Use Python 3 to run the package checker. Check your interpreter with `python --version`. Substitute `python3` or the path to an available interpreter if needed. For image exports and contact sheets, use Pillow or an equivalent image tool.

```sh
python -m pip install Pillow
```

FFmpeg is another option for exporting covers. Run `ffmpeg -version` to see whether it is installed. The optional [FFmpeg skill](third_party/ffmpeg) contains instructions; it does not install the executable. To make it available in your Codex skill list, copy that folder to `~/.agents/skills/ffmpeg` with its license intact. See [Third-party notices](THIRD_PARTY_NOTICES.md) for credits and tool links.

## Produce an episode

Send this in Codex with a screenshot, a link, or a written topic:

> Use $player-grossip to produce the full episode package for this story.

For a narrower task, say what you need: “Give me photos 01, 02, and 07 as separate files” or “Add the 522×652 portrait cover to the existing package.” To use another assistant with web and image tools, copy the [standalone workflow prompt](.agents/skills/player-grossip/WORKFLOW_PROMPT.md) and append the topic.

| Deliverable | What's included |
| --- | --- |
| Stories | Separate English and Chinese plain-text drafts, each with a headline and subhead. The writing follows the setup, reaction, and aftermath in an entertainment voice. |
| Photos | Numbered candid or editorial images with individual files, a contact sheet, and source credits. Coverage depends on what can be sourced and verified. |
| Covers | Two separately composed PNGs with English lettering: **1920×1080** landscape and **522×652** portrait. |
| Episode ZIP | Both drafts and covers, numbered photos, source credits, fact-check notes, and the prompts used to make the covers. |

New episodes are saved under `output/` by default. If the session lacks a required tool or a source cannot be verified, the workflow returns the completed work and names the missing deliverables.

## Check the package

Run the checker from the project root. Replace `episode` with your episode folder name and pass the path to the actual ZIP.

```sh
python .agents/skills/player-grossip/scripts/check_covers.py "./output/episode" --bundle "./output/episode/episode-package.zip" --full
```

The checker uses the Python 3 standard library. It checks PNG dimensions and structure, ZIP integrity, draft formatting, and whether the photo numbers match the source list. Open both covers to check the title, branding, people, and key props. See the [production guide](.agents/skills/player-grossip/references/production.md) and [skill instructions](.agents/skills/player-grossip/SKILL.md).

When publishing a copy of this repository, keep `.agents` and the root `.gitignore`. Inspect the staged files for credentials, databases, personal data, and episode assets. Preserve third-party credits and licenses.
