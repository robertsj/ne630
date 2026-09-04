LATEXMK = latexmk
FLAGS = -xelatex -interaction=nonstopmode -halt-on-error
WRAPPERS := $(wildcard lesson_??_handout.tex lesson_??_handout_instructor.tex) handout_template.tex

.PHONY: all L01 L02 L03 L04 L05 L06 \
	lesson01 lesson02 lesson03 lesson04 lesson05 lesson06 \
	template tidy clean

all: lesson01 lesson02 lesson03 lesson04 lesson05 lesson06

L01: lesson_01_handout.pdf

L02: lesson_02_handout.pdf

L03: lesson_03_handout.pdf

L04: lesson_04_handout.pdf

L05: lesson_05_handout.pdf

L06: lesson_06_handout.pdf

lesson01: L01 lesson_01_handout_instructor.pdf

lesson02: L02 lesson_02_handout_instructor.pdf

lesson03: L03 lesson_03_handout_instructor.pdf

lesson04: L04 lesson_04_handout_instructor.pdf

lesson05: L05 lesson_05_handout_instructor.pdf

lesson06: L06

lesson_01_handout.pdf: lesson_01_handout.tex lesson_01_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_01_handout.tex

lesson_01_handout_instructor.pdf: lesson_01_handout_instructor.tex lesson_01_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_01_handout_instructor.tex

lesson_02_handout.pdf: lesson_02_handout.tex lesson_02_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_02_handout.tex

lesson_02_handout_instructor.pdf: lesson_02_handout_instructor.tex lesson_02_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_02_handout_instructor.tex

lesson_03_handout.pdf: lesson_03_handout.tex lesson_03_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_03_handout.tex

lesson_03_handout_instructor.pdf: lesson_03_handout_instructor.tex lesson_03_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_03_handout_instructor.tex

lesson_04_handout.pdf: lesson_04_handout.tex lesson_04_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_04_handout.tex

lesson_04_handout_instructor.pdf: lesson_04_handout_instructor.tex lesson_04_handout_body.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_04_handout_instructor.tex

lesson_05_handout.pdf: lesson_05_handout.tex lesson_05_handout_body.tex spectra.pdf ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_05_handout.tex

lesson_05_handout_instructor.pdf: lesson_05_handout_instructor.tex lesson_05_handout_body.tex spectra.pdf ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) lesson_05_handout_instructor.tex

lesson_06_handout.pdf: lesson_06_handout.tex lesson_06_handout_body.tex ne630boardhandout.cls figures/h1_xsec.pgf figures/u235_fission.pgf figures/u238_threshold.pdf
	$(LATEXMK) $(FLAGS) lesson_06_handout.tex

handout_template.pdf: handout_template.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) handout_template.tex

template: handout_template.pdf

tidy:
	$(LATEXMK) -c $(WRAPPERS)

clean:
	$(LATEXMK) -C $(WRAPPERS)
