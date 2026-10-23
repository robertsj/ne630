# Shared NE 630 handout class

`ne630handout.cls` is the shared backend used by `lesson_22_handout.tex`
and `lesson_24_handout.tex`. `ne630boardhandout.cls`,
`ne630_ch04_reading_guide_common.tex`, and the other lesson sources retain
their existing backend choices; this is not a course-wide class migration.

The class is self-contained: it does not load either older backend or any
Beamer file. It builds on the course's existing LaTeX packages (`article`,
`fontspec`, `unicode-math`, `tcolorbox`, `paracol`, TikZ/PGFPlots, and
`listings`); no new service, paid dependency, or shell escape is needed.

## Authoring

```tex
\documentclass{ne630handout}
\handoutsolutionsfalse
\hypersetup{pdftitle={NE 630 -- Lesson XX: Title},pdfauthor={Jeremy Roberts}}
\begin{document}
\Lesson{XX}{Lesson title}{Assigned reading}{Guiding question}
\colstart
\Sec{1}{First topic}
Reference text, equations, tables, or a figure.
\begin{KeyBox}{A useful result}
  \Primary{Primary emphasis}; \Alert{alert emphasis}.
\end{KeyBox}
\colnext
\Sec{2}{Second topic}
\begin{checkpoint}[Predict before calculating]
  A question and \RevealBlank[1in]{a private answer}.
\end{checkpoint}
\colend
\end{document}
```

Build with `latexmk -xelatex -interaction=nonstopmode -halt-on-error file.tex`.
The class requires XeLaTeX or LuaLaTeX (the course checks use XeLaTeX).
The default body is 9.5/11.5 pt. `[compact]` selects 9/10.7 pt; a page limit
is an authoring decision, not a class constraint. The current instructor-edited
L22 uses two Letter pages; the original fuller draft used three.

Text uses locally installed Myriad Pro, matching the earlier board handouts,
with Libertinus Math and TeX Gyre Cursor for code. If Myriad is unavailable,
TeX Gyre Heros is used. `[fallbackfonts]` exercises this portable path.
No proprietary font files are distributed.

## One color vocabulary

These roles match `slides/beamercolorthemewildcat.sty` exactly:

| Name | RGB / hex | Default use |
| --- | --- | --- |
| `wcprimary` | 81, 40, 136 / `#512888` | Headings, reference boxes, primary emphasis |
| `wcalerted` | 202, 124, 27 / `#CA7C1B` | Alerts, checkpoints, contrasting terms |
| `wcexample` | 0, 134, 86 / `#008656` | Worked examples, takeaways, solution reveals |

The full `wcprimary10`--`wcprimary160` shade vocabulary is available, as are
legacy names `KSUPurple`, `KSUDeepPurple`, `KSUOrange`, `KSUTeal`, `KSUGray`,
`KSULightGray`, `ksupurple`, `purple`, `orange`, and `skyblue`.
`KSUTeal` retains its historical color; the synthesis **role** now uses the
Beamer example green. `\Primary{...}`, `\Alert{...}`, `\Example{...}`, and
`\textcolor{wcprimary}{...}` work in text or math. `\alert` is also available,
without Beamer overlay syntax.

Color may distinguish physical terms within a lesson, not just box types.
In L22, purple marks xenon and orange marks iodine/its feeding of xenon;
in the time-dependent multiplication-factor model orange marks control.
Labels and the plots' distinct line styles preserve the distinction in grayscale.

## Feature coverage from the existing handouts

| Existing use | Shared-class support |
| --- | --- |
| L01--10, L12--14: wrapper/body handouts | `\HandoutSetup`, `\MakeHandoutTitle`, `\HandoutSection` |
| Flowing two-column board layout | `handoutcolumns`, including normal `\switchcolumn` |
| Fixed data, board work, questions, synthesis | `fixedbox`, `boardbox`, `checkpoint`, `takeawaybox` |
| Blanks, ruled writing space, private results | `\Blank`, `\RevealBlank`, `\MathBlank`, `\RuledLines`, `\SolutionCue`, `\SolutionFigureContent`, `\ifhandoutsolutions` |
| Objectives and vocabulary | `targetlist`, `\TermStrip` |
| L15--22: reading-guide layout | `\Lesson`, `\Sec`, `\colstart`, `\colnext`, `\colend`, `KeyBox`, `Explore` |
| Captions, equation/source notes, continuation headings | `\figcap`, `\eqread`, `\SourceLine`, `\SourceEq`, `\HandoutContinue`; late-guide `NE*` aliases |
| Math, nuclear notation, tables | AMS/mathtools/unicode-math, `\unit`, `\uunit`, `\nucl`, `\Ktrue`, `\Kclassical`, `tabularx`, `Y`, booktabs |
| L02/L06--08 and later: drawings and plots | TikZ libraries, PGFPlots, PDF/PGF inclusion, `\mathdefault` |
| L15--18: historical reactor schematics | `\FamilyFigure`, `\PinCellsFigure`, `\CycleFigure`, `\ResonanceFigure` |
| L19/L22: Python listings | `listings`, `NEpython` and `omc` styles; inline or `\lstinputlisting` |

There is no L11 handout in the current repository: “01--22” contains 21
existing lesson sources. Lesson-specific equations and drawings remain
content, not styling. The four legacy Chapter 4 drawing helpers are retained
in the class solely for compatibility with future L15--18 migrations.

Additional boxes: `ExampleBox`, `OpenMCExplore`, and slide-like `block`,
`alertblock`, and `exampleblock`. `Explore` no longer automatically prepends
“OpenMC”; use `OpenMCExplore` or put OpenMC in the title when appropriate.
All box families share a common base style. The legacy box families accept
an additional optional tcolorbox argument after the title, for example:

```tex
\begin{KeyBox}{Long explanation}[breakable]
  ...
\end{KeyBox}
\begin{checkpoint}[Try this][breakable]
  ...
\end{checkpoint}
```

Breakable boxes belong in normal flowing text, not inside the nonbreaking
minipages created by `\colstart`. Both public and solution variants use the
same source: set `\handoutsolutionstrue` or use `[solutions]` (an explicit
`\handoutsolutionsfalse` in a wrapper overrides the class option).

## Future migrations (not applied now)

- **L01--10, L12--14:** replace the document class in a working copy; the
  body interface is available unchanged. Recheck spacing and page breaks.
- **L15--19:** replace the `\input{ne630_ch04_reading_guide_common.tex}` line
  with `\documentclass{ne630handout}`. Keep lesson-local content, figures,
  and any intentional overrides.
- **L20--21:** replace the embedded fallback and duplicated local layout
  definitions with the new class. Retain lesson-specific drawing macros
  and the document body. Do not define `NEContinue`, `NEbody`, etc. again.
- Do not redirect either old backend to this class until migration is
  explicitly requested: doing so would change all dependent handouts.

## L22 slide coverage

Source: `../slides/lecture_22.tex`. The current two-page instructor revision
retains the main slide topics. Its review is shorter than the initial draft,
and the equilibrium calculation is deliberately left as an in-class exercise.

| Slide frame | Handout location |
| --- | --- |
| Primary Objective | Page 1 objective |
| Review: Reactivity | Section 1 definitions, units, worths, and coefficients |
| Reactivity in Time | Section 2, FNRP 10.4* model with colored fuel/FP/control terms and moderator-volume control explanation |
| Fission Products | Section 3, six-entry yield table, decay-mode and yield-sum prompts |
| Evolution of Fission-Product Concentrations | Section 4, FNRP 10.7 and all-energy spectrum average |
| The Most Important Duo | Section 5, OpenMC-data capture figure and color-coded FNRP 10.12--10.13 |
| Equilibrium Xenon Worth | Section 6, zero-derivative balances, both saturation expressions, and the numerical exercise without a printed answer |
| The Xenon Transient: The Problem | Section 7, state vector, matrix, source term, and initial-value formulation |
| The Xenon Transient: The Code | Section 7, runnable script included directly, with its initial conditions and flux schedule |
| The Xenon Transient: The Result | Section 8, slide figure and shutdown interpretation |
| Beyond Xe! | Section 9, all six listed nuclides, FNRP samarium reading and IAEA chain link |

The equilibrium example and transient script retain their distinct parameter
sets; do not silently replace one with the other. The iodine balance is
FNRP 10.12 and the xenon balance is FNRP 10.13. The companion script retains
corrected xenon variable names and explicit plot colors. Samarium remains a
reading extension rather than an invented worked model. The −0.02% review
exercise and worked −2.9% equilibrium answer from the initial draft are not
part of the current instructor-edited source.

### Figures and code provenance

`figures/xe135_capture.pgf` now replaces the former notebook-image PDF.
The standalone `figures/plot_xe135_capture.py` reads OpenMC Xe135 MT=102
capture data and writes native PGFPlots output with inherited handout fonts.
See [the figure guide](figures/README.md) and `figures/xe135_capture.json` for
the regeneration command, temperature, source hashes, and measured annotation
value (2.664214 million barns at 0.0253 eV for the local ENDF/B-VIII.0 library).
The old `figures/lesson_22_xe135_comparison.pdf` is retained but unused by L22.

`figures/lesson_22_Xe_transient.pdf` remains a byte-for-byte copy of the
matching slide-generated file. It is produced by `build_xenon_transient` in
`slides/figures/build_recoverable_figures.py`, with the same corrected equations
and inputs as `lesson_22_xenon_transient.py`.

The L22 Makefile target depends on the class, both figures, and the Python
script. Building the PDF needs neither Python nor nuclear-data libraries.
Regenerating the capture PGF requires OpenMC/NumPy and the selected HDF5 data.
If the script's numerical parameters change, regenerate the transient figure
from those same parameters as part of that edit; including the script directly
prevents listing drift, not stale figures.

## Verification

```bash
make L22
python3 check_handout_class.py --keep
MPLBACKEND=Agg /home/robertsj/opt/miniforge3/bin/python lesson_22_xenon_transient.py
```

The compatibility check transforms **temporary copies** of all 21 existing
L01--L22 sources, compiles them against the new class, and also compiles
solution-enabled variants where a toggle exists plus L22's font fallback.
It reports fatal/missing-character/missing-command failures separately from
layout notices. This establishes interface coverage, not unchanged pagination
or a completed visual migration of earlier lessons. Existing handouts with
manual column breaks need their own layout pass when migrated.

For the delivered L22 PDF, additionally inspect `pdfinfo`, LaTeX layout and
reference diagnostics, and rendered images of every page. The companion
script's two plotted series have been compared numerically with the slide
figure generator, not just checked for successful execution.

### Initial class validation (2026-10-19, before later instructor edits)

- All 36 compatibility builds passed across the 21 existing lesson sources.
  Some earlier lessons emit layout notices after the temporary class swap;
  they are not visually migrated or published by this check.
- L22 public, solution, and font-fallback versions each build as three Letter
  pages without overfull/underfull boxes, missing characters, or unresolved
  references. The public PDF hides the shutdown-margin answer; the solution
  variant reveals it. All three delivered public pages were visually reviewed.
- Both companion-script curves exactly match the slide generator's arrays.
- Checksums confirm all other existing handout sources/PDFs and both older
  backends are unchanged from the task-start snapshot.
- That initial validation was local-only. Subsequent instructor revisions and
  the L22 publication supersede the initial draft's pagination and coverage.

### Current integration checks (2026-10-19)

The current canonical public L22 builds as two Letter pages without layout,
missing-character, or reference warnings. The backend is unchanged from the
initial compatibility validation. Re-run the commands above when changing
class behavior or migrating another lesson; the historical three-page
solution-reveal result is not a claim about the current edited content.
