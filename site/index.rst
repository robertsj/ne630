NE 630: Nuclear Reactor Theory
==============================

Handouts
--------

Download and print each available handout before class. The PDF and student
TeX wrapper are linked in the table; complete source bundles and supporting
TeX files are linked below it. A dash indicates that no handout or additional
resource is currently available for that lesson.

.. list-table:: Lesson materials
   :header-rows: 1
   :widths: 42 18 40
   :class: handout-table

   * - Lesson
     - Handout
     - Notebooks and other resources
   * - **Lesson 1** — Mass, Energy, and Nuclear Reactions
     - [`PDF <_static/handouts/lesson-01/lesson_01_handout.pdf>`__][`TeX <_static/handouts/lesson-01/lesson_01_handout.tex>`__]
     - —
   * - **Lesson 2** — Nuclear Fission and Chain Reactions
     - [`PDF <_static/handouts/lesson-02/lesson_02_handout.pdf>`__][`TeX <_static/handouts/lesson-02/lesson_02_handout.tex>`__]
     - —
   * - **Lesson 3** — Radioactive Decay
     - [`PDF <_static/handouts/lesson-03/lesson_03_handout.pdf>`__][`TeX <_static/handouts/lesson-03/lesson_03_handout.tex>`__]
     - —
   * - **Lesson 4** — Neutron Attenuation
     - [`PDF <_static/handouts/lesson-04/lesson_04_handout.pdf>`__][`TeX <_static/handouts/lesson-04/lesson_04_handout.tex>`__]
     - —
   * - **Lesson 5** — Using Cross-Section Data
     - [`PDF <_static/handouts/lesson-05/lesson_05_handout.pdf>`__][`TeX <_static/handouts/lesson-05/lesson_05_handout.tex>`__]
     - `Spectrum figure <_static/handouts/lesson-05/spectra.pdf>`__
   * - **Lesson 6** — Understanding Cross-Section Data
     - [`PDF <_static/handouts/lesson-06/lesson_06_handout.pdf>`__][`TeX <_static/handouts/lesson-06/lesson_06_handout.tex>`__]
     - `U-238 threshold figure <_static/handouts/lesson-06/figures/u238_threshold.pdf>`__ |middot|
       `OpenMC notebook <_static/handouts/lesson-06/figures/u238_threshold.ipynb>`__
   * - **Lesson 7** — Scattering Kinematics
     - [`PDF <_static/handouts/lesson-07/lesson_07_handout.pdf>`__][`TeX <_static/handouts/lesson-07/lesson_07_handout.tex>`__]
     - `U-238 threshold figure <_static/handouts/lesson-07/figures/u238_threshold.pdf>`__ |middot|
       `OpenMC notebook <_static/handouts/lesson-07/figures/u238_threshold.ipynb>`__
   * - **Lesson 8** — The Reproduction Factor, η
     - —
     - `OpenMC notebook <_static/notebooks/lesson_8.ipynb>`__

Handout source and support files
--------------------------------

The TeX links in the table point to each student wrapper. Download the complete
source bundle for a ready-to-build copy, or pair a wrapper with its public body
file and the shared class.

* **Lesson 1:** `source bundle <_static/handouts/lesson-01/lesson_01_handout_source.zip>`__ |middot|
  `body <_static/handouts/lesson-01/lesson_01_handout_body.tex>`__
* **Lesson 2:** `source bundle <_static/handouts/lesson-02/lesson_02_handout_source.zip>`__ |middot|
  `body <_static/handouts/lesson-02/lesson_02_handout_body.tex>`__
* **Lesson 3:** `source bundle <_static/handouts/lesson-03/lesson_03_handout_source.zip>`__ |middot|
  `body <_static/handouts/lesson-03/lesson_03_handout_body.tex>`__
* **Lesson 4:** `source bundle <_static/handouts/lesson-04/lesson_04_handout_source.zip>`__ |middot|
  `body <_static/handouts/lesson-04/lesson_04_handout_body.tex>`__
* **Lesson 5:** `source bundle <_static/handouts/lesson-05/lesson_05_handout_source.zip>`__ |middot|
  `body <_static/handouts/lesson-05/lesson_05_handout_body.tex>`__
* **Lesson 6:** `source bundle <_static/handouts/lesson-06/lesson_06_handout_source.zip>`__ |middot|
  `body <_static/handouts/lesson-06/lesson_06_handout_body.tex>`__
* **Lesson 7:** `source bundle <_static/handouts/lesson-07/lesson_07_handout_source.zip>`__ |middot|
  `body <_static/handouts/lesson-07/lesson_07_handout_body.tex>`__

All bundles include the shared
`ne630boardhandout.cls <_static/handouts/ne630boardhandout.cls>`__ class. No
course-specific ``.sty`` file is currently required. Compile a downloaded
bundle with:

.. code-block:: console

   latexmk -xelatex -interaction=nonstopmode -halt-on-error lesson_01_handout.tex

The public body files are student-safe exports. Instructor reveal values and
instructor-only figure content are deliberately omitted.

.. |middot| unicode:: U+00B7
