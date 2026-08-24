# NE 630 Administrivia

This directory is the plain-text source of truth for NE 630 administrative
artifacts. The root `README.md` is now only a repository landing page; the
syllabus, schedule, CourseDog import artifact, and reusable communication
templates live here.

## Files

- `syllabus.md`: canonical syllabus source for Fall 2026 and later terms.
- `schedule.md`: detailed term schedule workflow. This is intentionally
  separate from the syllabus.
- `schedule-source.psv`: dated detailed schedule source for Canvas.
- `generated/syllabus-coursedog.md`: generated CourseDog-ready Markdown.
- `generated/schedule-canvas.html`: generated Canvas-safe schedule snippet.
- `generated/coursedog-fields.tsv`: generated section map for CourseDog field
  copy/paste workflows.
- `generated/coursedog-copy.html`: generated browser copy board for
  CourseDog WYSIWYG boxes.
- `generated/coursedog-copy-fields.tsv`: generated map from CourseDog field
  labels to raw per-field Markdown files.
- `generated/sections/*.md`: generated raw per-field Markdown slices for
  review and fallback copy/paste.
- `templates/first-day-announcement.md`: first Canvas/email announcement draft.
- `templates/syllabus-addendum.md`: dated addendum template for substantive
  post-submission syllabus changes.
- `tool/build_coursedog.py`: builder, validator, and CourseDog copy-page
  generator.
- `tool/build_canvas_schedule.py`: builder and validator for the Canvas
  schedule HTML snippet.

## K-State Syllabus Rules for Fall 2026

Policy snapshot: 2026-08-23.

The controlling policy is the K-State University Handbook, Section F, Course
Syllabus Policy, Sections 25-26. The policy is effective June 10, 2026, applies
to all credit-bearing K-State courses, and supersedes inconsistent older unit
guidance unless the Provost explicitly authorizes an exception.

Effective Fall 2026, CourseDog is the official university repository for all
credit-bearing syllabi. The CourseDog-submitted syllabus is the official
syllabus of record, is tied to the records retention schedule, and may be
subject to Kansas Open Records Act requests.

The instructor must provide the syllabus to students by the end of the first
class session. The final electronic syllabus must be submitted through
CourseDog no later than the 10th day of a standard 16-week semester, the 5th
day of an 8-week session, the 3rd day of a 4-week session, or the proportional
equivalent for other course lengths.

Every credit-bearing syllabus must include, at minimum:

- Basic course details, instructional modality, instructor contact information,
  catalog course description, required materials, Canvas/communication
  statement, and student support resource references.
- Student learning outcomes, grading scale, assessment weights, and applicable
  exam/proctoring/common-exam information.
- Course-specific policies for attendance, late work or make-up work, AI and
  technology use, and any relevant instructor-specific rules.
- A course schedule of activities. The handbook allows this to be a general
  roadmap by week, module, topic sequence, milestone, or another appropriate
  instructional unit. The syllabus does not need a full day-by-day schedule.
  It does need anticipated timing for major graded components.
- Mandatory university statements, included verbatim or by a direct accessible
  link to the Provost's Official Syllabi Statements page/CourseDog statements.

For Fall 2026, the handbook's mandatory university statement categories are:

- Academic Honesty, including the Honor Pledge.
- Students with Disabilities.
- Classroom Conduct.
- Mutual Respect and Inclusion.
- Discrimination, Harassment, and Sexual Harassment.
- Campus Safety and Emergency Procedures.

Older public K-State syllabus-statement materials may list only the first five
statements as mandatory and campus safety as optional. For Fall 2026 and
later, the June 10, 2026 University Handbook syllabus policy is the controlling
source and includes Campus Safety and Emergency Procedures among mandatory
statement categories.

The handbook also makes AI/technology guidance a required course-specific
policy. If an older Provost page describes AI language as "strongly
encouraged," use the handbook rule for CourseDog readiness.

All electronically distributed syllabi, including CourseDog and Canvas copies,
must conform to WCAG 2.1 Level AA. In practical terms, keep heading levels
semantic, use descriptive links, avoid layout tables, include table headers
for data tables, avoid image-only PDFs, include alt text for non-decorative
images, and do not rely on color alone.

Substantive post-submission revisions, such as changes to grading structures,
major assignments, exam dates, attendance policy, or core course expectations,
must be communicated to students in writing and retained as a dated addendum.
Routine pacing changes, updated readings, minor due date adjustments, and
similar instructional updates can be handled in Canvas without a formal
syllabus addendum.

## Workflow

1. Edit `syllabus.md` as the canonical source.
2. Keep the detailed day-by-day schedule in `schedule-source.psv` and Canvas,
   not in the syllabus.
3. Run:

   ```bash
   /home/robertsj/miniforge3/bin/python administrivia/tool/build_coursedog.py
   ```

4. Review `generated/syllabus-coursedog.md`.
5. Open `generated/coursedog-copy.html` in a browser. For each CourseDog
   WYSIWYG field, click **Copy rich text** on the matching local field and
   paste into CourseDog. If the browser blocks clipboard access, the page
   selects the rendered content so Ctrl+C can copy it.
6. Use `generated/coursedog-copy-fields.tsv` and `generated/sections/*.md`
   only as an audit trail or Markdown fallback. CourseDog's Fall 2026 form
   uses WYSIWYG boxes, not Markdown-file upload fields.
7. For the detailed Canvas schedule, run:

   ```bash
   /home/robertsj/miniforge3/bin/python administrivia/tool/build_canvas_schedule.py
   ```

8. Paste `generated/schedule-canvas.html` into Canvas's HTML editor. To print
   the snippet directly, use `--stdout`.
9. After CourseDog submission, commit the source, generated artifact, and any
   dated addenda.

## Annual Review Checklist

- Confirm the official meeting pattern, location, section number, and final
  exam block from KSIS/CourseDog/Registrar pages.
- Confirm the University Handbook Course Syllabus Policy has not changed.
- Confirm the Provost/CourseDog mandatory statements list has not changed.
- Confirm the catalog description, prerequisites, credit hours, and required
  materials.
- Update major exam dates in `syllabus.md`.
- Update the detailed schedule in `schedule-source.psv`.
- Run `tool/build_canvas_schedule.py` and confirm holiday/no-class rows match
  the official Canvas-followed academic calendar.
- Run `tool/build_coursedog.py` and resolve warnings before CourseDog import.

## Primary Sources

- K-State University Handbook, Section F, Course Syllabus Policy:
  https://www.k-state.edu/provost/policies-resources/university-handbook/fhsecf.html#syllabuspolicy
- K-State Official Syllabi Statements page:
  https://www.k-state.edu/provost/policies-resources/classroom-policies-teaching-resources/course-syllabi-statements/
- K-State CourseDog/Canvas announcement, August 11, 2026:
  https://blogs.k-state.edu/it-news/2026/08/11/new-canvas-tools-for-the-fall-semester/
- K-State Fall 2026 final examination schedule:
  https://www.k-state.edu/registrar/students/student_resources/term_final_examinations/fall2026/
- K-State 2026-2027 academic calendar:
  https://www.k-state.edu/registrar/students/calendar/
- NE 630 catalog entry:
  https://catalog.k-state.edu/preview_course_nopop.php?catoid=63&coid=437945
