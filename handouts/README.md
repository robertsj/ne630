# NE 630 board-supported handout framework

This package contains a reusable LaTeX class and two-page handouts for Lessons
1--6.
The design separates three kinds of content:

1. **Fixed inputs** -- reading, objectives, notation, constants, data tables, and problem statements that students should not have to copy from the board.
2. **Board-built structure** -- partially completed derivations, bookkeeping tables, and ruled spaces that are filled as the lesson develops.
3. **Study checks** -- compact prediction, interpretation, and synthesis prompts.

The default layout uses US Letter paper, two columns, approximately half-inch margins, a modern print-friendly typeface, and a restrained K-State-purple accent. The boxes retain their hierarchy when printed in grayscale.

## Typography

The handouts use Adobe Myriad Pro for text and Libertinus Math for equations.
The class loads Myriad Pro from a local font installation rather than copying
the proprietary font into this repository. It detects the standard Windows font
directory from WSL (/mnt/c/Windows/Fonts/), native Windows TeX
(C:/Windows/Fonts/), and Jeremy's local Adobe CC font cache
(/home/robertsj/.local/share/fonts/adobe-cc/). If Myriad Pro is unavailable, it
falls back to TeX Gyre Heros so drafts still compile.

The configured text faces are Myriad Pro Regular, Semibold, and Semibold Italic.
Because this installation does not include the regular italic face, regular
italics use a subtle synthetic slant.

## Color semantics

Color identifies a box's instructional role, not its subject:

- **Purple** marks supplied reference material, vocabulary, and course hierarchy.
- **Gray** marks space students construct during lecture.
- **Orange** marks a formative checkpoint or decision.
- **Teal** marks synthesis, a key result, or an instructor-only reveal.

Titles provide the same distinctions for grayscale printing. In the student
version, graph curves and annotations are suppressed so plotted figures begin
as labeled blank axes; the instructor version overlays the completed curves.

## Files

- `ne630boardhandout.cls` -- reusable document class.
- `handout_template.tex` -- blank two-page starting point with comments.
- `lesson_01_handout_body.tex` -- all Lesson 1 content.
- `lesson_01_handout.tex` -- student wrapper.
- `lesson_01_handout_instructor.tex` -- instructor wrapper; reveals selected source-derived board results. Instructor cues are retained as comments in the shared body source.
- `lesson_02_handout_body.tex` -- shared Lesson 2 content.
- `lesson_02_handout.tex` -- Lesson 2 student wrapper, including blank-axis graphs.
- `lesson_02_handout_instructor.tex` -- Lesson 2 instructor wrapper with completed graphs and selected results.
- `lesson_03_handout_body.tex` -- shared Lesson 3 radioactive-decay content.
- `lesson_03_handout.tex` -- Lesson 3 student wrapper.
- `lesson_03_handout_instructor.tex` -- Lesson 3 instructor wrapper with selected results revealed.
- `lesson_04_handout_body.tex` -- shared Lesson 4 neutron-attenuation content.
- `lesson_04_handout.tex` -- Lesson 4 student wrapper.
- `lesson_04_handout_instructor.tex` -- Lesson 4 instructor wrapper with selected results revealed.
- `lesson_05_handout_body.tex` -- shared Lesson 5 cross-section-data and reaction-probability content.
- `lesson_05_handout.tex` -- Lesson 5 student wrapper, with a spectrum reference and reaction-probability workspaces.
- `lesson_05_handout_instructor.tex` -- Lesson 5 instructor wrapper with selected interpretations and results revealed.
- `lesson_06_handout_body.tex` -- shared Lesson 6 cross-section-shape and resonance content.
- `lesson_06_handout.tex` -- Lesson 6 student wrapper, including the cross-section figures from the slide deck.
- `figures/` -- supporting PGF figures used by Lesson 6.
- `spectra.pdf` -- supporting spectrum figure used by Lesson 5.
- `Makefile` -- builds the available student and instructor PDFs with `latexmk`.

## Build

```bash
make
```

Build only one student handout with its uppercase lesson target:

```bash
make L06
```

The lowercase legacy targets (for example, `make lesson05`) build both the
student and instructor versions when both wrappers exist. You can also compile
a single version directly:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error lesson_02_handout.tex
```

Remove temporary LaTeX files while retaining compiled PDFs:

```bash
make tidy
```

Remove temporary files and compiled PDFs:

```bash
make clean
```

## Core interface

```tex
\documentclass[student]{ne630boardhandout} % or instructor
\HandoutSetup{NE 630}{01}{Lesson title}{FNRP Sections X.X--X.X}

\begin{document}
\MakeHandoutTitle
\begin{handoutcolumns}
  ...
\end{handoutcolumns}
\end{document}
```

Useful components are:

```tex
\HandoutSection{1}{Section title}
\begin{fixedbox}{Fixed inputs} ... \end{fixedbox}
\begin{boardbox}{Board development} ... \end{boardbox}
\begin{checkpoint}[Prompt title] ... \end{checkpoint}
\begin{takeawaybox}[Synthesis] ... \end{takeawaybox}
\Blank[1.0in]
\RevealBlank[1.0in]{instructor-only result}
\RuledLines{3}
\InstructorCue{Instructor-only note.}
```

## Recommended authoring rule

Start with the two-page limit. Put on the sheet only material that is expensive
or unhelpful to reproduce by hand: fixed data, long expressions, diagrams, and
problem statements. Leave reasoning transitions, intermediate algebra,
interpretation, and selected final results for lecture and student annotation.
