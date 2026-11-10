# NE 630 public course site

This directory is the Sphinx source for the public NE 630 course-materials
site. The public page links student handouts for Lessons 1--10 and 12--31,
standalone notebooks for Lessons 8--12, 15--19, and 22--26, and available lesson videos.

## Build

Install the site dependency in your preferred Python environment:

```bash
python -m pip install -r site/requirements.txt
```

Then build from the repository root:

```bash
make html
```

The rendered site is written to `_build/html/`. Run the stricter release check
before publication:

```bash
make check
```

That check refreshes the public exports, compiles every downloadable source
bundle, compares its rendered pages with the published PDF, treats Sphinx
warnings as errors, and checks all local site links. It requires `latexmk`,
XeLaTeX, and Poppler's `pdftoppm` in addition to Sphinx. A stale or incorrect
PDF therefore fails the check instead of being silently published.

The configuration includes `sphinx.ext.githubpages`, so the rendered output
contains the `.nojekyll` file needed for a branch-based GitHub Pages site.

## Handout publication model

Canonical handouts remain in `handouts/`. Running `make html` first invokes
the handout Makefile and then `site/scripts/export_handouts.py`, which creates
the public files beneath `site/_static/handouts/`.

The canonical Lesson 1--10 and 12--14 wrappers, bodies, class, and referenced
supporting files are version-controlled. All handouts use `ne630handout.cls`.
Lessons 15--39 are exported as PDFs only. Lessons 27--28 use revised two-page
handouts. Lesson 29 is the revised two-page feedback handout.
Lessons 30--31 are published slide-derived handouts; Lessons 32--39 remain unpublished seeds; L30--35 contain the
corresponding Beamer slide content, and L36--39 use
existing notebooks (see `handouts/README.md` for selections and coverage gaps). Rendered handout PDFs
and the entire `site/_static/handouts/` export tree
are ignored build artifacts on the source branch; they are generated during
`make html` or `make check` and published in the rendered site on `gh-pages`.

Canonical kinetics notebooks (Lessons 27–28) and their module live in code/.
The existing depletion notebooks remain in notebooks/ in this release.
Download copies use site/_static/notebooks/ and retain their stable URLs.
The Lesson 28 kinetics module is newly downloadable; its notebooks are not.
make sync-code refreshes the module and existing depletion exports, and
make check-code verifies byte identity. This does not deploy the site.

Verify the publication copies with:

```bash
cmp notebooks/lesson_8.ipynb site/_static/notebooks/lesson_8.ipynb
cmp notebooks/lesson_09.ipynb site/_static/notebooks/lesson_9.ipynb
cmp notebooks/lesson_10.ipynb site/_static/notebooks/lesson_10.ipynb
cmp notebooks/lesson_11.ipynb site/_static/notebooks/lesson_11.ipynb
cmp notebooks/lesson_12.ipynb site/_static/notebooks/lesson_12.ipynb
cmp notebooks/lesson_15.ipynb site/_static/notebooks/lesson_15.ipynb
cmp notebooks/lesson_16.ipynb site/_static/notebooks/lesson_16.ipynb
cmp notebooks/lesson_17.ipynb site/_static/notebooks/lesson_17.ipynb
cmp notebooks/lesson_18.ipynb site/_static/notebooks/lesson_18.ipynb
cmp notebooks/lesson_19.ipynb site/_static/notebooks/lesson_19.ipynb
cmp notebooks/lesson_22.ipynb site/_static/notebooks/lesson_22.ipynb
cmp notebooks/lesson_23.ipynb site/_static/notebooks/lesson_23.ipynb
cmp notebooks/lesson_24.ipynb site/_static/notebooks/lesson_24.ipynb
cmp notebooks/lesson_25.ipynb site/_static/notebooks/lesson_25.ipynb
cmp notebooks/lesson_26.ipynb site/_static/notebooks/lesson_26.ipynb
cmp notebooks/ne630_depletion.py site/_static/notebooks/ne630_depletion.py
```

Lessons 23 and 24 require the shared `ne630_depletion.py` module, published
beside the notebook downloads. Copy it to the same local folder before running
the notebooks.

Do not edit generated handout exports directly. The build renders each public
PDF, and the exporter copies it while creating a complete source bundle from
the canonical inputs. Public handout wrappers must set
`\handoutsolutionsfalse`, so the published source reproduces the non-solution
PDF. A private solution copy can be made by changing that single line to
`\handoutsolutionstrue` before compiling.

To regenerate the ignored exports and verify that they match their canonical
inputs, run:

```bash
make check-handouts
```

The public TeX requires XeLaTeX or LuaLaTeX. Each lesson bundle contains the
wrapper with solutions disabled, the body source, shared `ne630handout.cls`,
any supporting figures or reproducibility notebooks referenced by that lesson,
and brief build instructions. No repository-local `.sty` file is currently
required.

Deployment to a `gh-pages` branch is intentionally separate from the local
build. Review `_build/html/` and the Git diff before creating or updating that
branch. See [PUBLISHING.md](PUBLISHING.md) for the first-publication and update
procedures.

Lesson 28: save ne630_kinetics.py beside your notebook or script. NumPy and
SciPy are required; direct execution plots the L27 pulse using Matplotlib.

## Lesson 30–31 release (November 10, 2026)

Published the two student-facing PDFs only, preserving the existing live
source-bundle and shared-class downloads. Lesson 30 corrects missing exponential
factors and uses the particular solution exp(x)/(1+p), with the resonant
p=-1 and repeated-root p=0 cases distinguished. Lesson 31 clarifies angular
density units and the differential balance convention, and removes a stray
time argument from a steady-state source.
