LATEXMK := latexmk
TARGET := fall_2026_ne630_solution_manual
FLAGS := -pdf -shell-escape -interaction=nonstopmode -halt-on-error
SOURCES := $(TARGET).tex \
	hw01.tex hw02.tex hw03.tex hw04.tex hw05.tex hw06.tex hw07.tex \
	hw08.tex hw09.tex hw10.tex hw11.tex hw12.tex hw13.tex
FIGURES := $(wildcard figures/*)

.PHONY: all tidy clean

all: $(TARGET).pdf

$(TARGET).pdf: $(SOURCES) $(FIGURES)
	$(LATEXMK) $(FLAGS) $(TARGET).tex

tidy:
	$(LATEXMK) -c $(TARGET).tex

clean:
	$(LATEXMK) -C $(TARGET).tex
