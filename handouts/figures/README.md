# Handout figure sources

## Xe-135 capture cross section (Lesson 22)

`plot_xe135_capture.py` is a standalone generator. It reads **Xe135, MT=102
(radiative capture)** using OpenMC's Python data API and writes:

- `xe135_capture.pgf`: self-contained vector PGFPlots figure, including its
  numerical table; no raster image or external data file is needed by LaTeX.
- `xe135_capture.json`: provenance, HDF5/XML checksums, OpenMC version,
  temperature, energy domain, and the exact annotated cross section.

It uses the installed OpenMC library; it does **not** run a transport simulation,
create synthetic cross sections, or require Matplotlib. The native energy grid
is retained and augmented by logarithmically spaced samples so sharp features
are not lost to coarse resampling. Energies are eV; cross sections are barns.

### Regenerate

Activate a Python environment containing OpenMC and NumPy, then run from any
working directory:

```bash
python /path/to/handouts/figures/plot_xe135_capture.py \
  --cross-sections /path/to/cross_sections.xml \
  --library-label ENDF/B-VIII.0
```

Alternatively, set `OPENMC_CROSS_SECTIONS` or use `--hdf5 /path/to/Xe135.h5`.
`--temperature` accepts an exact available table key (default `294K`);
`--output` changes the destination PGF. Outputs default to the script directory.
The optional library label is provenance only and must describe the selected
library; the script does not infer an evaluation name from arbitrary HDF5 data.

The verified local command is:

```bash
/home/robertsj/opt/miniforge3/envs/openmc/bin/python \
  /home/robertsj/Classes/ne630/handouts/figures/plot_xe135_capture.py \
  --cross-sections /home/robertsj/opt/openmc/endfb-viii.0-hdf5/cross_sections.xml \
  --library-label ENDF/B-VIII.0
```

From `handouts/`, `make xe135-figure` is also available. Override
`OPENMC_PYTHON` for the interpreter and pass optional arguments through
`XE135_PLOT_FLAGS`. Ordinary `make L22` uses the existing PGF and does not
require OpenMC or the nuclear-data library.

### Colors, typography, and inclusion

The curve uses Wildcat purple (`wcprimary`, `#512888`), and the thermal point,
arrow, and annotation use orange (`wcalerted`, `#CA7C1B`). All tick labels, axis
labels, and annotation text use 8 pt / 9.5 pt leading. Text and math faces are
inherited from the including document: Myriad Pro and Libertinus Math in the
current handout, or its configured font fallback.

```tex
% The ne630handout class already loads TikZ/PGFPlots and the required libraries.
\begin{center}
  \input{figures/xe135_capture.pgf}
\end{center}
```

Do **not** use `\resizebox` or `\includegraphics`: the PGF sets its width from
`\linewidth` while keeping text size fixed. In a different document, load
`pgfplots`, set `compat=1.18`, and load the TikZ `arrows.meta` library.
The figure supplies the two color names only if the parent has not defined them.

### Verified data point

The local ENDF/B-VIII.0 library at `294K` gives
`σγ(0.0253 eV) = 2,664,214 b`: approximately **3 million**, not 3 billion,
barns. The orange annotation is generated from this evaluated value, not
hard-coded. The processed HDF5 grid contains 2,665 points; the delivered PGF
contains 4,264 evaluated samples, including the exact annotation energy.

The former `lesson_22_xe135_comparison.pdf` is retained as a historical asset
but is no longer referenced by L22. The transient figure is unchanged.

API reference: [OpenMC IncidentNeutron](https://docs.openmc.org/en/stable/pythonapi/generated/openmc.data.IncidentNeutron.html)
and [DataLibrary](https://docs.openmc.org/en/stable/pythonapi/generated/openmc.data.DataLibrary.html).
