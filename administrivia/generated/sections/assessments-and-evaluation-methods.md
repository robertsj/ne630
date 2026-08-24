### Homework

Homework is assigned regularly. Unless Canvas says otherwise, homework associated with lesson N is due by the start of lesson N + 2. Every homework submission must follow exactly one of the two routes below.

#### Route A: No Generative AI Used for the Assignment

If no generative AI informed any part of the submitted work, submit one PDF. The PDF may be typeset or may contain clean scans of handwritten work. Your name, the course name, and the homework number must appear on the first page. Start each problem on a new page, include the full problem statement, clearly mark final answers, and write enough plain English that I can follow the reasoning.

Handwritten work must be scanned as US-letter pages at 300 dpi, in grayscale or color, with pages upright, tightly cropped, and free of shadows or visible background clutter. Do not submit photographs embedded in a PDF when a scan is reasonably available. I will allow one no-penalty resubmission during the semester solely to correct scan or document-formatting problems. Later nonconforming submissions may be returned for correction, with the original deadline still controlling unless I approve an exception.

#### Route B: Generative AI Used for the Assignment

If generative AI informed any part of the submitted work, submit one `.zip` archive rather than a stand-alone PDF. This route applies even when AI was used only for an explanation, derivation, calculation, code, debugging, checking, editing, formatting, or preparation of a supporting file. When in doubt about whether a tool or interaction counts, use Route B.

The archive must contain, at minimum:

- `solution.tex`, the polished final solution;
- `solution.pdf`, compiled from `solution.tex`;
- `discourse.tex`, containing the complete visible AI dialogue as defined in the Artificial Intelligence and Technology Use policy below;
- `discourse.pdf`, compiled from `discourse.tex`;
- `Makefile`, whose default target builds both PDFs; and
- every script, notebook, data file, bibliography, figure source, input file, or other artifact needed to reproduce or understand the submitted work.

`discourse.tex` may contain the transcript directly or may typeset an included plain-text export such as `discourse.txt`; any file it reads must also be in the archive.

The archive must be self-contained, use relative paths, and unpack into one ordinary directory without nested archives. Running `make` from the top level must produce `solution.pdf` and `discourse.pdf` without requiring files stored elsewhere on your computer. Do not include virtual environments, package caches, or unrelated files. When a specialized program or package is required, identify it clearly in a short `README.txt`.

The final solution must meet the same readability requirements as Route A: include the full problem statement, begin each problem on a new page, clearly mark final answers, and provide enough explanation to make the reasoning traceable. AI output does not need to be copied into the final solution merely because it appears in the discourse; `solution.tex` should be the coherent submission you intend me to grade.

The complete discourse is a submission requirement, but it is not graded for prompt count, speed, polish, or absence of false starts. Unsuccessful attempts, corrections, and changes of direction are normal and useful. The final solution and your demonstrated understanding remain the primary bases for the homework grade.

The lowest homework score is dropped. Late homework is not accepted after solutions have been posted, which, by default, is at the due time.

### Exams

The course has three exams. The first two are in-class exams. The third exam uses the university final exam period for the section unless Canvas announces an approved alternative.

Exams are not AI-enabled. Unless I announce otherwise, they are completed without generative AI, internet access, external communication, or access to prior AI dialogues. Allowed resources are limited by default to a writing utensil, a calculator, and an instructor-provided page of notes. That page will be provided no later than the class meeting before the exam.

A practice exam will be provided at least one class meeting before each exam. Exam problems will parallel selected portions of homework assignments and lesson examples in structure, required skills, and expected depth, although numbers, settings, and combinations of ideas may change.

The documented problem-solving progression and session timing in AI-assisted homework give both of us useful evidence about where time is being spent and how quickly the material is becoming usable. I may use that evidence, together with in-class work and the practice exam, to calibrate exam scope and length so that the exam measures reactor-theory mastery rather than merely rewarding unusual speed. The pace or number of prompts in an individual transcript is not itself a graded quantity.

To encourage timely and complete TEVAL responses, I will add one percentage point to every student's final course average if, and only if, the class TEVAL completion rate is 100% before the final examination begins.
