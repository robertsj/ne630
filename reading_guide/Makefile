# Programmed reading guides for FNRP Chapters 6 and 7.
LATEXMK ?= latexmk
PYTHON  ?= python3
FLAGS   := -xelatex -interaction=nonstopmode -halt-on-error
LUAFLAGS := -lualatex -interaction=nonstopmode -halt-on-error
LUA_CACHE ?= /tmp/ne630-reading-guide-luatex
SOURCES := $(wildcard ch*_guide.tex)
GUIDES  := $(SOURCES:.tex=.pdf)
LANDSCAPE_GUIDES := $(SOURCES:.tex=_landscape.pdf)
REFERENCE_GUIDES := $(SOURCES:.tex=_landscape_reference.pdf)
PLAYWRITE_GUIDES := $(SOURCES:.tex=_landscape_playwrite.pdf)
INDIE_EULER_GUIDES := $(SOURCES:.tex=_landscape_indie_euler.pdf)
COMMON_DEPS := ne630guide.sty ../handouts/ne630handout.cls figures/data/bessel.dat
export TEXINPUTS := ../handouts//:$(TEXINPUTS)

.PHONY: all portrait landscape both reference playwrite indie-euler verify data tidy clean

all: $(GUIDES)

portrait: $(GUIDES)

landscape: $(LANDSCAPE_GUIDES)

both: portrait landscape

reference: $(REFERENCE_GUIDES)

playwrite: $(PLAYWRITE_GUIDES)

indie-euler: $(INDIE_EULER_GUIDES)

# LuaLaTeX supports switching between the instructional and answer math fonts.
# Give its font loader a writable cache even in a restricted environment.
%_landscape_indie_euler.pdf: %.tex $(COMMON_DEPS) Makefile .latexmkrc fonts/indieflower/IndieFlower-Regular.ttf
	@mkdir -p "$(LUA_CACHE)"
	TEXMFCACHE="$(LUA_CACHE)" TEXMFVAR="$(LUA_CACHE)" \
		$(LATEXMK) $(LUAFLAGS) -jobname=$*_landscape_indie_euler \
		-usepretex='\PassOptionsToPackage{landscape,indieflower,eulermath}{ne630guide}' $<

%_landscape_playwrite.pdf: %.tex $(COMMON_DEPS) Makefile .latexmkrc fonts/playwrite/PlaywriteUSModern-Regular.ttf
	$(LATEXMK) $(FLAGS) -jobname=$*_landscape_playwrite \
		-usepretex='\PassOptionsToPackage{landscape,playwrite}{ne630guide}' $<

%_landscape_reference.pdf: %.tex $(COMMON_DEPS) Makefile .latexmkrc
	$(LATEXMK) $(FLAGS) -jobname=$*_landscape_reference \
		-usepretex='\PassOptionsToPackage{landscape,reference}{ne630guide}' $<

%_landscape.pdf: %.tex $(COMMON_DEPS) Makefile .latexmkrc
	$(LATEXMK) $(FLAGS) -jobname=$*_landscape \
		-usepretex='\PassOptionsToPackage{landscape}{ne630guide}' $<

%.pdf: %.tex $(COMMON_DEPS) Makefile .latexmkrc
	$(LATEXMK) $(FLAGS) $<

# Every number quoted in the guides is recomputed here; --write refreshes the
# tabulated Bessel functions used by the Chapter 7 figure.
figures/data/bessel.dat: tools/verify_examples.py
	$(PYTHON) tools/verify_examples.py --write > /dev/null

data: figures/data/bessel.dat

verify:
	$(PYTHON) tools/verify_examples.py

tidy:
	$(LATEXMK) -c $(SOURCES)
	@for source in $(SOURCES); do \
		for suffix in landscape landscape_reference landscape_playwrite landscape_indie_euler; do \
			$(LATEXMK) -c -jobname=$${source%.tex}_$$suffix $$source || exit $$?; \
		done; \
	done

clean:
	$(LATEXMK) -C $(SOURCES)
	@for source in $(SOURCES); do \
		for suffix in landscape landscape_reference landscape_playwrite landscape_indie_euler; do \
			$(LATEXMK) -C -jobname=$${source%.tex}_$$suffix $$source || exit $$?; \
		done; \
	done
