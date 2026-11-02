# NE 630 homework

This directory contains problem statements only. The retained Markdown sources
are:

- [HW01.md](markdown/HW01.md)
- [HW02.md](markdown/HW02.md)
- [HW03.md](markdown/HW03.md)
- [HW04.md](markdown/HW04.md)
- [HW05.md](markdown/HW05.md)
- [HW06.md](markdown/HW06.md)
- [HW10.md](markdown/HW10.md)
- [HW11.md](markdown/HW11.md)
- [HW12.md](markdown/HW12.md)
- [HW13.md](markdown/HW13.md)
- [HW14.md](markdown/HW14.md)
- [HW15.md](markdown/HW15.md)
- [HW16.md](markdown/HW16.md)
- [HW17.md](markdown/HW17.md)
- [HW18.md](markdown/HW18.md)
- [HW19.md](markdown/HW19.md)
- [HW20.md](markdown/HW20.md)
- [HW21.md](markdown/HW21.md)
- [HW22.md](markdown/HW22.md)
- [HW23.md](markdown/HW23.md)
- [HW25.md](markdown/HW25.md)
- [HW26.md](markdown/HW26.md)
- [HW27.md](markdown/HW27.md)
- [HW28.md](markdown/HW28.md)

The combined [HW01-06.html](html/HW01-06.html) page presents each homework and
each problem as a nested, collapsible section. All sections are closed when the
page first loads.

The following files are HTML fragments ready to paste into the corresponding
Canvas assignment's Rich Content Editor in HTML view:

- [HW01.html](html/HW01.html)
- [HW02.html](html/HW02.html)
- [HW03.html](html/HW03.html)
- [HW04.html](html/HW04.html)
- [HW05.html](html/HW05.html)
- [HW06.html](html/HW06.html)
- [HW07.html](html/HW07.html)
- [HW08.html](html/HW08.html)
- [HW09.html](html/HW09.html)
- [HW10.html](html/HW10.html)
- [HW11.html](html/HW11.html)
- [HW12.html](html/HW12.html)
- [HW13.html](html/HW13.html)
- [HW14.html](html/HW14.html)
- [HW15.html](html/HW15.html)
- [HW16.html](html/HW16.html)
- [HW17.html](html/HW17.html)
- [HW18.html](html/HW18.html)
- [HW19.html](html/HW19.html)
- [HW20.html](html/HW20.html)
- [HW21.html](html/HW21.html)
- [HW22.html](html/HW22.html)
- [HW23.html](html/HW23.html)
- [HW25.html](html/HW25.html)
- [HW26.html](html/HW26.html)
- [HW27.html](html/HW27.html)
- [HW28.html](html/HW28.html)

The Canvas fragments use semantic HTML without document wrappers, scripts, or
styles. They are generated through `../build/convert_to_canvas.py`, which uses
Pandoc and stores each equation in Canvas's `equation_image` format.

Regenerate the combined page and the Homework 01–06 fragments with:

    python3 build.py

For later homework, run the converter from `../build` (substitute the desired
homework number):

    cd ../build
    python3 convert_to_canvas.py ../homework/markdown/HW19.md ../homework/html/HW19.html
    python3 convert_to_canvas.py ../homework/markdown/HW20.md ../homework/html/HW20.html
    python3 convert_to_canvas.py ../homework/markdown/HW21.md ../homework/html/HW21.html
    python3 convert_to_canvas.py ../homework/markdown/HW22.md ../homework/html/HW22.html
    python3 convert_to_canvas.py ../homework/markdown/HW23.md ../homework/html/HW23.html
    python3 convert_to_canvas.py ../homework/markdown/HW25.md ../homework/html/HW25.html
    python3 convert_to_canvas.py ../homework/markdown/HW26.md ../homework/html/HW26.html
    python3 convert_to_canvas.py ../homework/markdown/HW27.md ../homework/html/HW27.html
    python3 convert_to_canvas.py ../homework/markdown/HW28.md ../homework/html/HW28.html
    rm tmp.html

The combined-page builder requires Pandoc and the installed markdown-it-py
package; the direct converter requires Pandoc. The combined page loads MathJax
from its versioned CDN URL; the separate Canvas fragments use Canvas equation
images.

Homework 05 is adapted from
`/home/robertsj/Classes/ne630_problems/lesson_05/inclass.tex`. Print-only page
breaks, writing space, and the local blank plotting image are omitted from the
Canvas-ready version; the plotting ranges are stated in the prompt.

Homework 06 combines Problem 1 from
`/home/robertsj/Classes/ne630_problems/lesson_05/statement.tex` with Problems 1
and 2 from `/home/robertsj/Classes/ne630_problems/lesson_06/statement.tex`.
Problem 1 now uses OpenMC, Problem 2 compares an SLBW reconstruction directly
against that OpenMC result, and Problem 3 requires normalization of the given
fission spectrum before the requested probability integrals are evaluated.

Problem 1 of `ne630_problems/lesson_16/statement.tex` is assigned as Homework
15. The remaining two problems from that source form Homework 16. Source
Lessons 17 and 18 supply matching Homeworks 17 and 18. This split is recorded
in each Markdown and solution source. Source Lessons 20 and 21 supply matching
Homeworks 20 and 21. Homework 19 was entered directly in Canvas; its statement
was supplied by Jeremy on 2026-11-02 and is now retained here. It uses the
Lesson 19 SFR unit-cell notebook and targets **k-infinity = 1**, not the
notebook's illustrative finite-system target 1/0.90.
Homework 22 retains all four parts of the xenon problem from Source Lesson 22,
with the control-rod model and fixed full-power conditions made explicit for
the xenon-worth comparisons.

Homework 23 retains both problems (FNRP 10.13 and 10.14) from Source Lesson 23:
uranium/plutonium conversion and power sharing, and the thorium–protactinium–
uranium buildup chain. The draft makes the atom-fraction enrichment convention,
initial inventories, and constant-flux/cross-section assumptions explicit;
the source's worked solutions and numerical verification code are omitted.

Draft Homework 25 retains all three problems from Source Lesson 25: neutron
lifetimes, mean-speed weighting, and equilibrium multibatch burnup. Draft
Homework 26 retains the two Source Lesson 26 problems on prompt-neutron growth
and a fixed-spectrum source transient, then adds the pulsed accelerator-driven
reactor problem. Source provenance and corrected legacy units/data are recorded
in the Markdown comments. Worked solutions and verification plots are maintained
separately in the instructor-only `solutions/` directory, not these Canvas files.


## Homework 27–28 seed provenance (internal)

Local seeds retain canonical source homework numbering, not a remapping by
individual lecture topics. Source titles explicitly identify Lessons 27 and 28;
current course Lessons 27–28 cover one-group delayed-neutron kinetics and
precursor groups/inhour kinetics. HW27 has two problems (FNRP 5.2 fuel-mixture
delayed fraction and a six-group transient). HW28 has three problems: FNRP 5.9 reactor periods, a one-group step transient,
and the original asymptotic-form question (now Problem 3). No dates or point values have been added.

Read-only source root: `/home/robertsj/Classes/ne630_problems`, HEAD
`4f375f82c1626817aa78590b057e5bce2b6ef713`. Last commit touching these
lesson directories: `8293be2c7bb066b347f34036fa95e091fd4fbda3`.
Sources: `lesson_27/statement.tex`, `lesson_27/HW27_Sol.ipynb`,
`lesson_28/statement.tex`, and `lesson_28/HW28_sol.ipynb`.
The statements contain matching private solutions; notebooks corroborate
parameters and calculations. Neither student prompt needs a separate image.
The legacy HW27 solution figure `prob2.pdf` is absent from the bank and is
regenerated privately from the retained six-group data.

Limited adaptations from source:

- TeX layout becomes Markdown/Canvas equations; print-only space, solutions,
  code, and solution graphics are excluded from student files.
- HW27 Problem 2 replaces reversed verbal removal/insertion descriptions
  with positive/negative steps, preserving the actual signed reactivities.
  Both cases use unambiguous right-continuous intervals at 1 and 6 seconds
  and explicitly include the requested 10-second endpoint.
- HW28 Problem 2 restores the missing multiplier `n(t)` in the neutron
  equation, confirmed by the source solution and notebook, and displays
  implied units of lambda and Lambda. Numerical parameters and times are unchanged.
- HW28 Problem 1 has no supplied generation time. The private answer retains
  the source small-reactivity approximation, not an invented exact period.
- **Review before release:** HW28 Problem 3 retains its original mathematical
  statement, but the source supplies no solution beyond “See me in office
  hours.” Its two stated inequalities alone do not guarantee the usual
  separated-root approximation near prompt criticality; a further smallness
  condition is needed. The private manual records this limitation, retains an asymptotic
  counterexample, and adds a labeled new derivation under the needed extra
  restriction. The current student statement has not been silently changed.

Matching solutions extend the existing instructor-only manual with `hw27.tex`
and `hw28.tex`. `solutions/build_hw27_28_checks.py` regenerates only new private
assets and verification data. It does not import the course kinetics module;
the unrelated Lesson 28 `ne630_kinetics.py` API mismatch is not fixed or tested.
