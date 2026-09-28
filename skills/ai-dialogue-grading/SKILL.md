---
name: "ai-dialogue-grading"
description: "Extract AI dialogue disclosures from NE630 Canvas homework ZIPs and build anonymized prompt inventories for local grading."
---

# AI Dialogue Grading

Use this skill when an NE630 homework archive may contain Route B / full-disclosure AI dialogue artifacts and the local grading tree needs an `extracted/ai_dialogues` workspace.

## Inputs

- Canvas submission ZIP, often named like `hw4_subs.zip` or a browser-renamed variant such as `hw4_subs.zip.zip`.
- Assignment label such as `hw01`, `hw04`, or `hw4`.
- Local grading root, normally `/home/robertsj/Classes/ne630_local_grading`.
- NE630 syllabus or policy text when detection rules need to be justified.

## Procedure

1. Normalize the assignment label to `hwNN` and create only the directories needed for AI-dialogue work unless the user asks for full grading:
   - `<grading-root>/<hwNN>/raw`
   - `<grading-root>/<hwNN>/extracted/ai_dialogues`
   - `<grading-root>/<hwNN>/extracted/ai_dialogues/by_student`

2. Preserve the source archive in `raw/`. If the source filename has an accidental double suffix, prefer the normalized raw name `<assignment>_subs.zip` and record the original source path in generated manifests.

3. Inspect the top-level Canvas archive without unpacking unrelated files into the grading tree. Treat nested `.zip` submissions as likely Route B candidates only when their contained artifact filenames, not merely their folder names, match dialogue evidence terms such as `discourse`, `transcript`, `dialogue`, `conversation`, `chatgpt`, `claude`, `copilot`, `ai`, or `screenshot`.

4. For each detected AI-dialogue submission, create:
   - `by_student/<student_key>/dialogue/` with only dialogue-facing files and LaTeX-included transcript dependencies.
   - `by_student/<student_key>/full_submission/` with the full nested ZIP extraction when a nested Route B ZIP exists.
   - `by_student/<student_key>/README.md` with source entry, route cue, and navigation notes.

5. Write `students.csv`, `manifest.csv`, and top-level `README.md` in `ai_dialogues/`. Include original archive entry paths, copied artifact paths, sizes, and SHA-256 hashes. Keep reports anonymizable and navigable; do not grade or score dialogue quality.

6. Unless the user asks for extraction only, parse student-side turns from the extracted `discourse.*` sources, cluster duplicate and near-duplicate prompts by theme, and write the results under `ai_dialogues/prompt_inventory/`. Attribute by anonymous source IDs only. Treat this inventory as a deterministic review aid; inspect source dialogue artifacts when a prompt is ambiguous.

## Helper Script

Use `scripts/extract_ai_dialogues.py` for the extraction and initialization pass:

```bash
python3 /home/robertsj/Classes/ne630/skills/ai-dialogue-grading/scripts/extract_ai_dialogues.py \
  --assignment hw04 \
  --source /path/to/hw4_subs.zip \
  --grading-root /home/robertsj/Classes/ne630_local_grading
```

The script initializes the AI-dialogue tree, extracts dialogue artifacts, and builds `prompt_inventory/` by default. Add `--no-prompt-inventory` when the user only wants the extraction/initialization pass. The script does not perform solution collection, scoring, or table extraction.

## Checks

- Confirm `students.csv` row count matches the number of detected AI-dialogue-bearing submissions.
- Confirm every `manifest.csv` artifact path exists.
- Confirm `dialogue/` does not contain ordinary solution files, Makefiles, READMEs, or ZIPs unless the filename itself is a dialogue artifact requested by the policy.
- Confirm `prompt_inventory/representative_prompts.md`, `representative_prompts.csv`, and `anonymized_prompt_samples.csv` exist when prompt inventory generation was not skipped.
- Mention any stale memory/search caveat separately; repository files and generated manifests are authoritative for the run.
