# Shared NE 630 handout class

[`ne630handout.cls`](ne630handout.cls) is the only formatting backend for all
38 lesson handouts (01–10 and 12–39). Both the former board-handout class and
the Chapter 4 common preamble have been removed. No Beamer theme is loaded.
Lesson-specific mathematics and drawings remain content: in particular,
[`figures/reactor_schematics.tex`](figures/reactor_schematics.tex) defines the
four Chapter 4 diagram helpers and is explicitly loaded by Lessons 15–18.

## Authoring

```tex
\documentclass{ne630handout}
\handoutsolutionsfalse
% Optional, before \begin{document}:
% \HandoutTypography{9.5}{11.5}{3pt}
\begin{document}
\Lesson{NN}{Lesson title}{Assigned reading}{Objective or guiding question}
\Sec{1}{First topic}
Reference text, equations, figures, and examples.
\begin{KeyBox}{A useful result}
  \Primary{Primary emphasis}; \Alert{contrasting terms}.
\end{KeyBox}
\end{document}
```

XeLaTeX or LuaLaTeX is required; the Makefile uses XeLaTeX through `latexmk`.
The class supplies AMS/mathtools/unicode-math, TikZ/PGFPlots, `tcolorbox`,
`paracol`, `listings`, `fvextra`, `siunitx`, `cancel`, and `xfrac`. No shell escape
is needed. `NEunicodecode` uses DejaVu Sans Mono for Unicode/Greek identifiers
in code, as needed by Lesson 28.

| Profile or command | Purpose |
| --- | --- |
| Default | 9.5 pt body, 11.5 pt leading, 3 pt paragraph skip |
| `[board]` | 9/11 pt, no paragraph skip, compact titles/boxes and tighter list/header spacing |
| `[compact]` | 9/10.7 pt, 2 pt paragraph skip |
| `[fallbackfonts]` | Force TeX Gyre Heros instead of locally detected Myriad Pro |
| `\HandoutTypography{size}{leading}{skip}` | Configure body typography centrally before the document begins |

Libertinus Math provides equations. Code uses TeX Gyre Cursor, with optical-size
Latin Modern Mono retained in the board profile. Layout profiles
do not impose a page limit. New Lessons 25–39 preserve their selected source
content even when that requires more than two pages.

## Shared interfaces

| Need | Interface |
| --- | --- |
| Lesson title and metadata | `\Lesson{number}{title}{reading}{focus}`; retained `\HandoutSetup` / `\MakeHandoutTitle` |
| Numbered topic | `\Sec{number}{title}` or `\HandoutSection` |
| Automatic two-column draft flow | `handoutflow` (full-width header outside the environment) |
| Occasional narrower math/table text | `handoutsmall` with optional font size |
| Flowing board columns | `handoutcolumns` and `\switchcolumn` |
| Paired, nonbreaking columns | `\colstart`, `\colnext`, `\colend` |
| Reference / board work / checks / synthesis | `fixedbox`, `boardbox`, `checkpoint`, `takeawaybox` |
| Reading-guide boxes | `KeyBox`, `Explore`, `ExampleBox`, `OpenMCExplore` |
| Slide-style boxes | `block`, `alertblock`, `exampleblock` |
| Blanks and writing space | `\Blank`, `\RevealBlank`, `\MathBlank`, `\RuledLines` |
| Objectives, vocabulary, private cues | `targetlist`, `\TermStrip`, `\SolutionCue`, `\SolutionFigureContent` |
| Continuations and source notes | `\HandoutContinue`, `\figcap`, `\eqread`, `\SourceLine`, `\SourceEq`; retained `NE*` aliases |
| Nuclear notation, units, tables | `\nucl`, `\unit`, `\uunit`, `\Ktrue`, `\Kclassical`, `tabularx`, `Y`, booktabs |
| Python listings | `NEpython` and `omc` listing styles |
| Unicode code | `NEunicodecode` verbatim environment with DejaVu Sans Mono |
| Lesson 24 steps and reveals | `\Step`, `\PageTitle`, `\Reveal`, `\RevealMath` |

Purple (`wcprimary`, `#512888`), orange (`wcalerted`, `#CA7C1B`), and green
(`wcexample`, `#008656`) match the Wildcat slide roles. `\Primary`, `\Alert`,
and `\Example` work in text or math. Historical color names remain available.
Box titles, labels, and distinct plot line styles retain meaning in grayscale.

Boxes accept an optional final `tcolorbox` argument, for example
`\begin{KeyBox}{Long result}[breakable]`. Breakable boxes belong in flowing
text, not inside the minipages created by `\colstart`.

Public wrappers select `\handoutsolutionsfalse`. A temporary private copy can
select `\handoutsolutionstrue`; the same switch controls blanks, cues, and
solution-only plot details. An explicit wrapper switch overrides `[solutions]`.
Keep private output separate from student PDFs.

## Slide seeding and review notes

[`seeded_lessons.json`](seeded_lessons.json) records the actual source hash,
title, and frame counts for slide-seeded Lessons 25–35. Title and primary-objective
frames move into metadata; every other substantive frame becomes a numbered
section. Slide equations, examples, answers, tables, and figures are retained.
Lessons 36–39 instead record notebook hashes, zero-based cell selections,
preferred stored outputs, original image hashes, and approved local plot
renderings. L37–39 retain their complete canonical notebooks; L36 selects matching cells from existing notebooks
because no lesson_36.ipynb exists. See the README for the source mapping and gaps.
Existing L01–24 instructional content is preserved during the formatting
migration. Lesson-local physics aliases and drawings remain with their content.

The stored sources require a later content review; this refactor preserves
these issues:

- L29 writes `rho = rho_0 - alpha_f T_f` but defines `d rho/d T_f = alpha_f`,
  which conflicts with the sign in the preceding expression.
- L30 gives `C_3 + p = 1`, hence `C_3 = 1 - p`, when substituting a particular
  solution `C_3 e^x`; that substitution instead gives `C_3(1+p) = 1`. Several
  neighboring homogeneous-solution terms also omit the exponential’s `e`.
- L33 prints `phi = (J+ + J-)/2` in the partial-current answer. Its boundary
  example also prints an incomplete diffusion equation and uses `b` after
  specifying a boundary at `a`; L34 repeats that example.
- L34 omits an equality sign in its reflecting boundary condition, uses
  `phi^(i+2)` in the flux-continuity equation, labels its final cases by
  `k_inf < 0` / `k_inf > 0`, and asks about `k_inf = 0` after discussing the
  transition around 1.
- L35 uses `Sigma_s` in its diffusion eigenproblem and prints a critical-width
  expression inconsistent with its stated numerical answer. Its title mentions
  cylinders and spherical elephants, but its stored content returns to neutron
  transport review after the slab-criticality examples.
- L36–39 slide files duplicate L31; those handout seeds now use notebook sources.
  L36's selected older notebook review repeats a fuel-region group label and
  has questionable reflector modal indices. The available cells omit the
  numerical two-group criticality example requested by its lesson objective.
- L37's reflector-width code omits a factor of two that appears in its displayed
  formula. That example is repeated in L38. L37's initial slab ODE also omits a
  flux factor; both the equations and code are preserved as stored.
- L38 contains reversed integration limits, a missing perturbation sign,
  stale numerical estimates, and a flux-notation disagreement with its code.
- L39 contains inherited sign, unit, and current-moment inconsistencies. Some
  stored localized-source results differ from the current code. Its historical
  homework deadline is retained as source content, not a current assignment.
  Plot data have now been recovered with the local transport solver; the
  localized-source rendering explicitly restores the source map represented in
  the stored figure. Original instructional listings remain unchanged. The manifest records cell-level
  details for each of these notebook review items.

## Build and validation

```bash
make L25 PLOT_PYTHON=/home/robertsj/miniforge3/bin/python
make all
make check-content
make check-class
make check-seeds
```

The Makefile discovers lessons automatically and supplies `LNN` / `lessonNN`
aliases. Draft figures are generated under `handouts/figures/drafts/` by the
local generator using `PLOT_PYTHON` (NumPy, SciPy, and Matplotlib). Photographs and
attributed engineering imagery retain their source colors; generated curves use
course purple/orange, related shades, and distinguishable line styles. Nuclear-data
figure regeneration remains an explicit operation; see the
[README](README.md) and [figure guide](figures/README.md).

`check-content` compares the 23 existing L01–24 lessons and the L07 derivation
supplement with Git `HEAD` by default,
including instructional body tokens, metadata, used preamble macros, solution
switches, and referenced binary figures. To audit against a preserved source
snapshot or another revision, run `check_handout_content.py --baseline DIR` or
`--ref REV`. The pre-refactor revision for this migration is
`4f9ffa8aa6449aed6c82fedf939301f472b7c7e1`. Its scope excludes newly seeded L25–39.

`check-seeds` checks slide-frame or notebook-cell coverage, source hashes,
mathematics, exact Python listings, stored outputs, and extracted notebook images.
It does not execute notebooks or certify their inherited physics. Figure hashes,
local paths, source data, generator version, and the two-column layout are checked
by `check_figure_assets.py`. Mathematical line breaks and aligned/split wrappers
may change; matrix/array/cases separators and all mathematical tokens remain
substantive in the preservation checks.

`check-class` runs isolated compilation and solution/font-fallback variants;
its report states the checked scope and layout notices. Compilation and token
preservation complement visual review: neither establishes unchanged pagination
or verifies the physics of inherited slide/notebook answers. Inspect rendered pages after
formatting edits. Build artifacts and publication remain separate from source
updates.
