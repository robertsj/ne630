# NE 630 Solution Table Format

Version: `ne630.solution_table.v0.1`

The solution table is a JSON Lines (`.jsonl`) file with one answer atom per
line. An answer atom is the smallest item worth comparing across submissions:
a numerical value, a completed reaction, an algebraic expression, a short
written conclusion, a code artifact, a figure, or a table.

Use this format for analytics and quick comparison, not as a replacement for
the original submissions. Every row must point back to the statement,
instructor solution, or student artifact from which it was extracted.

## Local Layout

For homework `hwNN`, use:

```text
<grading-root>/hwNN/
  raw/                         Original Canvas export and immutable inputs
  solutions/                   Normalized final-solution PDFs
  reports/                     Intake manifests
  tables/
    solution_table.jsonl        Expected and student answer rows
    solution_table.errors.jsonl Optional failed or uncertain extraction rows
  table_artifacts/              Cropped figures, code snippets, derived files
```

The schema lives at:

```text
<grading-root>/schema/solution_table.schema.json
```

## Source Inputs

For NE 630 Fall 2026, statement and reference solution sources are expected at:

```text
<ne630-repo>/homework/markdown/HWNN.md
<ne630-repo>/homework/html/HWNN.html
<ne630-repo>/homework/solutions/hwNN.tex
```

Prefer `markdown/HWNN.md` for student-facing prompt text and
`solutions/hwNN.tex` for instructor reference answers. Use the HTML when the
Markdown source is absent or when the HTML contains a newer Canvas fragment.

Student artifacts should normally come from:

```text
<grading-root>/hwNN/solutions/*_solution.pdf
<grading-root>/hwNN/reports/solution_manifest.csv
```

## Row Identity

Rows are grouped by:

- `homework_id`: `hw01`, `hw02`, ...
- `problem_id`: `p01`, `p02`, ...
- `part_id`: optional part label such as `a`, `b`, `q1`, or `reaction_1`
- `answer_id`: stable answer atom id such as `q_value`, `completed_reaction`,
  `percent_error`, or `sanity_check`
- `source.role`: `expected` for instructor solution rows, `student` for
  extracted student rows
- `source.student_group`: normalized `slug_userid` for student rows

Keep `answer_id` stable once analytics are built on it. If an old id was poor,
add a new row and mark the old row obsolete in downstream tooling rather than
silently changing historical tables.

## Answer Kinds

`answer_kind` and `value.kind` must agree.

- `numerical`: scalar numerical answer with optional unit and tolerances.
- `algebraic`: equation, completed reaction, symbolic expression, or formula.
- `short_answer`: prose conclusion or qualitative explanation.
- `code`: code snippet or artifact path with language/hash.
- `figure`: figure artifact path, caption, and optional alt text/hash.
- `table`: tabular values stored inline or by artifact path.
- `mixed`: small composite answer when splitting would destroy context.

## Provenance

Every row must include:

- `prompt.statement_path` and a useful `statement_locator` when known.
- `reference.solution_path` and `solution_locator` for expected rows or when a
  student row is compared to a reference answer.
- `source.path`, which is the normalized artifact for student rows or the
  solution source for expected rows.
- `evidence`, usually a short text or LaTeX excerpt and, when possible, a
  page/locator from the PDF or source file.
- `extraction.method`, `extraction.confidence`, and `extraction.needs_review`.

Use absolute paths in local artifacts while the pipeline is local. Later export
layers can remap paths to project-relative or content-addressed URIs.

## Comparison Fields

The optional `comparison` object records quick analytic status. It is not a
grade by itself.

Recommended methods:

- `numeric_tolerance` for numerical quantities with units.
- `symbolic_equivalence` for algebraic expressions after normalization.
- `rubric` for short-answer claims.
- `manual` when an automatic comparison is not reliable.

Use `manual_review` status whenever extraction or comparison is uncertain.

## Minimal Example

```json
{"schema_version":"ne630.solution_table.v0.1","course":"NE 630","term":"Fall 2026","homework_id":"hw01","problem_id":"p01","part_id":"a","answer_id":"q_value","prompt":{"statement_path":"<ne630-repo>/homework/markdown/HW01.md","statement_locator":"Problem 1, reaction a"},"reference":{"solution_path":"<ne630-repo>/homework/solutions/hw01.tex","solution_locator":"Problem 1 solution, Q_1"},"source":{"role":"expected","path":"<ne630-repo>/homework/solutions/hw01.tex","locator":"Q_1"},"answer_kind":"numerical","value":{"kind":"numerical","value":-6.885,"unit":"MeV","display":"-6.885 MeV","tolerance_abs":0.01},"evidence":[{"kind":"latex","text":"Q_1 \\approx -6.885~\\mega\\electronvolt"}],"extraction":{"method":"manual_seed_from_instructor_solution","confidence":1.0,"needs_review":false}}
```

## Validation

Validate a table with Python's `jsonschema` package when available:

```bash
python - <<'PY'
import json
from pathlib import Path
from jsonschema import Draft202012Validator

schema = json.loads(Path("schema/solution_table.schema.json").read_text())
validator = Draft202012Validator(schema)
for line_no, line in enumerate(Path("hw01/tables/solution_table.jsonl").read_text().splitlines(), 1):
    validator.validate(json.loads(line))
print("ok")
PY
```

If `jsonschema` is not installed, still run a JSON parse pass and schema review
before using rows for analytics.
