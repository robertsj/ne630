# Slide figure builds

Figure sources live in this directory.  Rendered outputs are written to the
ignored `generated/` directory, temporary compiler and transport files go in
the ignored `.build/` directory, and source-less assets that must remain under
version control live in `static/`.

## Targets

- `make core` builds every deterministic Python and TeX figure that does not
  require evaluated nuclear data.
- `make openmc` builds the evaluated-data plots and the Monte Carlo comparison.
- `make all` builds both sets.
- `make extras` builds the standalone TeX figures that are not used by a
  lecture.
- `make check` builds the lecture figures and verifies every referenced asset.
- `make tidy` removes intermediates while retaining rendered figures.
- `make clean` removes intermediates and `generated/`.
- `make distclean` also removes products left by the former in-place build.

The build requires Python 3.10 or newer and GNU Make 4.3 or newer (the grouped
figure rules are not supported by the older Make bundled with macOS).  The core
Python packages are listed in `requirements.txt`; XeLaTeX and `latexmk` are also
needed.

For normal use, copy the example machine configuration once and edit its three
paths.  `config.mk` is ignored by Git and is loaded automatically, so subsequent
`make`, `make rebuild`, and top-level slide builds need no command-line options:

```console
cp config.mk.example config.mk
$EDITOR config.mk
make rebuild
```

Settings may still be overridden on the command line, for example:

```console
make core PYTHON=/path/to/python
```

OpenMC figures require the OpenMC Python package and executable plus an HDF5
cross-section library.  A typical invocation is:

```console
make openmc \
  OPENMC_PYTHON="conda run -n openmc python" \
  OPENMC_CROSS_SECTIONS=/path/to/cross_sections.xml
```

`make rebuild` checks the complete toolchain before deleting existing outputs,
so a missing dependency or bad local path does not destroy a usable build.

The top-level `slides/Makefile` runs the appropriate figure target before each
lecture.  Its PDFs and all LaTeX intermediates are kept under `slides/.build/`.

The build records the resolved `cross_sections.xml` path, modification time,
and checksum; switching or updating that XML automatically invalidates the
OpenMC figures.  Evaluated HDF5 files named by the XML are normally immutable.
If those files are replaced in place without changing the XML, run `make clean`
before rebuilding.

`static/bea.pgf` and `static/depletion_chain.pdf` currently have no complete
generators.  They are explicit exceptions: cleanup rules never remove them.
