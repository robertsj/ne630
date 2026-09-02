LATEXMK = latexmk
FLAGS = -xelatex -interaction=nonstopmode -halt-on-error

.PHONY: all lesson01 lesson02 lesson03 lesson04 lesson05 template clean

all: lesson01 lesson02 lesson03 lesson04 lesson05

lesson01: lesson_01_handout.pdf lesson_01_handout_instructor.pdf

lesson02: lesson_02_handout.pdf lesson_02_handout_instructor.pdf

lesson03: lesson_03_handout.pdf lesson_03_handout_instructor.pdf

lesson04: lesson_04_handout.pdf lesson_04_handout_instructor.pdf

lesson05: lesson_05_handout.pdf lesson_05_handout_instructor.pdf

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

handout_template.pdf: handout_template.tex ne630boardhandout.cls
	$(LATEXMK) $(FLAGS) handout_template.tex

template: handout_template.pdf

clean:
	$(LATEXMK) -C lesson_01_handout.tex
	$(LATEXMK) -C lesson_01_handout_instructor.tex
	$(LATEXMK) -C lesson_02_handout.tex
	$(LATEXMK) -C lesson_02_handout_instructor.tex
	$(LATEXMK) -C lesson_03_handout.tex
	$(LATEXMK) -C lesson_03_handout_instructor.tex
	$(LATEXMK) -C lesson_04_handout.tex
	$(LATEXMK) -C lesson_04_handout_instructor.tex
	$(LATEXMK) -C lesson_05_handout.tex
	$(LATEXMK) -C lesson_05_handout_instructor.tex
	$(LATEXMK) -C handout_template.tex
