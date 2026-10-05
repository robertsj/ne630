.DEFAULT_GOAL := all
.DELETE_ON_ERROR:

# Keep machine-specific interpreter and nuclear-data paths out of version
# control.  Copy config.mk.example to config.mk and edit it once per machine.
LOCAL_CONFIG ?= config.mk
-include $(LOCAL_CONFIG)

PYTHON ?= python3
OPENMC_PYTHON ?= $(PYTHON)
LATEXMK ?= latexmk
XELATEX ?= xelatex

OUTPUT_DIR := generated
BUILD_DIR := .build
STATIC_DIR := static

CARTOON_OUTPUTS := \
	$(foreach cut,0p00 0p25 0p50 0p75 1p00,\
		$(OUTPUT_DIR)/cross_section_cartoon_2D_x$(cut).pdf \
		$(OUTPUT_DIR)/cross_section_cartoon_3D_x$(cut).pdf)

RECOVERABLE_OUTPUTS := \
	$(OUTPUT_DIR)/realistic_rho.pdf \
	$(OUTPUT_DIR)/subcrit_mult.pgf \
	$(OUTPUT_DIR)/example_kinetics.pgf \
	$(OUTPUT_DIR)/traces.pgf \
	$(OUTPUT_DIR)/slab_bc.pgf \
	$(OUTPUT_DIR)/multiplying_slab.pgf \
	$(OUTPUT_DIR)/Xe_transient.pdf \
	$(OUTPUT_DIR)/xe135_comparison.pdf \
	$(OUTPUT_DIR)/prompt_drop_illustration.png \
	$(OUTPUT_DIR)/prompt_drop_illustration.pgf

LEGACY_RECONSTRUCTIONS := \
	$(OUTPUT_DIR)/accuracy_vs_precision.pgf \
	$(OUTPUT_DIR)/thermal_scattering_hydrogen.pdf

RESONANCE_OUTPUTS := \
	$(OUTPUT_DIR)/sde_NR.pdf \
	$(OUTPUT_DIR)/sde_WR.pdf

OPENMC_DATA_OUTPUTS := \
	$(OUTPUT_DIR)/h1_xsec.pgf \
	$(OUTPUT_DIR)/u235_fission.pgf \
	$(OUTPUT_DIR)/U238_inelastic.pgf \
	$(OUTPUT_DIR)/eta_nat_20.pgf

OPENMC_TRANSPORT_OUTPUT := $(OUTPUT_DIR)/mc_vs_nr_u238_h1.pdf
OPENMC_OUTPUTS := $(OPENMC_DATA_OUTPUTS) $(OPENMC_TRANSPORT_OUTPUT)
OPENMC_LIBRARY_STAMP := $(OUTPUT_DIR)/.openmc-library.stamp

STATIC_ASSETS := \
	$(STATIC_DIR)/bea.pgf \
	$(STATIC_DIR)/depletion_chain.pdf

EXTRA_OUTPUTS := \
	$(OUTPUT_DIR)/cross_section_cartoon.pdf \
	$(OUTPUT_DIR)/elastic_scattering_diagram.pdf \
	$(OUTPUT_DIR)/slowing_down_with_resonances.pdf

CORE_OUTPUTS := $(CARTOON_OUTPUTS) $(RECOVERABLE_OUTPUTS) \
	$(LEGACY_RECONSTRUCTIONS) $(RESONANCE_OUTPUTS)
ALL_OUTPUTS := $(CORE_OUTPUTS) $(OPENMC_OUTPUTS)

RECOVERABLE_INPUTS := \
	../../notebooks/lesson_22.ipynb \
	../../notebooks/lesson_24.ipynb \
	../../notebooks/lesson_26.ipynb \
	../../notebooks/lesson_27.ipynb \
	../../notebooks/lesson_28.ipynb \
	../../notebooks/Lesson_33_and_34_examples.ipynb

LEGACY_ROOT_OUTPUTS := $(notdir $(ALL_OUTPUTS) $(EXTRA_OUTPUTS)) \
	bea.pgf depletion_chain.pdf
LEGACY_TEX_INTERMEDIATES := $(wildcard *.aux *.bbl *.bcf *.blg \
	*.fdb_latexmk *.fls *.log *.out *.run.xml *.synctex.gz *.xdv)

.PHONY: all core openmc extras static-check check check-tools \
	check-core-tools check-openmc-tools rebuild tidy clean distclean \
	FORCE_OPENMC_LIBRARY

# Run the complete preflight before starting either build class.  The recursive
# make retains jobserver parallelism while ensuring a bad environment cannot
# leave behind a confusing partial build.
all: check-tools
	+$(MAKE) core openmc

core: check-core-tools static-check $(CORE_OUTPUTS)

openmc: check-openmc-tools $(OPENMC_OUTPUTS)

extras: $(EXTRA_OUTPUTS)

static-check:
	@for asset in $(STATIC_ASSETS); do \
		test -s "$$asset" || { echo "missing static figure: $$asset" >&2; exit 1; }; \
	done

check-tools: check-core-tools check-openmc-tools

check-core-tools:
	@command -v "$(firstword $(LATEXMK))" >/dev/null || { \
		echo "missing LaTeX tool: $(firstword $(LATEXMK))" >&2; exit 1; \
	}
	@command -v "$(firstword $(XELATEX))" >/dev/null || { \
		echo "missing LaTeX tool: $(firstword $(XELATEX))" >&2; exit 1; \
	}
	@$(PYTHON) -c 'import matplotlib, numpy, PIL, scipy' >/dev/null 2>&1 || { \
		echo "core figure dependencies are unavailable via: $(PYTHON)" >&2; \
		echo "copy config.mk.example to config.mk and set PYTHON" >&2; \
		exit 1; \
	}

check-openmc-tools:
	@$(OPENMC_PYTHON) -c 'import shutil; import matplotlib, numpy, openmc, scipy; assert shutil.which("openmc")' >/dev/null 2>&1 || { \
		echo "OpenMC and its executable are unavailable via: $(OPENMC_PYTHON)" >&2; \
		echo "copy config.mk.example to config.mk and set OPENMC_PYTHON" >&2; \
		exit 1; \
	}
	@cross_sections="$(OPENMC_CROSS_SECTIONS)"; \
	if test -n "$$cross_sections"; then \
		test -r "$$cross_sections" || { \
			echo "cannot read OPENMC_CROSS_SECTIONS: $$cross_sections" >&2; exit 1; \
		}; \
	else \
		$(OPENMC_PYTHON) -c 'import os, pathlib; p = os.environ.get("OPENMC_CROSS_SECTIONS"); assert p and pathlib.Path(p).is_file()' >/dev/null 2>&1 || { \
			echo "OPENMC_CROSS_SECTIONS is not configured" >&2; \
			echo "copy config.mk.example to config.mk and set its library path" >&2; \
			exit 1; \
		}; \
	fi

check: all
	@set -eu; \
	status=0; \
	for asset in $$(grep -hEo 'figures/(generated|static)/[A-Za-z0-9_.-]+\.(pdf|pgf|png)' ../*.tex | sort -u); do \
		if ! test -s "../$$asset"; then \
			echo "missing referenced figure: $$asset" >&2; \
			status=1; \
		fi; \
	done; \
	exit $$status

$(OUTPUT_DIR) $(BUILD_DIR):
	@mkdir -p "$@"

$(CARTOON_OUTPUTS) &: drive_cross_section_cartoon.py \
		cross_section_cartoon_2D.tex cross_section_cartoon_3D.tex \
		cross_section_cartoon_shared_template.tex | $(OUTPUT_DIR) $(BUILD_DIR)
	$(PYTHON) drive_cross_section_cartoon.py \
		--output-dir "$(OUTPUT_DIR)" \
		--build-dir "$(BUILD_DIR)/cross_section_cartoon"

$(RECOVERABLE_OUTPUTS) &: build_recoverable_figures.py $(RECOVERABLE_INPUTS) \
		| $(OUTPUT_DIR)
	$(PYTHON) build_recoverable_figures.py --output-dir "$(OUTPUT_DIR)" --group all

$(LEGACY_RECONSTRUCTIONS) &: generate_legacy_figures.py \
		../lecture_01.tex ../lecture_11.tex | $(OUTPUT_DIR)
	$(PYTHON) generate_legacy_figures.py --output-dir "$(OUTPUT_DIR)"

$(OUTPUT_DIR)/sde_NR.pdf: slowing_down_with_resonances.tex | $(OUTPUT_DIR) $(BUILD_DIR)
	@mkdir -p "$(BUILD_DIR)/resonance"
	$(XELATEX) -interaction=nonstopmode -halt-on-error \
		-output-directory="$(BUILD_DIR)/resonance" -jobname=sde_NR \
		'\def\ResonanceVariant{NR}\input{$(abspath $<)}'
	cp "$(BUILD_DIR)/resonance/sde_NR.pdf" "$@"

$(OUTPUT_DIR)/sde_WR.pdf: slowing_down_with_resonances.tex | $(OUTPUT_DIR) $(BUILD_DIR)
	@mkdir -p "$(BUILD_DIR)/resonance"
	$(XELATEX) -interaction=nonstopmode -halt-on-error \
		-output-directory="$(BUILD_DIR)/resonance" -jobname=sde_WR \
		'\def\ResonanceVariant{WR}\input{$(abspath $<)}'
	cp "$(BUILD_DIR)/resonance/sde_WR.pdf" "$@"

# OpenMC and its evaluated-data library are deliberately separate from the
# lightweight plotting environment. Override OPENMC_PYTHON when needed, e.g.
# `make openmc OPENMC_PYTHON="conda run -n openmc python"`.
$(OPENMC_LIBRARY_STAMP): FORCE_OPENMC_LIBRARY | $(OUTPUT_DIR)
	@set -eu; \
		tmp="$@.tmp"; \
		trap 'rm -f -- "$$tmp"' EXIT HUP INT TERM; \
		cross_sections="$(OPENMC_CROSS_SECTIONS)"; \
		if test -n "$$cross_sections"; then \
			$(PYTHON) -c 'from pathlib import Path; import hashlib, sys; p = Path(sys.argv[1]).expanduser().resolve(strict=True); s = p.stat(); print(p); print(s.st_mtime_ns); print(hashlib.sha256(p.read_bytes()).hexdigest())' "$$cross_sections" > "$$tmp"; \
		else \
			printf '%s\n' '<OPENMC_CROSS_SECTIONS inherited at runtime>' > "$$tmp"; \
		fi; \
		if ! test -r "$@" || ! cmp -s "$$tmp" "$@"; then \
			mv -f -- "$$tmp" "$@"; \
		fi

FORCE_OPENMC_LIBRARY:

$(OPENMC_DATA_OUTPUTS) &: generate_openmc_figures.py $(OPENMC_LIBRARY_STAMP) \
		| $(OUTPUT_DIR) $(BUILD_DIR)
	$(OPENMC_PYTHON) generate_openmc_figures.py \
		--output-dir "$(OUTPUT_DIR)" \
		--work-dir "$(BUILD_DIR)/openmc" \
		--target h1_xsec \
		--target u235_fission \
		--target U238_inelastic \
		--target eta_nat_20 \
		$(if $(OPENMC_CROSS_SECTIONS),--cross-sections "$(OPENMC_CROSS_SECTIONS)",)

$(OPENMC_TRANSPORT_OUTPUT): generate_openmc_figures.py $(OPENMC_LIBRARY_STAMP) \
		| $(OUTPUT_DIR) $(BUILD_DIR)
	$(OPENMC_PYTHON) generate_openmc_figures.py \
		--output-dir "$(OUTPUT_DIR)" \
		--work-dir "$(BUILD_DIR)/openmc" \
		--target mc_vs_nr_u238_h1 \
		$(if $(OPENMC_CROSS_SECTIONS),--cross-sections "$(OPENMC_CROSS_SECTIONS)",)

$(OUTPUT_DIR)/%.pdf: %.tex | $(OUTPUT_DIR) $(BUILD_DIR)
	@mkdir -p "$(BUILD_DIR)/extras"
	$(LATEXMK) -xelatex -interaction=nonstopmode -halt-on-error \
		-outdir="$(BUILD_DIR)/extras" "$<"
	cp "$(BUILD_DIR)/extras/$*.pdf" "$@"

rebuild:
	+$(MAKE) check-tools
	+$(MAKE) clean
	+$(MAKE) all

# Keep rendered figures, but remove all temporary TeX/Python/OpenMC products.
tidy:
	@rm -rf -- "$(BUILD_DIR)" __pycache__
	@rm -f -- $(LEGACY_TEX_INTERMEDIATES)

# Every path below is generated and recoverable from tracked sources/assets.
clean: tidy
	@rm -rf -- "$(OUTPUT_DIR)"

# Also remove products left by the former in-place figure build.
distclean: clean
	@rm -f -- $(LEGACY_ROOT_OUTPUTS)
