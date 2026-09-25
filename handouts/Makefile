LATEXMK = latexmk
FLAGS = -xelatex -interaction=nonstopmode -halt-on-error
WRAPPERS := $(wildcard lesson_??_handout.tex) handout_template.tex

.PHONY: all L01 L02 L03 L04 L05 L06 L07 L08 L09 L10 L12 L13 L14 \
	lesson01 lesson02 lesson03 lesson04 lesson05 lesson06 lesson07 lesson08 lesson09 lesson10 \
	lesson12 lesson13 lesson14 \
	template tidy clean

all: lesson01 lesson02 lesson03 lesson04 lesson05 lesson06 lesson07 lesson08 lesson09 lesson10 \
	lesson12 lesson13 lesson14

L01: lesson_01_handout.pdf

L02: lesson_02_handout.pdf

L03: lesson_03_handout.pdf

L04: lesson_04_handout.pdf

L05: lesson_05_handout.pdf

L06: lesson_06_handout.pdf

L07: lesson_07_handout.pdf

L08: lesson_08_handout.pdf

L09: lesson_09_handout.pdf

L10: lesson_10_handout.pdf

L12: lesson_12_handout.pdf

L13: lesson_13_handout.pdf

L14: lesson_14_handout.pdf

lesson01: L01

lesson02: L02

lesson03: L03

lesson04: L04

lesson05: L05

lesson06: L06

lesson07: L07

lesson08: L08

lesson09: L09

lesson10: L10

lesson12: L12

lesson13: L13

lesson14: L14

lesson_01_handout.pdf: lesson_01_handout.tex lesson_01_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_01_handout.tex

lesson_02_handout.pdf: lesson_02_handout.tex lesson_02_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_02_handout.tex

lesson_03_handout.pdf: lesson_03_handout.tex lesson_03_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_03_handout.tex

lesson_04_handout.pdf: lesson_04_handout.tex lesson_04_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_04_handout.tex

lesson_05_handout.pdf: lesson_05_handout.tex lesson_05_handout_body.tex spectra.pdf ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_05_handout.tex

lesson_06_handout.pdf: lesson_06_handout.tex lesson_06_handout_body.tex ne630boardhandout.cls figures/h1_xsec.pgf figures/u235_fission.pgf figures/u238_threshold.pdf
	$(LATEXMK) $(FLAGS) lesson_06_handout.tex

lesson_07_handout.pdf: lesson_07_handout.tex lesson_07_handout_body.tex ne630boardhandout.cls figures/u238_threshold.pdf
	$(LATEXMK) $(FLAGS) lesson_07_handout.tex

lesson_08_handout.pdf: lesson_08_handout.tex lesson_08_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_08_handout.tex

lesson_09_handout.pdf: lesson_09_handout.tex lesson_09_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_09_handout.tex

lesson_10_handout.pdf: lesson_10_handout.tex lesson_10_handout_body.tex ne630boardhandout.cls figures/nr.pdf figures/wr.pdf
	$(LATEXMK) $(FLAGS) lesson_10_handout.tex

lesson_12_handout.pdf: lesson_12_handout.tex lesson_12_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_12_handout.tex

lesson_13_handout.pdf: lesson_13_handout.tex lesson_13_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_13_handout.tex

lesson_14_handout.pdf: lesson_14_handout.tex lesson_14_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_14_handout.tex

handout_template.pdf: handout_template.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) handout_template.tex

template: handout_template.pdf

tidy:
	$(LATEXMK) -c $(WRAPPERS)

clean:
	$(LATEXMK) -C $(WRAPPERS)
