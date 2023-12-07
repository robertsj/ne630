# Lesson 36

## Learning Objectives

### Macro Objectives

Students will be able to write down the equations necessary to model
multi-region reactors using the two-group approximation and to solve
such equations numerically.

### Micro Objectives

 - Explain what the *removal cross section* $\Sigma_r$ represents.
 - Explain what the scattering cross section $\Sigma_{s_{2\gets 1}}$ represents.
   (Pay attention to the arrow, which I use to make explicit how the indices are 
   ordered!)
 - Explain why the "right-hand sides" of the two-group equations (in Eq. (7-40) of
   Duderstadt and Hamilton; see reading below) are the appropriate "gains" terms
   for each energy group.
 - Explain what the migration area is as it relates to a neutron's life.
 - Determine $k$ for a bare, homogeneous reactor in 1-D slab or 1-D cylindrical 
   coordinates subject to zero-flux boundary conditions.
 - Describe why one would use $M^2$ in place of $L_1^2$ in the modified one-group diffusion.

## Key Terms

 - two-group approximation 
 - modified one-group approximation
 - removal cross section 
 - migration length
 - group collapsing
 - six-factor formula
  

## Before Lecture

You are responsible for doing the following:

  - Read [Section 7.III.B-7.III.C](link) of Duderstadt and Hamiliton (D&H).  I've 
    annotated the linked PDF with a few comments.  I've also highlighted a number 
    of terms and equations that you should make sure to define in your notes.
  - Read Section 7.4 of Lewis.  Although the D&H sections provide the fundamental 
    "equations," Lewis provides some physical "insight" regarding the numerical 
    values of the two-group diffusion lengths and associated migration area. 

## After Lecture

### Homework


- [36.1] Consider a bare, homogeneous slab reactor of width $a$.  Use the two-group data of Table 7-2 in D&H to determine the critical width $a$ assuming that $\phi_g(-a/2) = \phi_g{a/2} = 0$ for $g = 1$ and $g=2$.  How would your answer differ if we applied vacuum conditions instead?  Explain.



