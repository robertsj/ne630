Build the guides with XeLaTeX and latexmk:

```sh
make                          # Every chapter (1-7, 10), portrait (the default)
make landscape                # Every chapter, landscape
make both                     # Both orientations of every chapter
make reference                # Dense landscape editions without writing space
make playwrite                # Landscape trials using Playwrite US Modern
make indie-euler              # Landscape trials: Indie Flower + Euler Math
make ch07_guide_landscape.pdf  # Just Chapter 7, landscape
make ch07_guide.pdf            # Just Chapter 7, portrait
```

Landscape output uses the `_landscape` suffix, with separate auxiliary files,
so both orientations can coexist. Both use US Letter paper, the same margins,
and the same 60/40 prompt/answer columns. The Makefile and `.latexmkrc` locate
the shared class in `../handouts`; no local class copy is needed.

The default edition divides multipart frames into paired subcells such as
F1(a), F1(b), and F1(c). Each question, its writing space, and its matching
feedback stay together on one page. Shared givens appear above the sequence;
illustrations that reveal a result appear in the corresponding feedback cell.
Subcells can continue onto a new page without splitting a question/answer pair.

Use one sheet to cover every row below the current cell and another to cover
its tinted answer. Write a response, reveal only that answer, and correct the
work before uncovering the next question. This keeps later questions covered
while students address a misconception.

Each subcell has three writing lines at 7 mm spacing; unsplit frames have four.
Use `\renewcommand{\GuideSubcellLines}{4}` to increase the default subcell space.
Sources pair each question and answer explicitly:

```tex
\begin{pframe}[Frame title]
\GuideContext{Shared givens, with no later questions or answers.}
\GuideSubcell{a}{First question}{First answer}
\GuideSubcell[4]{b}{Next question}{Next answer\GuideCommentary{Teaching note.}}
\end{pframe}
```

The optional argument to `\GuideSubcell` sets its number of writing lines.
The F-number remains stable for cross-references to the original frames.

Model answers use the locally installed Comic Neue font at 13 pt, with a 7 mm
baseline pitch matching the writing rules. Print at **Actual size / 100%** to
retain that scale. Prompts, headings, quizzes, and explanatory notes retain the
handout's Adobe Myriad Pro typography. Equations use the existing math font at
the answer's larger size. The `reference` edition keeps the compact typography.

`make playwrite` builds separate `_landscape_playwrite.pdf` editions with
Playwrite US Modern Regular, also at 13 pt and 7 mm spacing. Comic Neue remains
the default. The static Playwrite font and its SIL Open Font License are bundled
under `fonts/playwrite/`, with no system-wide installation required. The
`playwrite` package option can also be combined with `portrait`. Both fonts
have a lowercase x-height of about 2.3 mm at this size; Playwrite has taller
capitals and ascenders. Print the trials at 100% for comparison.

`make indie-euler` builds separate `_landscape_indie_euler.pdf` trials using
Indie Flower for handwritten prose and Euler Math for answer equations,
including Greek. Both use the existing 13 pt answer size and 7 mm line pitch.
Indie Flower has a light synthetic weight (`FakeBold=1.0`) to balance Euler.
Numbers and units produced by `siunitx` in model answers use the selected
handwriting font, matching the answer prose in every handwriting edition.
Prompts and explanatory notes retain Myriad Pro text and Libertinus Math.
The default Comic Neue editions and Playwrite trials remain available.

This pairing uses LuaLaTeX to support switching math fonts. Its font loader
uses a writable cache at `/tmp/ne630-reading-guide-luatex`; set `LUA_CACHE` to
another directory if desired. Its first run may take longer to index fonts.
Indie Flower and its license are bundled in `fonts/indieflower/`; Euler Math
must be available through the TeX installation. The package options
`indieflower` and `eulermath` can also be used independently.

Use `\GuideCommentary{...}` within a response for an instructional note in the
default font. To adjust the model handwriting, set
`\renewcommand{\GuideHandwritingSize}{14}` in the preamble; adjust the shared
line pitch with `\renewcommand{\GuideWritingPitch}{8mm}`. Comic Neue's regular,
bold, italic, and bold-italic OTF files must be installed for editions that use it.
Legacy unsplit responses can use `\GuideAnswerPart{a}`, `\GuideAnswerPart{b}`,
etc. Those markers add a paragraph break and a 2 mm gap in the writing edition;
adjust it with `\renewcommand{\GuideAnswerPartSkip}{3mm}`. New multipart frames
use `\GuideSubcell` to keep questions and feedback in separate paired rows.

Set `\renewcommand{\GuideWritingLines}{6}` in the preamble to increase writing
space throughout a guide. For an individual frame, use
`\begin{pframe}[Frame title][6]`. Use the package option `reference` to restore
the dense layout without writing space; it combines with either orientation:

```sh
latexmk -xelatex -jobname=ch07_guide_landscape_reference \
  -usepretex='\PassOptionsToPackage{landscape,reference}{ne630guide}' ch07_guide.tex
```

Orientation is a compile-time option of `ne630guide`. To select it in a source,
use `\usepackage[landscape]{ne630guide}` (or `[portrait]`). To build a landscape
variant without changing the source, as the Makefile does:

```sh
latexmk -xelatex -jobname=ch07_guide_landscape \
  -usepretex='\PassOptionsToPackage{landscape}{ne630guide}' ch07_guide.tex
```

`make tidy` removes auxiliary files for all editions, retaining PDFs;
`make clean` removes those PDFs too. `make verify` checks the numerical examples.
Both `make verify` and the figure-data rule run `tools/verify_examples.py`,
which needs NumPy and SciPy; pass `PYTHON=/path/to/python` if the default
interpreter lacks them (for this workspace,
`PYTHON=/home/robertsj/miniforge3/bin/python`). With `--write` the script
refreshes every table under `figures/data/`: the Bessel functions of the
Chapter 7 figure, the six-group step response of the Chapter 5 figure, and
the xenon, samarium, and depletion curves of the Chapter 10 figures.

Guides exist for Chapters 1-4 (`ch01_guide.tex` to `ch04_guide.tex`; Lessons
1-21), Chapter 5 (`ch05_guide.tex`; Lessons 25-29), Chapters 6-7 (Lessons
31-39), and Chapter 10 (`ch10_guide.tex`; Lessons 22-24). The Makefile
discovers `ch*_guide.tex`, so every target above applies to all of them. The
Chapter 1-5 and 10 sources label each frame (`\label{f:name}`) and cite it
with `\ref*{f:name}`, which prints the frame number with its F; frames can
then be inserted without renumbering the cross-references, key terms, or
problem tables. After adding or moving frames, update the frame tags in
`tools/verify_examples.py` to match.

The Chapter 4 guide ends with an addendum (its Section 7, frames F28-F35) on
FNRP 9.1-9.4: reactivity and its units, the additive form of the four-factor
formula, the temperature dependence of the resonance integral for UO2 and
uranium metal rods (FNRP Eqs. 9.13-9.14 and Table 9.1), the fuel and moderator
temperature coefficients, composite coefficients and defects, and the startup
reactivity budget. It sits there because Lessons 20-21 introduce reactivity
coefficients directly from the four-factor analysis of Lessons 17-19, and its
chains continue the PWR lattice of the Chapter 4 frames. The budget sketch is
`figures/feedback_schematics.tex`, adapted from the Lesson 20 handout.

The Chapter 10 guide includes a closing section on the linear reactivity
model and batch refueling, which is the Lesson 24 supplement rather than part
of Lewis's text, and reuses the Lesson 23 depletion chain
(`../handouts/figures/depletion_chain_tikz.tex`, found through `TEXINPUTS`).
Where a textbook problem is assigned as homework in the lesson pages (5.1,
5.2, 5.4, 5.9, 5.10, 5.15, 10.13, 10.14), the corresponding frames use
different numbers or materials so that the guide builds the method without
reproducing the assigned answer.

The Chapter 3 guide extends Lewis: its Sections 7 and 8 introduce the
multigroup method and the multigroup $k$-eigenvalue problem formally,
following the Lesson 13 and 14 handouts, because the text mentions multigroup
methods only in passing. `learning_objectives.md` compares the objectives
implied by Chapters 1-5 and 10 (and the Chapter 9 addendum) with the lesson
objectives in `../pages/` and flags new ones; the Chapter 6-7 comparison has
not been written.

The Chapter 4 guide reuses the lattice, neutron-cycle, and resonance sketches
of the Lesson 15-18 handouts by loading
`../handouts/figures/reactor_schematics.tex` (found through `TEXINPUTS`), so a
change to those sketches changes the guide as well.

This folder contains reading guides for Chapters 6 and 7, with illustrative examples of each new principle, which can include a physical quantity defined in words or by equation, a modeled system via a set of equations representing specific cases of the reading material, and similar exercises that, in isolation, are short but that, if chained together, can recreate more traditional homework problems in terms of extent and depth.

Archival LaTeX source for the book can be found under ~/Classes/books/books/lewis_fundamentals_of_nuclear_reactor_physics.

This reading guide should define key terms.  

Examples should require a minimum of in-place cognitive load (i.e., we may take subsequent results as inputs, perhaps modified, to show illustrative steps of families of problems rather than of a specific exemplar).

After major subsections, short multiple choice "quizzes" can be proposed, perhaps with answers in the footnote, upside down.  

Personally, I would restructure Ch 6 and 7.  I would build on a detailed accounting of neutron balance across phase space that yields a continuity equation, inserting illustrations and vector-field examples exercises along the way to illustrate net flows through surfaces of arbitrary outward normal. 

We should also infer the learning objectives implied by these chapters and compare with the ne630 LO's already documented.  When new LOs are found, we should flag them for possible inclusion.  

Finally, this reading guide should actually probably be formatted as a programmed guide, meaning a left panel has content while the right panel contains answers and programmed commentary that can be covered by a second sheet.

Please, help me help my students wrestle with this last third of the course.

