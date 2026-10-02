# NE 630 — Exam 1 reference handout

A two-page, US-letter reference for Lessons 1–14, prepared from the supplied
`maters.zip` course archive. The compiled PDF is ready for front/back printing
at actual size (100%). It has no fill-in spaces or hidden solutions.

## Files

- `exam_01_reference.pdf`: the verified two-page handout.
- `exam_01_reference.tex`: main compilation wrapper.
- `exam_01_reference_body.tex`: editable content, following the existing shared-body convention.
- `ne630boardhandout.cls`: the supplied handout class, with an additional portable font fallback.
- `coverage_notes.md`: instructor-only assessment alignment and editorial assumptions; not part of the student handout.
- `Makefile`: build and cleanup commands.

## Build

Run LuaLaTeX twice, from this directory:

```sh
lualatex -interaction=nonstopmode -halt-on-error exam_01_reference.tex
lualatex -interaction=nonstopmode -halt-on-error exam_01_reference.tex
```

Alternatively, run `make`. XeLaTeX is also supported by the class.
Do not compile the body file directly.

The original Myriad Pro font search paths remain intact. If Myriad is absent,
the class tries TeX Gyre Heros and then Nimbus Sans. The supplied PDF was
compiled with Nimbus Sans and Libertinus Math. No font files are included.
A different local font may change line breaks; check the page count after editing
or recompiling with a different font. The supplied PDF has been visually checked
on both pages and contains no overfull boxes or unresolved references.

The body uses 8.6-point text with 9.6-point leading, the original letter-page
margins, two columns, and the supplied purple reference-box/heading conventions.
The data tables are slightly smaller. All content is supplied reference material;
the student/instructor solution toggle does not alter the sheet.

## Numerical checks

Independent numerical checks were made for Watt-spectrum normalization,
Maxwellian density/flux normalization and moments, elastic-collision mean
logarithmic energy loss and mean lab cosine, the two-group eigenvalue and
fixed-source formulas, global neutron balance, scattering-transfer conservation
including a lower energy cutoff, and the decay-chain integrating-factor formula.

The PDF is a draft for instructor approval. Problem-specific inputs not reproduced
here—such as an exam mixture's density or its multigroup coefficient table—should
be supplied with the corresponding examination problem.
