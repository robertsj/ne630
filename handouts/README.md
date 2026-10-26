# NE 630 handouts

All 38 handouts (Lessons 01–10 and 12–39) use
[`ne630handout.cls`](ne630handout.cls) directly. There is no Lesson 11 source.
The Lesson 07 derivation supplement and handout template use the same class.
The class owns fonts, page geometry, headers, colors, boxes, columns, listings,
and common authoring commands. The former board class and Chapter 4 common
preamble have been removed.

Existing instructional bodies, equations, figures, blanks, and solution reveals
are retained. Lessons 25–35 retain every substantive frame from their Beamer
slides, with title/objective frames promoted to metadata. Lessons 36–39 use
existing notebook content, including Python listings, embedded images, and
stored results. These seeded drafts have no two-page limit. Their bodies use the
shared two-column `handoutflow` layout beneath full-width lesson metadata.

## Build

Run from this directory with XeLaTeX and `latexmk` installed:

```bash
make L25                         # one lesson
make lesson25                    # equivalent alias
make all                         # every lesson and derivation supplement
make template
make check-content               # existing lessons/supplement versus Git HEAD
make check-class                 # isolated compilation/variant checks
make check-seeds                 # slide/notebook provenance and payload preservation
```

The Makefile discovers `lesson_??_handout.tex`, so adding a lesson does not
require another lesson-target definition. It automatically regenerates the
draft figures under `figures/drafts/` using the local
`figures/build_draft_figures.py` generator. Set `PLOT_PYTHON` to an
interpreter with NumPy, SciPy, and Matplotlib; for this workspace:

```bash
make L25 PLOT_PYTHON=/home/robertsj/miniforge3/bin/python
```

`python3 check_seeded_handouts.py` runs the seed check directly. It compares
ordered display/inline mathematics, tags, complete tables, code, and figure
targets within each frame/section, and verifies manifest hashes and metadata.
It does not validate inherited physics, prose exhaustively, plot data, or PDF
appearance; those require separate review.

`PYTHON` controls the check scripts. `OPENMC_PYTHON` is used only by the explicit
`make xe135-figure` regeneration target; ordinary PDF builds use the supplied
Xe-135 capture figure. No shell escape is required.

`make tidy` removes LaTeX intermediates; `make clean` also removes compiled
handout PDFs. Lesson PDFs are generated review/publication artifacts. Building
or editing sources does not publish the course site.

## Files and authoring

- [`ne630handout.cls`](ne630handout.cls): the single formatting backend.
- [`handout_template.tex`](handout_template.tex): a board-handout starting point.
- `lesson_NN_handout.tex`: public lesson wrapper or self-contained lesson.
- `lesson_NN_handout_body.tex`: retained early-lesson instructional bodies.
- [`figures/reactor_schematics.tex`](figures/reactor_schematics.tex): Chapter 4
  instructional diagrams, explicitly loaded by Lessons 15–18 rather than by
  the class.
- [`seeded_lessons.json`](seeded_lessons.json): source hashes, selected notebook
  cells, extracted-image provenance, coverage gaps, and review notes for L25–39.

Use the default flowing layout, `[board]`, or `[compact]` to match the lesson's
purpose. `[fallbackfonts]` forces the portable TeX Gyre Heros text font; otherwise
Myriad Pro is selected when locally available. Equations use Libertinus Math.
No proprietary fonts are distributed. `handoutflow` automatically flows and
balances draft text across two columns; `handoutsmall` handles occasional wide
tables/equations without changing their content. `\HandoutTypography{size}{leading}{skip}`
provides a shared interface for measured lesson-specific typography.

The [backend guide](handout_backend.md) documents the authoring commands,
solution switches, and validation scope. The [figure guide](figures/README.md)
records existing figure provenance and regeneration details.

## Source review notes

The slide files for Lectures 36–39 duplicate Lecture 31. Their handouts now use:

| Lesson | Topic | Notebook source |
| --- | --- | --- |
| 36 | Two-group diffusion and criticality | `lesson_35.ipynb`, cells 5–7; `L39_f24.ipynb`, cells 1–7 |
| 37 | The reflected reactor | Complete `lesson_37.ipynb` |
| 38 | Modeling reactor control | Complete `lesson_38.ipynb` |
| 39 | Numerical diffusion and transport | Complete `lesson_39.ipynb` |

Cell indices are zero-based. L36 has no corresponding notebook: selected cells
cover the equations, migration area, and modified one-group approximation, but
do not supply a worked bare two-group criticality calculation or numerical
solver. Readings and objectives for L36–38 come from their existing lesson pages.
The canonical L39 notebook identifies itself as Lessons 39 and 40 together;
`L39_f24.ipynb` instead covers a historical reactor-control lesson.

Notebook text and symbolic outputs retain their original content. Numerical
plots are regenerated in course purple/orange from locally recovered data. L39
transport data were recovered using the available external `detran` installation;
ordinary builds use the saved data without requiring that solver. Two historical
two-group illustrations are traced from the original curves, with their pixel
precision recorded. Original images remain provenance evidence in `figures/`.
Equation/code disagreements, stale numerical examples, and other inherited
issues are recorded by source cell in the manifest. The backend guide summarizes
the principal review items.

Several source inconsistencies remain for instructional review: L29's feedback
sign, L30's ODE algebra, L33's printed
flux/partial-current relation; L34's boundary/continuity notation and case labels;
and L35's eigenproblem coefficient and critical-width expression. L35's title
also promises cylindrical material while the stored deck returns to transport
review after its slab examples. These have been preserved rather than silently
corrected. See the backend guide and manifest for specifics.
