# Lesson 20

## Learning Objectives

### Macro Objectives


Students will be able to quantify the impact of changes in the fuel temperature
on the reactivity.

### Micro Objectives

 - Explain the relationship between reactivity and the multiplication factor.
 - Explain why the fuel temperature coefficient (FTC) is usually strongly negative.
 - Explain how the fuel temperature coefficient of a sodium-cooled fast reactor differs from 
   that of a light-water reactor.

## Key Terms

 - reactivity
 - units of reactivity: dollars and cents; $\Delta k/k$; percent-milli (pcm)
 - fuel temperature coefficient (FTC)



## Before Lecture

  - Read 9.1-9.2 (through FTC)  



## After Lecture

### Homework

  - Problem 9.1.
  - Use `SFRUnitCell` to estimate the fuel and coolant temperature coefficients of reactivity
    at the default conditions of $T_f = 900$ K and $T_c = 500$ K based on a *finite difference*
    approximation.  To ensure that the uncertainty in the computed coefficients are negligible,
    set the number of particles in the `run` function to one million.  How do these coefficients
    compare to the PWR coefficients at nominal full-power conditions (i.e., $T_f = 900$ K and 
    $T_c = 300$ K)? <!-- update these temperatures -->

