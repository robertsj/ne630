TEX := exam_01_reference
LATEX ?= lualatex

.PHONY: all clean
all: $(TEX).pdf

$(TEX).pdf: $(TEX).tex $(TEX)_body.tex ne630boardhandout.cls
	$(LATEX) -interaction=nonstopmode -halt-on-error $(TEX).tex
	$(LATEX) -interaction=nonstopmode -halt-on-error $(TEX).tex

clean:
	rm -f $(TEX).aux $(TEX).log $(TEX).out
