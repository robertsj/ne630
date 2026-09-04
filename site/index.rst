NE 630: Nuclear Reactor Theory
==============================

Handouts
--------

Download and print the PDF for each lesson before class. Each handout is a
two-page, US Letter worksheet designed to be completed alongside the board
work.

.. list-table:: Lesson handouts
   :header-rows: 1
   :widths: 8 34 18 40
   :class: handout-table

   * - Lesson
     - Topic
     - Print
     - TeX source
   * - 1
     - Mass, Energy, and Nuclear Reactions
     - `PDF <_static/handouts/lesson-01/lesson_01_handout.pdf>`__
     - `Source bundle <_static/handouts/lesson-01/lesson_01_handout_source.zip>`__

       `wrapper <_static/handouts/lesson-01/lesson_01_handout.tex>`__ |middot|
       `body <_static/handouts/lesson-01/lesson_01_handout_body.tex>`__
   * - 2
     - Nuclear Fission and Chain Reactions
     - `PDF <_static/handouts/lesson-02/lesson_02_handout.pdf>`__
     - `Source bundle <_static/handouts/lesson-02/lesson_02_handout_source.zip>`__

       `wrapper <_static/handouts/lesson-02/lesson_02_handout.tex>`__ |middot|
       `body <_static/handouts/lesson-02/lesson_02_handout_body.tex>`__
   * - 3
     - Radioactive Decay
     - `PDF <_static/handouts/lesson-03/lesson_03_handout.pdf>`__
     - `Source bundle <_static/handouts/lesson-03/lesson_03_handout_source.zip>`__

       `wrapper <_static/handouts/lesson-03/lesson_03_handout.tex>`__ |middot|
       `body <_static/handouts/lesson-03/lesson_03_handout_body.tex>`__
   * - 4
     - Neutron Attenuation
     - `PDF <_static/handouts/lesson-04/lesson_04_handout.pdf>`__
     - `Source bundle <_static/handouts/lesson-04/lesson_04_handout_source.zip>`__

       `wrapper <_static/handouts/lesson-04/lesson_04_handout.tex>`__ |middot|
       `body <_static/handouts/lesson-04/lesson_04_handout_body.tex>`__
   * - 5
     - Using Cross-Section Data
     - `PDF <_static/handouts/lesson-05/lesson_05_handout.pdf>`__
     - `Source bundle <_static/handouts/lesson-05/lesson_05_handout_source.zip>`__

       `wrapper <_static/handouts/lesson-05/lesson_05_handout.tex>`__ |middot|
       `body <_static/handouts/lesson-05/lesson_05_handout_body.tex>`__ |middot|
       `spectrum figure <_static/handouts/lesson-05/spectra.pdf>`__
   * - 6
     - Understanding Cross-Section Data
     - `PDF <_static/handouts/lesson-06/lesson_06_handout.pdf>`__
     - `Source bundle <_static/handouts/lesson-06/lesson_06_handout_source.zip>`__

       `wrapper <_static/handouts/lesson-06/lesson_06_handout.tex>`__ |middot|
       `body <_static/handouts/lesson-06/lesson_06_handout_body.tex>`__ |middot|
       `U-238 threshold figure <_static/handouts/lesson-06/figures/u238_threshold.pdf>`__

Shared LaTeX support
--------------------

All source bundles include the shared
`ne630boardhandout.cls <_static/handouts/ne630boardhandout.cls>`__ class. No
course-specific ``.sty`` file is currently required. Compile a downloaded
bundle with:

.. code-block:: console

   latexmk -xelatex -interaction=nonstopmode -halt-on-error lesson_01_handout.tex

The public body files are student-safe exports. Instructor reveal values and
instructor-only figure content are deliberately omitted.

.. |middot| unicode:: U+00B7
