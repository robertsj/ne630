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
HW26_FIGURES := figures/hw26_absorption_rate.png figures/hw26_pulse_power.png
HW20_28_FIGURES := figures/hw21_fuel_coefficient.png figures/hw22_xenon.png figures/hw27_six_group.png
FIGURES := $(wildcard figures/*) $(HW18_FIGURES) $(HW19_FIGURES) $(HW26_FIGURES) $(HW20_28_FIGURES)

.PHONY: all tidy clean

all: $(TARGET).pdf

$(TARGET).pdf: $(SOURCES) $(FIGURES)
	$(LATEXMK) $(FLAGS) $(TARGET).tex

$(HW18_FIGURES): build_hw18_figures.py data/hw18_p_over_d.csv
	$(PYTHON) build_hw18_figures.py

$(HW19_FIGURES) &: build_hw19_figures.py data/hw19_results.json
	$(PYTHON) build_hw19_figures.py

$(HW26_FIGURES) &: build_hw25_26_figures.py
	$(PYTHON) build_hw25_26_figures.py

$(HW20_28_FIGURES) &: build_hw20_28_figures.py
	$(PYTHON) build_hw20_28_figures.py

tidy:
	$(LATEXMK) -c $(TARGET).tex

clean:
	$(LATEXMK) -C $(TARGET).tex
