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
- [HW20.md](markdown/HW20.md)
- [HW21.md](markdown/HW21.md)
- [HW22.md](markdown/HW22.md)
- [HW23.md](markdown/HW23.md)
- [HW25.md](markdown/HW25.md)
- [HW26.md](markdown/HW26.md)

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
- [HW20.html](html/HW20.html)
- [HW21.html](html/HW21.html)
- [HW22.html](html/HW22.html)
- [HW23.html](html/HW23.html)
- [HW25.html](html/HW25.html)
- [HW26.html](html/HW26.html)

The Canvas fragments use semantic HTML without document wrappers, scripts, or
styles. They are generated through `../build/convert_to_canvas.py`, which uses
Pandoc and stores each equation in Canvas's `equation_image` format.

Regenerate the combined page and the Homework 01–06 fragments with:

    python3 build.py

For later homework, run the converter from `../build` (substitute the desired
homework number):

    cd ../build
    python3 convert_to_canvas.py ../homework/markdown/HW20.md ../homework/html/HW20.html
    python3 convert_to_canvas.py ../homework/markdown/HW21.md ../homework/html/HW21.html
    python3 convert_to_canvas.py ../homework/markdown/HW22.md ../homework/html/HW22.html
    python3 convert_to_canvas.py ../homework/markdown/HW23.md ../homework/html/HW23.html
    python3 convert_to_canvas.py ../homework/markdown/HW25.md ../homework/html/HW25.html
    python3 convert_to_canvas.py ../homework/markdown/HW26.md ../homework/html/HW26.html
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
Homeworks 20 and 21; there is no Homework 19 source in `ne630_problems`.
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
