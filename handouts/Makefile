LATEXMK ?= latexmk
PYTHON ?= python3
PLOT_PYTHON ?= python
OPENMC_PYTHON ?= python3
XE135_PLOT_FLAGS ?=
FLAGS := -xelatex -interaction=nonstopmode -halt-on-error
LESSONS := $(patsubst lesson_%_handout.tex,%,$(wildcard lesson_??_handout.tex))
HANDOUTS := $(foreach n,$(LESSONS),lesson_$(n)_handout.pdf)
SUPPLEMENT_SOURCES := $(wildcard lesson_??_derivations.tex)
SUPPLEMENTS := $(SUPPLEMENT_SOURCES:.tex=.pdf)
WRAPPERS := $(wildcard lesson_??_handout.tex) $(SUPPLEMENT_SOURCES) handout_template.tex
SUPPORT := $(wildcard figures/*.tex figures/*.pgf figures/*.pdf) spectra.pdf
DRAFT_NAMES := subcrit_mult example_kinetics traces prompt_drop_illustration slab_bc multiplying_slab \
 lesson38_cell46 lesson38_cell50 lesson39_cell10 lesson39_cell11 lesson39_cell19 \
 lesson39_cell22 lesson39_cell24 lesson39_cell25 lesson39_cell27 lesson39_cell28 lesson39_cell30 lesson39_cell31
DRAFT_FIGURES := $(addprefix figures/drafts/,$(addsuffix .pdf,$(DRAFT_NAMES))) figures/drafts/manifest.json
DRAFT_DATA := $(wildcard figures/drafts/data/*.json figures/drafts/data/*.npz)

.PHONY: all template check-class check-content check-seeds xe135-figure lesson27-figure tidy clean $(foreach n,$(LESSONS),L$(n) lesson$(n))

all: $(HANDOUTS) $(SUPPLEMENTS)

$(foreach n,$(LESSONS),$(eval L$(n): lesson_$(n)_handout.pdf))
$(foreach n,$(LESSONS),$(eval lesson$(n): L$(n)))

lesson_%_derivations.pdf: lesson_%_derivations.tex ne630handout.cls $(SUPPORT)
	$(LATEXMK) $(FLAGS) $<

# latexmk tracks transitive TeX inputs; these prerequisites trigger its first pass.
lesson_%_handout.pdf: lesson_%_handout.tex ne630handout.cls $(SUPPORT)
	$(LATEXMK) $(FLAGS) $<

$(foreach n,01 02 03 04 05 06 07 08 09 10 12 13 14,$(eval lesson_$(n)_handout.pdf: lesson_$(n)_handout_body.tex))
lesson_22_handout.pdf: lesson_22_xenon_transient.py
lesson_27_handout.pdf: figures/lesson_27_traces.pdf
$(foreach n,25 26 29 30 31 32 33 34 35 36 37 38 39,$(eval lesson_$(n)_handout.pdf: $(DRAFT_FIGURES)))
$(foreach n,36 37 38 39,$(eval lesson_$(n)_handout.pdf: $(wildcard figures/notebook_$(n)/*.png)))

$(DRAFT_FIGURES) &: figures/build_draft_figures.py ne630handout.cls $(DRAFT_DATA)
	MPLCONFIGDIR=$(CURDIR)/figures/.mplconfig MPLBACKEND=Agg $(PLOT_PYTHON) figures/build_draft_figures.py

handout_template.pdf: handout_template.tex ne630handout.cls
	$(LATEXMK) $(FLAGS) $<

template: handout_template.pdf

check-class: $(DRAFT_FIGURES)
	$(PYTHON) check_handout_class.py

check-content:
	$(PYTHON) check_handout_content.py

check-seeds: $(DRAFT_FIGURES)
	$(PYTHON) check_seeded_handouts.py

# Explicit regeneration only: ordinary PDF builds use the checked-in PGF.
xe135-figure:
	$(OPENMC_PYTHON) figures/plot_xe135_capture.py $(XE135_PLOT_FLAGS)

# Revised L27 uses its supplied Br-87 figure, independent of draft figures.
lesson27-figure:
	MPLCONFIGDIR=$(CURDIR)/figures/.mplconfig MPLBACKEND=Agg $(PLOT_PYTHON) figures/make_lesson_27_traces.py

tidy:
	$(LATEXMK) -c $(WRAPPERS)

clean:
	$(LATEXMK) -C $(WRAPPERS)
