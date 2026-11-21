# Player Grossip: Production guide

## Start with the story

A recognizable screenshot, a link, or a short topic is enough. Read the user's latest corrections first, then review the attachments and any accessible approved files. If an image is unclear, inspect the original and available context. Ask only for the missing detail needed to identify the story.

Keep each episode in its own directory and respect the requested location. Use relative paths in the shareable project. For a revision to color, jersey, hair, props, or one cover format, start from the approved reference and focus on the requested changes.

## Choose the tools

- Use web search and image search to locate and verify sources. Search snippets are leads; open the source page and inspect the image itself. Use the browser skill when inspecting sources in Codex's browser.
- Use imagegen or an equivalent generator/editor for covers. Use Pillow, FFmpeg, or another image tool for proportional resizing, and inspect the actual exports afterward. See the [README](../../../../README.md) for optional FFmpeg skill setup.
- Use skill-creator and release checks when maintaining the skill. When producing an episode, use the bundled Python checker. Equivalent tools are fine when the default tools are unavailable.

## Source the photos

1. Search names with the event, year, and follow-up terms. Open original posts, interviews, reports, and official records to confirm dates, context, and the latest verifiable development. Resolve conflicting accounts with direct statements where possible.
2. Search for candid expressions, reactions, interactions, and real props. If an object or body detail is central to the story, find an attributable close-up and a wider photo that gives it context.
3. Save available originals from public sources. If there is a broken link, login gate, or unusable thumbnail, look for a public alternative. Record unresolved links separately. Check files for errors, duplicates, blur, and misidentification. Retain credits and known usage terms.
4. Keep numbered images as separate files and create a contact sheet with readable numbers. Once the user selects images, retain their IDs. In the source list, start each entry with its ID, a space, and a description. Use the literal prefix `来源:` for the source page URL. A direct image URL can go on a separate line. Label archive photos, reposted screenshots, and memes with their actual context.

## Compose and export the covers

- Generate the landscape cover first. When creating the portrait version or revising artwork, open the approved reference before using it as an editing input. Prompt for the exact English headline, safe margins, subjects and reactions, period details, scene, props, lighting, and palette. Inspect the generated art before copying it to the episode folder.
- Use story objects as visual clues. For example, a bathtub with bubbles can allude to a viral quote, and a church visible beyond a club doorway can show what happened to the venue later. Let the scene do most of the work. Keep the typography short and the imagery clearly illustrative.
- Generate in 16:9 for landscape and close to 4:5 for portrait. Export at the required pixel dimensions even if the generator uses a different resolution. Recompose old 9:16 artwork for the new portrait format where needed.
- This FFmpeg command is suitable for portrait artwork that is already close to 4:5 and has spare room around the edges. If the crop cuts into lettering, faces, or the key prop, recompose before exporting. For landscape, use `1920:1080` in both filter stages and output `poster_1920x1080.png`. Pillow can also resize and crop proportionally.

```sh
ffmpeg -i portrait_source.png -vf "scale=522:652:force_original_aspect_ratio=increase:flags=lanczos,crop=522:652,setsar=1" -frames:v 1 -update 1 poster_522x652.png
```

## Package and check

Place the two text drafts, fact-check notes, numbered images, contact sheet, source list, final PNGs, and actual cover prompts at their episode-relative paths in the ZIP. Keep unused candidates, references, and intermediate renders outside the bundle. For old episodes, stage the update in a temporary ZIP in the same folder, check the preserved files and new portrait, and replace the original bundle after validation.

From the repository root, pass the actual episode folder and ZIP. To check just the two final PNGs, omit `--bundle` and `--full`. The checker uses the Python 3 standard library.

```sh
python .agents/skills/player-grossip/scripts/check_covers.py "./output/episode" --bundle "./output/episode/episode-package.zip" --full
```

The checker validates PNG structure and pixel dimensions, ZIP integrity, draft formatting, required notes, and photo-to-source matching. Open the final covers and contact sheet to review details that the script cannot judge. If browsing or generating images is unavailable, hand over the finished material and spell out what remains.
