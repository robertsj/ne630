# Exercise Alignment

This folder records curated links between NE 630 learning objectives and
external textbook exercises.

The first pass covers only the objectives listed in `pages/lesson_01.md`,
`pages/lesson_02.md`, and `pages/lesson_03.md`.  Exercise references point to
stable files in the sibling `ne630_problems` repository.

## Files

- `lesson_01_03_catalog.yml` defines the lesson objective IDs and reusable
  orthogonal objective tags.
- `lesson_01_03_exercise_edges.psv` is the source of truth for exercise
  alignments.
- `lesson_01_03_coverage.md` is a human-readable index grouped by objective.

## Edge Format

`lesson_01_03_exercise_edges.psv` is pipe-separated:

```text
objective_id|book|exercise_id|problem_path|direct_basis|orthogonal_objectives|review_status
```

- `objective_id` uses `LNN.MACRO` or `LNN.M##`, where the micro objective
  numbering follows the order in the lesson page.
- `book` is one of `Lewis`, `DHNRA`, or `Lamarsh`.
- `exercise_id` is the book chapter/problem label.
- `problem_path` is repo-relative to `ne630_problems`.
- `direct_basis` is a short reason the exercise directly assesses the objective.
- `orthogonal_objectives` is a semicolon-separated list of recurring tags for
  identifiable exercise parts that are not among the selected Lesson 01-03
  objectives.
- `review_status` is `draft_curated` until reviewed.

The mapping rule for this seed file is intentionally strict: an exercise is
linked when the exercise statement asks students to perform the same named
calculation, explanation, or model construction as the NE 630 objective.  Later
reactor-physics contexts that reuse the same early skill are kept as direct
links, while their extra context is captured through orthogonal tags.
