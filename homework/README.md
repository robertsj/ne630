# NE 630 homework

This directory contains problem statements only:

- [HW01.md](markdown/HW01.md)
- [HW02.md](markdown/HW02.md)
- [HW03.md](markdown/HW03.md)

The combined [HW01-03.html](html/HW01-03.html) page presents each homework and
each problem as a nested, collapsible section. All sections are closed when the
page first loads.

The following files are HTML fragments ready to paste into the corresponding
Canvas assignment's Rich Content Editor in HTML view:

- [HW01.html](html/HW01.html)
- [HW02.html](html/HW02.html)
- [HW03.html](html/HW03.html)

The Canvas fragments use semantic HTML without document wrappers, scripts, or
styles. They are generated through `../build/convert_to_canvas.py`, which uses
Pandoc and stores each equation in Canvas's `equation_image` format.

Regenerate the HTML after editing a Markdown file with:

    python3 build.py

The builder requires Pandoc and the installed markdown-it-py package. The
combined page loads MathJax from its versioned CDN URL; the separate Canvas
fragments use Canvas equation images.
