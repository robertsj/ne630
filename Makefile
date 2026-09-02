# Sphinx site for public NE 630 course materials.

SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR   := site
BUILDDIR    := _build
DOCTREEDIR  := $(BUILDDIR)/doctrees
PYTHON      ?= python3

.PHONY: help html sync-handouts check-handouts check clean

help:
	@$(SPHINXBUILD) --help

sync-handouts:
	$(PYTHON) site/scripts/export_handouts.py

check-handouts:
	$(PYTHON) site/scripts/export_handouts.py --check

html: sync-handouts
	$(SPHINXBUILD) -d "$(DOCTREEDIR)" -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

check:
	$(PYTHON) site/scripts/export_handouts.py
	$(PYTHON) site/scripts/export_handouts.py --check
	$(PYTHON) site/scripts/check_handout_builds.py
	$(SPHINXBUILD) -W -d "$(DOCTREEDIR)" -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)
	$(PYTHON) site/scripts/check_site.py "$(BUILDDIR)/html"

clean:
	rm -rf -- "$(BUILDDIR)"
