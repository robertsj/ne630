# NE 630 Homework QTI Conversion Feasibility Memo

Date: 2026-09-29

## Question

How hard would it be to convert an existing NE 630 homework statement and
solution into a Canvas quiz-compatible QTI format, using short answer, multiple
choice, file upload, and related Canvas question types to replace selected steps
in the current written problems?

## Short Answer

The QTI packaging problem is manageable. The instructional conversion problem is
the hard part.

NE 415 already has useful Canvas QTI machinery for multiple-choice and
file-upload exam items. That code can probably be adapted for NE 630 without
starting from scratch. However, the NE 630 homeworks and solution manual were
written as rich problem statements and worked TeX solutions, not as atomized
quiz items. A good conversion should not try to mechanically dump a solution
into QTI. It should create a reviewed intermediate item source that preserves
the structure of the written solution while choosing where Canvas questions
actually help.

For a first pilot, this is moderate effort. For a full HW01-HW13 conversion, it
is a real production workflow.

## Source Context Inspected

NE 630 currently has:

- Student-facing Markdown homework statements under `homework/markdown/`.
- Instructor-only solution sections under `homework/solutions/hwNN.tex`.
- A solution manual driver at `homework/solutions/fall_2026_ne630_solution_manual.tex`.
- A homework HTML builder at `homework/build.py`, with Canvas-oriented HTML
  fragments generated from Markdown.

Representative NE 630 cases:

- `homework/markdown/HW05.md` and `homework/solutions/hw05.tex`: good example
  of data lookup, calculation chains, tables, and intermediate numerical
  results. This is a strong candidate for short-answer, numerical, multiple
  choice, and selected file-upload/checkpoint items.
- `homework/markdown/HW10.md` and `homework/solutions/hw10.tex`: good example
  of OpenMC/code/data workflows plus a derivation. This should use file upload,
  essay/rubric, and a few checkpoint questions rather than trying to fully
  autograde the whole problem.

NE 415 already has:

- `../ne415_notes/exams/tools/qti_canvas_renderer.py`: a reusable-ish Canvas QTI
  1.2 package renderer for multiple-choice and multiple-answer items.
- `../ne415_notes/exams/exam2/tools/build_main_qti.py`: an example of deriving
  a QTI package from structured exam source.
- `../ne415_notes/exams/exam2/tools/build_code_qti.py` and
  `../ne415_notes/exams/exam1/tools/build_code_qti.py`: examples of Canvas
  file-upload QTI packages.
- `../ne415_notes/memos/QTILocalPreviewOptions_2026-06-25.md`: prior conclusion
  that local previews are useful for content QA, but Canvas sandbox import is
  the authoritative test.

## What Transfers Cleanly From NE 415

The following pieces are reusable or close to reusable:

- Building an IMS/QTI zip with `imsmanifest.xml` and an assessment XML file.
- Rendering Canvas-compatible question text with HTML and TeX math preserved in
  a Canvas-friendly form.
- Stable item IDs, objective references, local validation, key CSVs, and
  instructor preview artifacts.
- File-upload question shells for code, plots, notebooks, or long written work.
- A workflow where generated QTI is treated as a build product and Canvas import
  into a sandbox course is the final acceptance test.

The NE 415 code is exam-shaped rather than homework-shaped, but it gives us the
right spine.

## What Does Not Transfer Automatically

The NE 630 content introduces harder conversion issues:

- Statements are Markdown, while solutions are TeX. The correspondence between
  problem parts and solution steps is often implicit.
- Worked solutions contain explanatory prose, tables, figures, macros, and
  derivations that do not map one-to-one to Canvas question types.
- Many answers are numerical and data-dependent. These need tolerances,
  explicit units, and sometimes a pinned data source or cross-section library.
- Some problems ask for plots, code, or physical interpretation. These are not
  good candidates for pure autograding.
- QTI packages with correct answers are instructor-only artifacts. They should
  not be published beside student-facing homework HTML.

## Recommended Conversion Model

Use a structured intermediate source per homework or per problem, then generate
Canvas QTI from that source. Do not make the QTI zip the only editable artifact.

Suggested source layout:

```text
homework/qti/
  README.md
  schema.md
  questions/
    hw05.yaml
    hw10.yaml
  build_hw_qti.py
  build/
```

Each item should include:

- Stable question ID.
- Homework, problem, and optional solution-step reference.
- Question type.
- Student-facing prompt.
- Points.
- Expected answer, answer choices, tolerance, or rubric note.
- Units, data-source assumptions, and grading notes where needed.
- Optional objective tags.
- Optional feedback or worked-solution pointer.

This keeps the written homework and solution manual as the source of
instructional truth, while the YAML/JSON item source records the deliberate quiz
design choices.

## Canvas Question Type Mapping

Good fits:

- `multiple_choice_question`: conceptual checks, sign/direction choices,
  dominant interaction choices, reaction/channel identification, and qualitative
  interpretation.
- `multiple_answers_question`: "select all that apply" checks, assumptions,
  active terms in an approximation, or valid data sources.
- `numerical_question`: scalar intermediate values with tolerances. This would
  need to be added and import-tested in the NE 415 renderer style.
- `short_answer_question`: terse symbolic or text answers where exact matching
  is acceptable, or where Canvas is used as a collection point for manual review.
- `essay_question`: derivation checkpoints, physical interpretation, and
  explanation-heavy steps.
- `file_upload_question`: code, notebooks, plots, tables, or full written
  derivations. This is especially important for OpenMC/data workflow problems.

Use caution with:

- Long derivations converted to multiple choice. These can become artificial
  and may test recognition rather than reasoning.
- Short answer for numeric physics answers unless units, significant figures,
  and tolerances are handled cleanly.
- Matching/fill-in-multiple-blanks until Canvas import behavior is tested on the
  exact course platform.

## Pilot Plan

Start with one homework problem, not an entire course.

Recommended first pilot:

1. Choose one calculation-chain problem from HW05, such as a number-density,
   cross-section, or table-building problem.
2. Create a small `homework/qti/questions/hw05.yaml` with 8-12 reviewed items:
   a mix of conceptual multiple choice, numerical checkpoints, and one
   file-upload or essay item for the final work product.
3. Adapt the NE 415 QTI renderer into `homework/qti/build_hw_qti.py`.
4. Generate three artifacts:
   - Canvas QTI zip.
   - Instructor key/rubric CSV.
   - Local HTML/Markdown preview for quick content review.
5. Import the QTI zip into a Canvas sandbox course and check equations, tables,
   scoring, feedback, question order, and Student View.
6. Revise the schema before expanding to another problem.

Second pilot:

- Use HW10 for a code/plot/derivation-heavy case. This will test whether the
  workflow supports file upload and essay/rubric items without forcing
  everything into autograded form.

## Effort Estimate

For one problem:

- Simple proof of concept using multiple choice and file upload only: about
  half a day to one day.
- Stronger proof of concept with numerical/short-answer support and Canvas
  sandbox import QA: about one to two days.

For one full homework:

- Two to four days is a realistic first-pass estimate, mostly because item
  authoring and instructor review dominate the XML generation work.

For HW01-HW13:

- Roughly two to four weeks, depending on how aggressively each written problem
  is decomposed into quiz items and how much Canvas QA is required.

These estimates assume the NE 415 renderer can be adapted locally and that
Canvas sandbox access is available for import testing.

## Main Risks

- Over-atomizing the homework could make the quiz feel like a checklist rather
  than a coherent engineering problem.
- Under-specifying numerical tolerance and units could create grading friction.
- Local QTI validation can pass while Canvas import/rendering still has issues.
- Autograded QTI packages contain answer keys, so generated zips and key files
  need instructor-only handling.
- If the generator pulls homework inventory from `homework/build.py`, it should
  not blindly inherit the current hard-coded HW01-HW06 list, since the repo also
  contains later homework files.

## Recommendation

Proceed with a QTI overlay pilot rather than a full automatic conversion.

The best first milestone is a single HW05 problem converted into a reviewed QTI
quiz package with a local preview and Canvas sandbox import. That will answer
the important questions quickly: how math renders, how numerical checkpoints
behave, how much authoring time is required, and whether students would benefit
from Canvas quiz structure without losing the substance of the written solution.

If the pilot works, expand by problem archetype:

1. Calculation chain with numerical checkpoints.
2. Data lookup and table construction.
3. Plot/code workflow with file upload.
4. Derivation/explanation with essay rubric.
5. Mixed conceptual checks and final upload.

That staged path should preserve the strengths of the existing NE 630 written
homeworks while reusing the proven NE 415 QTI packaging work where it actually
helps.
