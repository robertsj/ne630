---
name: "ne630-local-grading"
description: "Build or reproduce the NE630 local grading workspace from Canvas submission ZIPs, including normalized solution PDFs, solution tables, assessment UI, feedback artifacts, and supervised SpeedGrader queues."
---

# NE630 Local Grading

Use this skill when Jeremy asks to create, reproduce, repair, or extend the local NE630 grading pipeline from Canvas homework submission archives.

This is a local-only grading workflow. Preserve raw submissions, keep student artifacts outside the public NE630 course repo, and report enough paths/counts that the run can be audited later.

## Roots and Portability

Use explicit roots instead of assuming this machine:

- `NE630_REPO_ROOT`: NE630 repository checkout, default `/home/robertsj/Classes/ne630`.
- `NE630_GRADING_ROOT`: local private grading workspace, default `/home/robertsj/Classes/ne630_local_grading`.
- Windows downloads, when applicable: `/mnt/c/Users/Jeremy/Downloads`.

If the user says `ne630_grades`, `ne630_local_grading`, or another path, treat that as the grading root and set `NE630_GRADING_ROOT` for helper scripts.

The grading root should use this layout:

```text
<grading-root>/
  bin/
  docs/
  schema/
  automation/
  web/assessment/
  hwNN/
    raw/
    solutions/
    reports/
    work/
    tables/
    table_artifacts/
    assessment/
```

## Bundled Resources

This skill includes reusable starting points:

- `scripts/collect_solutions.py`: normalize Canvas submissions into one final-solution PDF per student group; can build suitable LaTeX ZIPs and convert image or notebook-only uploads to archival PDFs.
- `scripts/match_hw01_transcriptions.py`: populate HW01 rows from handwritten transcriptions plus PDF-text fallback.
- `scripts/match_hw02_latex.py`, `scripts/match_hw03_latex.py`, `scripts/match_hw04_latex.py`: seed expected rows and extract typeset/Route-B rows for those assignments.
- `scripts/assessment_server.py`: local browser assessment interface and CSV export.
- `scripts/feedback_summaries.py` and `scripts/generate_canvas_feedback.py`: create pasteable Canvas feedback artifacts from `assessment/scores.json` and solution-table evidence.
- `scripts/build_speedgrader_queue.py`: merge Canvas gradebook roster rows with generated feedback, producing a roster-ordered SpeedGrader queue with submitted/no-submission handling.
- `scripts/speedgrader_autopilot.js`: supervised Playwright paste assistant for SpeedGrader; copy it into `automation/single_hw.js` when needed.
- `references/solution_table_format.md` and `references/solution_table.schema.json`: row contract for solution tables.
- `assets/web/assessment/`: browser UI assets expected by `assessment_server.py`.

When bootstrapping a new machine, copy these resources into the grading root before running the pipeline:

```bash
mkdir -p "$NE630_GRADING_ROOT"/{bin,docs,schema,automation,web/assessment}
cp "$NE630_REPO_ROOT"/skills/ne630-local-grading/scripts/*.py "$NE630_GRADING_ROOT"/bin/
cp "$NE630_REPO_ROOT"/skills/ne630-local-grading/scripts/speedgrader_autopilot.js "$NE630_GRADING_ROOT"/automation/single_hw.js
cp "$NE630_REPO_ROOT"/skills/ne630-local-grading/references/solution_table_format.md "$NE630_GRADING_ROOT"/docs/
cp "$NE630_REPO_ROOT"/skills/ne630-local-grading/references/solution_table.schema.json "$NE630_GRADING_ROOT"/schema/
cp "$NE630_REPO_ROOT"/skills/ne630-local-grading/assets/web/assessment/* "$NE630_GRADING_ROOT"/web/assessment/
chmod +x "$NE630_GRADING_ROOT"/bin/*.py
```

Do not overwrite an existing grading root blindly. Inspect the current files, preserve generated reports, and only refresh scripts/assets when the user asks or when the task requires the newer helper behavior.

## Intake Procedure

1. Normalize the homework id to `hwNN`.
2. Locate the Canvas ZIP. Common Windows download names are `hw4_subs.zip.zip`, `hw3_subs.zip.zip`, `hw2_subs.zip.zip`, or browser-renamed `submissions (N).zip`.
3. Copy the raw archive into `<grading-root>/<hwNN>/raw/`, using a stable name such as `hw4_subs.zip`.
4. Run the collector:

```bash
NE630_GRADING_ROOT=/path/to/grading-root \
NE630_REPO_ROOT=/path/to/ne630 \
python3 "$NE630_GRADING_ROOT/bin/collect_solutions.py" \
  "$NE630_GRADING_ROOT/hwNN/raw/<archive>.zip" \
  --clean-output
```

5. Inspect `reports/solution_manifest.csv` and `reports/needs_review.csv`.
6. Confirm normalized PDFs:

```bash
find "$NE630_GRADING_ROOT/hwNN/solutions" -maxdepth 1 -name '*_solution.pdf' | wc -l
```

For ZIP submissions, prefer exact `solution.pdf`. Avoid `discourse.pdf`, `transcript`, `chat`, `dialogue`, and source-only files unless the task is specifically about AI disclosure. If the collector selects a nonstandard PDF, inspect the manifest row and candidates before trusting it.

Notebook-only submissions are converted to archival PDFs from saved markdown/code cells and saved outputs without executing student code. If a student submits both a notebook and a PDF, the submitted PDF remains the preferred final-solution artifact.

For AI-dialogue extraction or prompt inventories, use the separate `ai-dialogue-grading` skill; do not mix dialogue inventory with final-solution normalization unless the user asks for both.

## Solution Tables

Create `tables/solution_table.jsonl` and `tables/solution_table.errors.jsonl` using the local format in `docs/solution_table_format.md`.

Rules:

- Expected rows come from `$NE630_REPO_ROOT/homework/markdown/HWNN.md` and `$NE630_REPO_ROOT/homework/solutions/hwNN.tex`.
- Student rows come from normalized solution PDFs and supporting text artifacts under `table_artifacts/`.
- For typeset/Route-B submissions, extract supported scalar final answers with `pdftotext` and regex/manual rules.
- For algebraic derivations and short-answer explanations, store section excerpts with `manual_review` comparison rather than pretending automatic equivalence.
- For direct scan PDFs or handwritten variants, create explicit deferred/error rows until transcriptions exist. Do not guess from image-only PDFs.
- Keep comparison separate from grading. A row status is an analytics hint, not a score.

Current homework-specific initializers:

```bash
NE630_GRADING_ROOT=/path/to/grading-root NE630_REPO_ROOT=/path/to/ne630 \
  python3 "$NE630_GRADING_ROOT/bin/match_hw04_latex.py"

NE630_GRADING_ROOT=/path/to/grading-root NE630_REPO_ROOT=/path/to/ne630 \
  python3 "$NE630_GRADING_ROOT/bin/match_hw03_latex.py"

NE630_GRADING_ROOT=/path/to/grading-root NE630_REPO_ROOT=/path/to/ne630 \
  python3 "$NE630_GRADING_ROOT/bin/match_hw02_latex.py"
```

For HW01 handwritten transcriptions, set the transcription root explicitly:

```bash
NE630_GRADING_ROOT=/path/to/grading-root \
NE630_REPO_ROOT=/path/to/ne630 \
NE630_HW01_TRANSCRIPTION_ROOT=/path/to/hw1_handwritten_scan_candidates_YYYYMMDD \
python3 "$NE630_GRADING_ROOT/bin/match_hw01_transcriptions.py"
```

For a new homework, copy the closest `match_hwNN_latex.py` pattern, define answer atoms from the prompt/reference solution, and preserve the same JSONL/schema contract. If the homework has many qualitative parts, prefer manual-review text rows over fragile automatic scoring.

## Assessment UI and Feedback

After a solution table exists, start the local browser UI:

```bash
NE630_GRADING_ROOT=/path/to/grading-root NE630_REPO_ROOT=/path/to/ne630 \
python3 "$NE630_GRADING_ROOT/bin/assessment_server.py" --host 127.0.0.1 --port 8765
```

Open:

```text
http://127.0.0.1:8765/assessment/?hw=hwNN
```

The UI reads `tables/solution_table.jsonl`, `tables/solution_table.errors.jsonl`, `reports/solution_manifest.csv`, and `assessment/scores.json`. It writes scores locally and exports CSV through `/api/hw/hwNN/export.csv`.

For SpeedGrader feedback summaries, generate one pasteable block per student from `assessment/scores.json` and the solution table:

```bash
NE630_GRADING_ROOT=/path/to/grading-root NE630_REPO_ROOT=/path/to/ne630 \
python3 "$NE630_GRADING_ROOT/bin/generate_canvas_feedback.py" hwNN
```

This writes:

- `hwNN/assessment/canvas_feedback.md`: human-readable review source.
- `hwNN/assessment/canvas_feedback.csv`: feedback rows keyed by local `student_group`.
- `hwNN/assessment/canvas_feedback.json`: structured version for audit/debug.

Feedback style matters. Include only non-pass issues. For scalar answers, do not stop at the final expected value; use the reference-solution excerpt carried in the solution table to write "I get X from [compact reference step], but it looks like you got Y" whenever that evidence is available. Put the "because/from" clause on the reference-solution calculation, assumption, sign convention, or unit conversion, not on a guessed student motive. Because feedback is pasted directly into Canvas, convert common LaTeX math in generated feedback to readable Unicode/plain text such as `→`, `≈`, `Σ`, `σ`, `λ`, `η`, superscript isotope mass numbers, and simple subscripts; do not rely on Canvas rendering TeX. Avoid directionless comments such as "make the final claim, assumptions, and supporting reasoning explicit" unless the same sentence also gives a concrete anchor: the reference calculation, a compact expected answer, the student's extracted value, or a named example of what should have been stated. When several qualitative items share the same problem-level advice, group them if useful, but include at least one "for example" or "concrete anchor" comparison so the student has something actionable. For open-ended or assumption-heavy prompts, avoid the brittle "I expected X, but you got Y" pattern; instead give a compact reference answer, then say whether the student took roughly the same path or an alternative path, and ask them to make assumptions/units explicit. Keep the tone compact, personal, and useful rather than numerically punitive.

Canvas score uploads are not the same as the local assessment totals. For normalized one-point Canvas assignments:

- Students with submissions get Canvas score `1`; put the real grading value in the feedback.
- Students with no submission get Canvas score `0` and comment exactly `Not submitted.`

Before SpeedGrader posting, export the Canvas gradebook CSV and build a roster-ordered queue:

```bash
NE630_GRADING_ROOT=/path/to/grading-root NE630_REPO_ROOT=/path/to/ne630 \
python3 "$NE630_GRADING_ROOT/bin/build_speedgrader_queue.py" \
  hwNN /mnt/c/Users/Jeremy/Downloads/<grades-export>.csv
```

The queue file is `hwNN/assessment/speedgrader_queue.csv`. It is the posting source of truth because it includes roster order, Canvas user id, `submission_status`, `canvas_score`, and `feedback_text`. Match feedback to roster rows by Canvas user id, not by display name.

## Supervised SpeedGrader Posting

Use Playwright as a supervised paste assistant, not as unattended grading. Do not put credentials in scripts. Either pass a SpeedGrader URL or navigate manually in the launched browser:

```bash
cd "$NE630_GRADING_ROOT"
SPEEDGRADER_URL='<SpeedGrader URL for the first queued student>' \
STUDENT_COUNT=3 \
node automation/single_hw.js
```

The script should:

- Prefer `hwNN/assessment/speedgrader_queue.csv` when present; otherwise fall back to `canvas_feedback.csv`.
- Preview the row, including internal score and Canvas score.
- Fill the grade box and comment box only.
- Submit only after an explicit terminal confirmation.
- Advance to the next Canvas student only after a second explicit confirmation.

Use preview mode before a posting run:

```bash
cd "$NE630_GRADING_ROOT"
PREVIEW_ONLY=1 STUDENT_COUNT=3 node automation/single_hw.js
```

If the queue includes no-submission rows, verify that they preview with `submission_status=no_submission`, Canvas score `0`, and feedback `Not submitted.` before posting.

## Checks Before Reporting Done

Run checks proportional to the step completed:

- `python3 -m py_compile "$NE630_GRADING_ROOT"/bin/*.py`
- Manifest count equals normalized solution PDF count unless `needs_review.csv` explains the difference.
- Every normalized PDF has a `%PDF-` header; use `pdfinfo` page counts when available.
- Solution tables parse as JSONL and validate against `schema/solution_table.schema.json`.
- `reports/solution_table_summary.json` exists after table initialization.
- Errors/deferred rows accurately distinguish missing extraction from intentionally deferred handwritten work.
- For assessment UI work, confirm `scores.json` is valid JSON and CSV export returns expected student rows.
- For feedback work, regenerate `canvas_feedback.*`, review the `.md` file, then build `speedgrader_queue.csv` from a Canvas gradebook export and confirm submitted/no-submission counts.
- For SpeedGrader automation work, run `node --check "$NE630_GRADING_ROOT/automation/single_hw.js"` and `PREVIEW_ONLY=1 STUDENT_COUNT=<small N> node "$NE630_GRADING_ROOT/automation/single_hw.js"` before any browser posting.

When reporting, include the grading root plus paths from that root, not only bare filenames. Call out deferred handwriting/transcription work and any typeset submissions with missing scalar extractions.
