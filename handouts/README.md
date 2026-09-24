# NE 630 board-supported handout framework

This package contains a reusable LaTeX class and two-page handouts for Lessons
1--10 and 12--14.
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

## Recommended authoring rule

Start with the two-page limit. Put on the sheet only material that is expensive
or unhelpful to reproduce by hand: fixed data, long expressions, diagrams, and
problem statements. Leave reasoning transitions, intermediate algebra,
interpretation, and selected final results for lecture and student annotation.
