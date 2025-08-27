TEX=xelatex
BIB=biber

TEX_FILES=$(wildcard *.tex)
PDF_FILES=$(TEX_FILES:.tex=.pdf)
TEMP_FILES=$(wildcard *.aux *.bbl *.blg *.bcf *.log *.nav *.out *.snm *.synctex.gz *.toc *.run.xml)

.PHONY: all clean tidy git_sha

# Default target
all: git_sha.txt $(PDF_FILES)

# Rule to compile any .tex file into a .pdf
%.pdf: %.tex
	@echo "Compiling $< with $(TEX)..."
	$(TEX) -shell-escape $<
	@# If a .bcf file exists, run biber for bibliography
	if [ -f "$(basename $<).bcf" ]; then $(BIB) $(basename $<); fi
	@# Run xelatex again to ensure proper cross-references
	$(TEX) -shell-escape $<

# Generate git_sha.txt in the current directory
git_sha.txt:
	@echo "Generating git_sha.txt..."
	@git rev-parse --short=6 HEAD > git_sha.txt

# Tidy up but keep .pdf files
tidy:
	@echo "Tidying up temporary files..."
	rm -f $(TEMP_FILES)

# Clean everything
clean:
	@echo "Cleaning all files, including PDFs and git_sha.txt..."
	rm -f $(PDF_FILES) $(TEMP_FILES) git_sha.txt

