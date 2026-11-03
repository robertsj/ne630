LATEXMK := latexmk
PYTHON ?= python3
TARGET := fall_2026_ne630_solution_manual
FLAGS := -pdf -shell-escape -interaction=nonstopmode -halt-on-error
SOURCES := $(TARGET).tex \
	hw01.tex hw02.tex hw03.tex hw04.tex hw05.tex hw06.tex hw07.tex \
	hw08.tex hw09.tex hw10.tex hw11.tex hw12.tex hw13.tex hw14.tex \
	hw15.tex hw16.tex hw17.tex hw18.tex hw19.tex hw20.tex hw21.tex \
	hw22.tex hw23.tex hw24.tex hw25.tex hw26.tex hw27.tex hw28.tex
HW18_FIGURES := figures/hw18_koo.png figures/hw18_log_four_factors.png
HW19_FIGURES := figures/hw19_enrichment.png figures/hw19_convergence.png
HW20_28_FIGURES := figures/hw21_fuel_coefficient.png figures/hw22_xenon.png figures/hw27_six_group.png
HW24_TABLES := data/hw24/startup.tex data/hw24/poisons.tex data/hw24/fits.tex data/hw24/cycles.tex \
	data/hw24/core10.tex data/hw24/errors.tex
HW24_FIGURES := figures/hw24_power_flux_burnup.png figures/hw24_startup.png \
	figures/hw24_fits.png figures/hw24_core10.png figures/hw24_cross_section_effect.png
HW26_FIGURES := figures/hw26_absorption_rate.png figures/hw26_pulse_power.png
HW27_FIGURES := figures/hw27_neutron_density.png
FIGURES := $(HW27_FIGURES) $(wildcard figures/*) $(HW18_FIGURES) $(HW19_FIGURES) $(HW20_28_FIGURES) $(HW24_FIGURES) $(HW26_FIGURES)

.PHONY: all tidy clean

all: $(TARGET).pdf

$(TARGET).pdf: $(SOURCES) $(FIGURES) $(HW24_TABLES)
	$(LATEXMK) $(FLAGS) $(TARGET).tex

$(HW18_FIGURES): build_hw18_figures.py data/hw18_p_over_d.csv
	$(PYTHON) build_hw18_figures.py

$(HW19_FIGURES) &: build_hw19_figures.py data/hw19_results.json
	$(PYTHON) build_hw19_figures.py

$(HW20_28_FIGURES) &: build_hw20_28_figures.py
	$(PYTHON) build_hw20_28_figures.py

$(HW26_FIGURES) &: build_hw25_26_figures.py
	$(PYTHON) build_hw25_26_figures.py

$(HW27_FIGURES): build_hw27_28_checks.py
	$(PYTHON) build_hw27_28_checks.py

# Standalone review copy shares the canonical HW24 section and numerical assets.
hw24_review.pdf: hw24_review.tex hw24.tex $(HW24_TABLES) $(HW24_FIGURES)
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error hw24_review.tex

$(HW24_TABLES) $(HW24_FIGURES) &: build_hw24_solution.py ../../code/ne630_depletion.py ../markdown/HW24.md
	MPLBACKEND=Agg $(PYTHON) build_hw24_solution.py

tidy:
	$(LATEXMK) -c $(TARGET).tex

clean:
	$(LATEXMK) -C $(TARGET).tex
