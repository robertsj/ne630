# Lesson 19

<!--

4-factor analysis of a LWR pin cell, P/D.


https://info.ornl.gov/sites/publications/Files/Pub172008.pdf

https://inldigitallibrary.inl.gov/sites/sti/sti/3395100.pdf


The formal content for this lesson is incomplete.  A few numerical 
examples would be good.  I included the "data fit" as 
-->

## Learning Objectives

### Macro Objectives


Students will be able to design unit cells that meet target objectives
within given constraints.


### Micro Objectives

 - Apply minimization to a function $f(x)$ to obtain optimum values of $x$
 - Explain how changes in $P/D$ effect $f$, $p$, and $k_{\infty}$ of a PWR unit cell.
 - Explain how changes in the Pu fraction impact $k_{\infty}$ of a SFR unit cell.
 - Fit data points to a polynomial.

## Key Terms

 - under-, over-, and optimally-moderated
 - $P/D$ ratio 
 - parametric study
 - numerical optimization
 - high- and low-order model
 

## Before Lecture

  - (Re)read the last bit of 4.4.


## After Lecture

### Homework

 - In the lesson 18 notebook, I explained how to transform Eqs. (4.25), (4.28), (4.48), and (4.49) into the two-group form forms that use fuel and non-fuel quantities. 
    + Write these expressions down.
    + The expression for $p$ is missing one possible source of absorption.  Write down a modified form of 
      $p$ that includes this term.
    + With that modified $p$ and the other three factors, show that $\eta_T f p \varepsilon$ recovers
      our familiar gains (from fission in the fuel) to losses (from absorption anywhere) definition 
      of $k_{\infty}$.

 - (Similar to 4.10) Use `LWRUnitCell` with the default fuel and cladding radii and enrichment.  Then, 
   determine the P/D ratios that represent $V_{nf}/V_{f} = 0.5$ and $V_{nf}/V_{f} = 2.5$.  For P/D 
   values between those extremes, use `LWRUnitCell` to compute and plot 
   the four factors and $k_{\infty}$.
