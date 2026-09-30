---
name: "ne630-local-grading"
description: "Build or reproduce the NE630 local grading workspace from Canvas submission ZIPs, including normalized solution PDFs, solution tables, assessment UI, and feedback artifacts."
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

- `scripts/collect_solutions.py`: normalize Canvas submissions into one final-solution PDF per student group; can build suitable LaTeX ZIPs and convert image uploads to PDFs.
- `scripts/match_hw01_transcriptions.py`: populate HW01 rows from handwritten transcriptions plus PDF-text fallback.
- `scripts/match_hw02_latex.py`, `scripts/match_hw03_latex.py`, `scripts/match_hw04_latex.py`: seed expected rows and extract typeset/Route-B rows for those assignments.
- `scripts/assessment_server.py`: local browser assessment interface and CSV export.
- `references/solution_table_format.md` and `references/solution_table.schema.json`: row contract for solution tables.
- `assets/web/assessment/`: browser UI assets expected by `assessment_server.py`.

When bootstrapping a new machine, copy these resources into the grading root before running the pipeline:

```bash
mkdir -p "$NE630_GRADING_ROOT"/{bin,docs,schema,web/assessment}
cp "$NE630_REPO_ROOT"/skills/ne630-local-grading/scripts/*.py "$NE630_GRADING_ROOT"/bin/
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

## Assessment UI

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

For SpeedGrader feedback summaries, generate one pasteable block per student from `assessment/scores.json` and the solution table. Include only non-pass issues, the right answer where applicable, and a concise explanation of what seems to have gone wrong. Mark extraction misses as draft/verify-before-posting when scans or handwritten work are involved.

## Checks Before Reporting Done

Run checks proportional to the step completed:

- `python3 -m py_compile "$NE630_GRADING_ROOT"/bin/*.py`
- Manifest count equals normalized solution PDF count unless `needs_review.csv` explains the difference.
- Every normalized PDF has a `%PDF-` header; use `pdfinfo` page counts when available.
- Solution tables parse as JSONL and validate against `schema/solution_table.schema.json`.
- `reports/solution_table_summary.json` exists after table initialization.
- Errors/deferred rows accurately distinguish missing extraction from intentionally deferred handwritten work.
- For assessment UI work, confirm `scores.json` is valid JSON and CSV export returns expected student rows.

When reporting, include the grading root plus paths from that root, not only bare filenames. Call out deferred handwriting/transcription work and any typeset submissions with missing scalar extractions.
