# NE 630 public course site

This directory is the Sphinx source for the public NE 630 course-materials
site. The initial page publishes student handouts for Lessons 1--6.

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

The canonical Lesson 1--6 wrappers, bodies, class, student PDFs, and referenced
supporting figures must be version-controlled along with the public exports;
the build intentionally stops if any required input is absent.

Do not edit those generated files directly. The exporter copies each student
PDF, creates a complete source bundle, and removes instructor-only reveal
values, figures, conditionals, and cue comments from the public TeX body. It
never publishes instructor wrappers or instructor PDFs. The build stops if a
required input is missing, if a lesson's audited redaction counts change, or if
the generated source still contains a known instructor-only construct. Public
body exports contain no TeX comments, so an accidental answer or teaching note
cannot leak through a comment line.

To verify that committed exports match their canonical inputs without changing
anything, run:

```bash
make check-handouts
```

The public TeX requires XeLaTeX or LuaLaTeX. Each lesson bundle contains the
student wrapper, sanitized body, shared `ne630boardhandout.cls`, any supporting
figures referenced by that lesson, and brief build instructions. No
repository-local `.sty` file is currently required.

Deployment to a `gh-pages` branch is intentionally separate from the local
build. Review `_build/html/` and the Git diff before creating or updating that
branch. See [PUBLISHING.md](PUBLISHING.md) for the first-publication and update
procedures.
