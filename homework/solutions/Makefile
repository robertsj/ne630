LATEXMK := latexmk
PYTHON ?= python3
TARGET := fall_2026_ne630_solution_manual
FLAGS := -pdf -shell-escape -interaction=nonstopmode -halt-on-error
SOURCES := $(TARGET).tex \
	hw01.tex hw02.tex hw03.tex hw04.tex hw05.tex hw06.tex hw07.tex \
	hw08.tex hw09.tex hw10.tex hw11.tex hw12.tex hw13.tex hw14.tex \
	hw15.tex hw16.tex hw17.tex hw18.tex
HW18_FIGURES := figures/hw18_koo.png figures/hw18_log_four_factors.png
FIGURES := $(wildcard figures/*) $(HW18_FIGURES)

.PHONY: all tidy clean

all: $(TARGET).pdf

$(TARGET).pdf: $(SOURCES) $(FIGURES)
	$(LATEXMK) $(FLAGS) $(TARGET).tex

$(HW18_FIGURES): build_hw18_figures.py data/hw18_p_over_d.csv
	$(PYTHON) build_hw18_figures.py

tidy:
	$(LATEXMK) -c $(TARGET).tex

clean:
	$(LATEXMK) -C $(TARGET).tex
