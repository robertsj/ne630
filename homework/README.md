# NE 630 homework

This directory contains problem statements only:

- [HW01.md](markdown/HW01.md)
- [HW02.md](markdown/HW02.md)
- [HW03.md](markdown/HW03.md)
- [HW04.md](markdown/HW04.md)
- [HW05.md](markdown/HW05.md)
- [HW06.md](markdown/HW06.md)

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

The Canvas fragments use semantic HTML without document wrappers, scripts, or
styles. They are generated through `../build/convert_to_canvas.py`, which uses
Pandoc and stores each equation in Canvas's `equation_image` format.

Regenerate the HTML after editing a Markdown file with:

    python3 build.py

The builder requires Pandoc and the installed markdown-it-py package. The
combined page loads MathJax from its versioned CDN URL; the separate Canvas
fragments use Canvas equation images.

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
