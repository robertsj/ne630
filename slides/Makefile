.DEFAULT_GOAL := all
.DELETE_ON_ERROR:

LATEXMK ?= latexmk
LATEXMK_FLAGS := -xelatex -shell-escape -interaction=nonstopmode \
	-halt-on-error -file-line-error -outdir=.build \
	-usepretex='\PassOptionsToPackage{outputdir=.build}{minted}'

BUILD_DIR := .build
FIGURE_DIR := figures
GIT_SHA := $(BUILD_DIR)/git_sha.txt

# lecture_21.tex is intentionally empty and is not a build target yet.
SLIDE_SOURCES := $(filter-out lecture_21.tex,$(wildcard lecture_*.tex appendix_*.tex))
SLIDE_TARGETS := $(basename $(notdir $(SLIDE_SOURCES)))
PDF_FILES := $(addprefix $(BUILD_DIR)/,$(addsuffix .pdf,$(SLIDE_TARGETS)))
OPENMC_SLIDE_TARGETS := lecture_06 lecture_07 lecture_09 lecture_11
OPENMC_PDF_FILES := $(addprefix $(BUILD_DIR)/,$(addsuffix .pdf,$(OPENMC_SLIDE_TARGETS)))
CORE_PDF_FILES := $(filter-out $(OPENMC_PDF_FILES),$(PDF_FILES))

# Explicit dependencies make common presentation changes visible to make.
# latexmk's dependency database handles inputs specific to an individual deck.
COMMON_INPUTS := term.txt $(wildcard *.sty *.bib)

# These cover artifacts from the former in-place build as well as an interrupted
# build that writes a temporary file before latexmk moves it into BUILD_DIR.
TEMP_EXTENSIONS := aux bbl bcf blg fdb_latexmk fls log nav out pyg pygtex \
	run.xml snm synctex.gz toc vrb w18 xdv
LEGACY_TEMP_FILES := $(foreach ext,$(TEMP_EXTENSIONS),$(wildcard *.$(ext)))
LEGACY_PDF_FILES := $(SLIDE_TARGETS:%=%.pdf)
LEGACY_GIT_SHA := git_sha.txt

.PHONY: all figures figures-core check figures-check tidy clean distclean FORCE \
	$(SLIDE_TARGETS)

all: $(PDF_FILES)

# Recursive make is intentional: the figure Makefile owns its generated files.
# Most individual decks avoid the slower OpenMC build; only the four decks that
# consume evaluated-data figures require the complete figure set.
figures-core:
	+$(MAKE) -C $(FIGURE_DIR) static-check core

figures: figures-core
	+$(MAKE) -C $(FIGURE_DIR) openmc

figures-check: figures
	+$(MAKE) -C $(FIGURE_DIR) check

check: all figures-check

# Convenience targets: `make lecture_04` and `make appendix_Z`.
$(SLIDE_TARGETS): %: $(BUILD_DIR)/%.pdf

# These phony gates intentionally cause latexmk to inspect its dependency
# database on every requested deck build.  That lets latexmk notice when a
# nested figure build changed one of the inputs actually used by the deck,
# while a non-OpenMC lecture still avoids the transport solve.
$(CORE_PDF_FILES): figures-core
$(OPENMC_PDF_FILES): figures

$(BUILD_DIR)/%.pdf: %.tex $(COMMON_INPUTS) $(GIT_SHA) | $(BUILD_DIR)
	@echo "Building $< -> $@"
	@TEXINPUTS="$(abspath $(BUILD_DIR)):$${TEXINPUTS:-}:" \
		$(LATEXMK) $(LATEXMK_FLAGS) "$<"

$(BUILD_DIR):
	@mkdir -p "$@"

# Always compare against HEAD, but only change the file's timestamp when the
# abbreviated commit ID changes. The temporary file keeps this update atomic.
$(GIT_SHA): FORCE | $(BUILD_DIR)
	@set -eu; \
		tmp="$@.tmp"; \
		trap 'rm -f -- "$$tmp"' EXIT HUP INT TERM; \
		git rev-parse --short=6 HEAD > "$$tmp"; \
		if ! test -r "$@" || ! cmp -s "$$tmp" "$@"; then \
			mv -f -- "$$tmp" "$@"; \
		fi

FORCE:

# Keep PDFs and the generated SHA, but remove TeX intermediates.  The extension
# list includes Beamer's fragile-frame files and Minted's transient inputs.
tidy:
	+$(MAKE) -C $(FIGURE_DIR) tidy
	@if test -d "$(BUILD_DIR)"; then \
		$(LATEXMK) -c -outdir="$(BUILD_DIR)" $(SLIDE_SOURCES); \
	fi
	@for ext in $(TEMP_EXTENSIONS); do \
		rm -f -- "$(BUILD_DIR)"/*."$$ext"; \
	done
	@rm -f -- $(LEGACY_TEMP_FILES)
	@rm -rf -- ./_minted-* "$(BUILD_DIR)"/_minted-*

# Remove declared slide products while leaving BUILD_DIR available for the next
# build. Figure cleanup remains scoped by figures/Makefile.
clean:
	+$(MAKE) -C $(FIGURE_DIR) clean
	@if test -d "$(BUILD_DIR)"; then \
		$(LATEXMK) -C -outdir="$(BUILD_DIR)" $(SLIDE_SOURCES); \
	fi
	@for ext in $(TEMP_EXTENSIONS); do \
		rm -f -- "$(BUILD_DIR)"/*."$$ext"; \
	done
	@rm -f -- $(PDF_FILES) $(GIT_SHA) $(LEGACY_PDF_FILES) $(LEGACY_GIT_SHA) \
		$(LEGACY_TEMP_FILES)
	@rm -rf -- ./_minted-* "$(BUILD_DIR)"/_minted-*

# BUILD_DIR is wholly generated, so distclean may safely remove it as a unit.
distclean:
	+$(MAKE) -C $(FIGURE_DIR) distclean
	@rm -rf -- "$(BUILD_DIR)" ./_minted-*
	@rm -f -- $(LEGACY_PDF_FILES) $(LEGACY_GIT_SHA) $(LEGACY_TEMP_FILES)
