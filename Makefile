# Sphinx site for public NE 630 course materials.

SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR   := site
BUILDDIR    := _build
DOCTREEDIR  := $(BUILDDIR)/doctrees
PYTHON      ?= python3

.PHONY: help build-handouts html sync-handouts check-handouts check clean

help:
	@$(SPHINXBUILD) --help

build-handouts:
	$(MAKE) -C handouts all

sync-handouts: build-handouts
	$(PYTHON) site/scripts/export_handouts.py

check-handouts: sync-handouts
	$(PYTHON) site/scripts/export_handouts.py --check

html: sync-handouts
	$(SPHINXBUILD) -d "$(DOCTREEDIR)" -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

check: check-handouts
	$(PYTHON) site/scripts/check_handout_builds.py
	$(SPHINXBUILD) -W -d "$(DOCTREEDIR)" -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)
	$(PYTHON) site/scripts/check_site.py "$(BUILDDIR)/html"

clean:
	$(MAKE) -C handouts clean
	rm -rf -- "$(BUILDDIR)" "$(SOURCEDIR)/_static/handouts"
