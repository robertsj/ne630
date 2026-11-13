Build the guides with XeLaTeX and latexmk:

```sh
make                          # Both chapters, portrait (the default)
make landscape                # Both chapters, landscape
make both                     # Both orientations of both chapters
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

This folder contains reading guides for Chapters 6 and 7, with illustrative examples of each new principle, which can include a physical quantity defined in words or by equation, a modeled system via a set of equations representing specific cases of the reading material, and similar exercises that, in isolation, are short but that, if chained together, can recreate more traditional homework problems in terms of extent and depth.

Archival LaTeX source for the book can be found under ~/Classes/books/books/lewis_fundamentals_of_nuclear_reactor_physics.

This reading guide should define key terms.  

Examples should require a minimum of in-place cognitive load (i.e., we may take subsequent results as inputs, perhaps modified, to show illustrative steps of families of problems rather than of a specific exemplar).

After major subsections, short multiple choice "quizzes" can be proposed, perhaps with answers in the footnote, upside down.  

Personally, I would restructure Ch 6 and 7.  I would build on a detailed accounting of neutron balance across phase space that yields a continuity equation, inserting illustrations and vector-field examples exercises along the way to illustrate net flows through surfaces of arbitrary outward normal. 

We should also infer the learning objectives implied by these chapters and compare with the ne630 LO's already documented.  When new LOs are found, we should flag them for possible inclusion.  

Finally, this reading guide should actually probably be formatted as a programmed guide, meaning a left panel has content while the right panel contains answers and programmed commentary that can be covered by a second sheet.

Please, help me help my students wrestle with this last third of the course.

