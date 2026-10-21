# NE 630 board-supported handout framework

This package contains a reusable LaTeX class and printable handouts for Lessons
1--10 and 12--23.
The design separates three kinds of content:

1. **Fixed inputs** -- reading, objectives, notation, constants, data tables, and problem statements that students should not have to copy from the board.
2. **Board-built structure** -- partially completed derivations, bookkeeping tables, and ruled spaces that are filled as the lesson develops.
3. **Study checks** -- compact prediction, interpretation, and synthesis prompts.

The default layout uses US Letter paper, two columns, approximately half-inch margins, a modern print-friendly typeface, and a restrained K-State-purple accent. The boxes retain their hierarchy when printed in grayscale.

## Shared backend pilot (Lesson 22 only)

[`ne630handout.cls`](ne630handout.cls) is the new course-wide backend, with
Wildcat/Beamer colors and the combined board-handout and reading-guide
interfaces. **Only Lesson 22 is migrated.** The old class and chapter-style
backend remain unchanged for all other lessons.

See [the backend guide](handout_backend.md) for authoring, feature coverage,
future migration notes, and the Lesson 22 slide-coverage map. Build L22 with
`make L22`; run the isolated compatibility check with `make check-class`.
The current instructor-edited L22 builds as two Letter pages.

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
- **Teal** marks synthesis, a key result, or a solution-only reveal.

Titles provide the same distinctions for grayscale printing. With
`\handoutsolutionsfalse`, graph curves and annotations are suppressed so plotted
figures begin as labeled blank axes; switching the wrapper to
`\handoutsolutionstrue` overlays the completed curves and reveals selected
results.

## Files

- `ne630boardhandout.cls` -- reusable document class.
- `handout_template.tex` -- blank two-page starting point with comments.
- `lesson_XX_handout.tex` -- lesson wrapper with `\handoutsolutionsfalse` for the public handout.
- `lesson_XX_handout_body.tex` -- lesson body with blanks and solution payloads.
- `figures/` -- supporting figures used by Lessons 6, 7, and 10, including the
  OpenMC notebook that generates the U-238 threshold plot.
- `spectra.pdf` -- supporting spectrum figure used by Lesson 5.
- `Makefile` -- builds the public non-solution PDFs with `latexmk`.

Rendered `lesson_XX_handout.pdf` files are build artifacts. They are ignored on
the course-development branch and copied into the generated site during the
publication build. The published copies live on `gh-pages`.

## Build

```bash
make
```

Build only one handout with its uppercase lesson target:

```bash
make L07
```

The lowercase lesson targets are aliases for the public PDF targets. You can
also compile a single version directly:

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
\documentclass{ne630boardhandout}
\handoutsolutionsfalse % change to \handoutsolutionstrue for a private solution copy
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
\RevealBlank[1.0in]{solution-only result}
\RuledLines{3}
\SolutionCue{Solution-only note.}
```

## Legacy board-handout authoring rule

Start with the two-page limit. Put on the sheet only material that is expensive
or unhelpful to reproduce by hand: fixed data, long expressions, diagrams, and
problem statements. Leave reasoning transitions, intermediate algebra,
interpretation, and selected final results for lecture and student annotation.

## Lessons 22 and 23

Build with `make L22 L23` (or `make lesson22 lesson23`).

- `lesson_22_handout.tex` uses `ne630handout.cls`: two pages covering the
  Lesson 22 slides, including reactivity/control bookkeeping, iodine--xenon
  balances, equilibrium worth, transient code/results, and the samarium
  reading extension. Purple/orange equation emphasis follows the slides.
- `lesson_22_xenon_transient.py` is included directly as the printed listing;
  it requires NumPy, SciPy, and Matplotlib when run, but not to build the PDF.
  The equilibrium and transient examples intentionally retain distinct inputs.
- L22's capture cross section is a native PGF plot generated from OpenMC
  Xe135 MT=102 data; its text inherits the handout fonts. See the
  [figure guide](figures/README.md) for regeneration and data provenance.
  The transient figure remains a local copy of the slide figure.
- `lesson_23_handout.tex` is a two-page reading guide using
  `ne630_ch04_reading_guide_common.tex`. Its editable depletion chain is included
  directly from `figures/depletion_chain_tikz.tex`, retaining shared isotope
  columns and element rows with fixed-size stacked labels. FNRP equation
  numbers use `\tag`, with asterisks explained
  where the expression is modified. See the [figure guide](figures/README.md)
  for standalone compilation and the figure conventions.

Original Downloads files are untouched. Lessons 22 and 23 are published as
PDF-only handouts on the course site.
Committing source updates does not republish the site; a release must rebuild
and validate the student-facing exports separately.
