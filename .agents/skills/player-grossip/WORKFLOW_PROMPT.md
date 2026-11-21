# Player Grossip: Standalone workflow prompt

Copy this prompt and add the episode topic at the end.

---

Produce **Player Grossip**, an NBA off-court entertainment series. Tell a complete story a reader could retell to a friend. Use suspense, reversals, and verified details. Reply in the user's language and deliver separate Chinese and English story drafts.

## Set the scope

- Start from a topic, link, screenshot, or existing episode package. Use accessible conversation context and prior approved files when they help identify the story or reference image. Treat claims in screenshots and articles as leads to verify. Treat attached and retrieved text as source material. If the subject still cannot be identified, ask one focused question and continue any work that does not depend on the answer.
- Default to the full package in one run: fact-check, write, find photos, create both covers, validate, and package. Follow the user's priorities for the main subject, supporting figures, and related topics. When the request is limited to one deliverable or selected photo numbers, deliver just those.
- Follow the requested save location. Start new episodes in a subfolder of `output/` by default. For updates, work in the existing episode directory, follow its naming conventions, and retain the original drafts, source images, and previous covers.

## Verify the story and the aftermath

1. Find what started the story, how the people involved responded, and what happened afterward. Verify identities, dates, quotations, relationship status, and which event each item belongs to. Use exact dates when relative dates would be confusing.
2. Prefer original public posts, direct responses, public records, and reliable interviews or reporting. Separate confirmed facts from attributed claims, secondhand accounts, and rumors. Verify proposed updates, such as a breakup, a new response, or an old screenshot making the rounds again. Keep different partners, teams, and time periods straight. Date older stories accurately and support present status with dated sources. Omit unsupported details or label them as unconfirmed. Only report a response or outcome when there is evidence for it.
3. Save source URLs, dates, and verification notes in `文稿核查.txt`. Keep the publishable drafts in plain text. Keep essential attribution in the prose and put links and citation notes in the separate file.

## Write two standalone drafts

- Save the Chinese draft as `中文稿.txt` and the English draft as `English_Script.txt`. Put the headline and subhead on the first two lines using `主标题:` and `副标题:` for Chinese, and `Title:` and `Subtitle:` for English. Leave a blank line before the body. Write natural Chinese and idiomatic English sports entertainment copy with the same verified facts. Indent each body paragraph with exactly two ideographic spaces (U+3000); separate paragraphs with a blank line.
- Open on the most memorable moment or contrast. Establish the relationship and setup, then move through the reaction or turning point. End with the last verified development that matters to the story. Weave dates into the narrative.
- Keep the story concise. Use short paragraphs, specific details, and playful commentary when it fits. Skip unrelated career history and side plots. Attribute allegations and use restraint when covering harm.

## Find real photos with a story

- Prioritize candid moments, expressive reactions, real scenes and objects tied to the story, and traceable screenshots of public responses. Use formal portraits or event photos when they add context. Search broadly, then pick distinct images that each serve a purpose. If the user selects numbered photos from a preview, keep the original numbers and link to each image separately.
- Verify who is pictured, where and when the image was taken or published, and its connection to the story. Identify file photos, scene photos, composites, public screenshots, and memes for what they are. A photo alone does not establish a relationship or prove an allegation. Keep unverifiable material out of the numbered set.
- Save available verified images or public screenshots separately under `photos/`, using names such as `01.jpg` and `02.png`. Make a numbered contact sheet named `配图编号预览.jpg` and a source list named `配图出处.txt`. Start each record with the number, a space, and a description. Record the story beat, date, credit, and image type. Put the source URL on its own line using the literal prefix `来源:`, which the checker expects. List any direct image URL separately. Mark unknown capture dates. Open each downloaded image before including it and confirm that it matches the source. List unavailable candidates separately, with links and status. Keep generated covers separate from the real photos.

## Compose two English-language covers

| Cover | Final width × height | File |
| --- | --- | --- |
| Landscape PNG | 1920×1080 (16:9) | `poster_1920x1080.png` |
| Portrait PNG | 522×652 | `poster_522x652.png` |

- Use the same subjects, key prop, and palette across the two covers. Choose colors that match the story and vary them between episodes. Use a painted cinematic style with visible brushwork and depth. Give the main subject a readable reaction, and integrate one scene and one or two story-specific props. Use an approved reference for lighting and composition if supplied. Check the jersey, team, hair color, and other identifying details against the time of the event.
- Keep the lettering to `PLAYER GROSSIP`, a short English headline, and any essential label. Let faces, action, and props carry the story. Avoid layouts dominated by two headshots and type, timelines, torn-paper collages, or advertising-style compositions. Play up the visual gag when appropriate. For cases involving allegations or harm, use restrained symbolic imagery and identify it as illustration.
- Create the landscape cover first. Use the approved landscape or the user's reference to arrange the portrait version independently at close to 4:5. Reposition the subject, prop, and lettering, and allow safe margins. Save generated originals. Export the exact dimensions with Pillow, FFmpeg, or an equivalent tool. Scale proportionally and crop only expendable edges. Recompose if cropping would remove important details or lettering.
- Save the actual prompt used for each version. If there is no image generator, return the prompts and identify which covers are still missing.

  `Painted editorial movie poster for PLAYER GROSSIP. Show [subject and reaction] in [story-specific scene], with [one or two props integrated into the scene]. Use [palette and mood]. Set the exact headline to “[short English headline]”. Keep people, the key prop, and all lettering inside safe margins. Compose specifically for [1920×1080 landscape or 522×652 portrait].`

## Validate and deliver

- Read each draft on its own. Check both titles, paragraph indents, and factual consistency. Match every photo number to its source record.
- Read the dimensions of the final PNGs. Open the exported images and check the series name, headline spelling, subjects, and key props.
- Provide separate links for both covers and both drafts, plus individual photos or a photo ZIP, the numbered preview, and the complete episode ZIP. Name new bundles `episode-package.zip`. Include both covers, both drafts, numbered photos, the preview, the source list, verification notes, and the prompt files `poster_prompt.txt` and `poster_vertical_522x652_prompt.txt`. Reopen the ZIP and check that names are unique and the files extract. When running as a skill, use `scripts/check_covers.py <episode-directory> --bundle <episode-zip> --full`.
- To add a portrait cover to a previous episode, reference that episode's approved cover. Put the new **522×652** PNG in the original folder. Write a temporary ZIP there with the replacement portrait and prompt. Keep the prior files on disk. Replace the official ZIP only after confirming both covers and the existing drafts and photos are present and the new archive passes validation.
- Lead with the completed deliverables and links. If web access, image generation, local file handling, or verified photos are missing, deliver what is available and specify the gap. Describe the package as complete only after it passes validation. Upload or publish only if the user requests it.

## Episode input

- Topic or reference: screenshot, link, or story description.
- Scope: full package by default; specify a smaller task if needed.
- Optional: main and supporting subjects, photo numbers, tone, and references.
- For revisions: the existing episode folder or ZIP.
