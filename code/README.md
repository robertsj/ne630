# NE 630 kinetics code

The Lessons 27 and 28 historical notebooks and ne630_kinetics.py live here.
The solver provides f and solve and uses NumPy and SciPy. Running
python code/ne630_kinetics.py plots the Lesson 27 Example 4 pulse using
Matplotlib. The historical notebooks retain their own standalone examples.

The public module is exported to site/_static/notebooks/ne630_kinetics.py
by make sync-code and linked from Lesson 28; its public filename is stable.
The notebooks are not newly published. Other lessons remain in notebooks/.

The local lesson_28_exploration.ipynb is not included in this release: it
still imports a former, incompatible API and needs instructor review.
