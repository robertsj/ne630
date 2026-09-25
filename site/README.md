# NE 630 public course site

This directory is the Sphinx source for the public NE 630 course-materials
site. The initial page publishes student handouts for Lessons 1--10 and 12--14,
and standalone notebooks for Lessons 8--12.

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
`site/scripts/export_handouts.py`, which creates the public files beneath
`site/_static/handouts/`.

The canonical Lesson 1--10 and 12--14 wrappers, bodies, class, student PDFs,
and referenced supporting files must be version-controlled along with the public exports;
the build intentionally stops if any required input is absent.

Standalone lesson notebooks remain canonical in `notebooks/`. Public download
copies live beneath `site/_static/notebooks/` and must be byte-for-byte
identical to their canonical files. The Lesson 8--12 notebooks are
published alongside their handouts as independent course resources. Verify their
publication copies with:

```bash
cmp notebooks/lesson_8.ipynb site/_static/notebooks/lesson_8.ipynb
cmp notebooks/lesson_09.ipynb site/_static/notebooks/lesson_9.ipynb
cmp notebooks/lesson_10.ipynb site/_static/notebooks/lesson_10.ipynb
cmp notebooks/lesson_11.ipynb site/_static/notebooks/lesson_11.ipynb
cmp notebooks/lesson_12.ipynb site/_static/notebooks/lesson_12.ipynb
```

Do not edit those generated files directly. The exporter copies each public
PDF and creates a complete source bundle from the canonical wrapper, body, and
class. The exported wrapper must set `\handoutsolutionsfalse`, so the published
source reproduces the non-solution PDF. A private solution copy can be made by
changing that single line to `\handoutsolutionstrue` before compiling.

To verify that committed exports match their canonical inputs without changing
anything, run:

```bash
make check-handouts
```

The public TeX requires XeLaTeX or LuaLaTeX. Each lesson bundle contains the
wrapper with solutions disabled, the body source, shared `ne630boardhandout.cls`,
any supporting figures or reproducibility notebooks referenced by that lesson,
and brief build instructions. No repository-local `.sty` file is currently
required.

Deployment to a `gh-pages` branch is intentionally separate from the local
build. Review `_build/html/` and the Git diff before creating or updating that
branch. See [PUBLISHING.md](PUBLISHING.md) for the first-publication and update
procedures.
