# Lesson 32

## Learning Objectives

### Macro Objectives

Students will be able to develop solutions for the one-speed diffusion equation in slab geometry for 
single-region systems with constant $D$, constant $\Sigma_a$, and an arbitrary volumetric source term $s(x)$.

### Micro Objectives

 - Explain what is meant by "slab" geometry and under which conditions such a model is of use.
 - Describe what "homogeneous" and "particular" solutions are and the basic techniques used to find them.
 - Verify that a solution $\phi(x)$ satisfies the diffusion equation.
 - Verify that a solution $\phi(x)$ preserves neutron balance over an arbitrary volume.

## Key Terms

 - diffusion length
 - method of undetermined coefficients
 - homogeneuous solution
 - particular solution
  

## Before Lecture

You are responsible for doing the following:

  - Read Section 6.3.
  - Although we'll review some aspects of solving second-order ODEs over the next several lessons, you
    should be generally familiar with solving such equations, especially when the equation has 
    "constant coefficients."  Here's [one resource](https://tutorial.math.lamar.edu/Classes/DE/IntroSecondOrder.aspx)
    that may help you refresh what you once learned.
    
 

## After Lecture

### Homework

  - [32.1] Consider a finite, homogeneous slab over $x \in [-a, a]$, with a 
    source $s(x) = s_0 \cos(\pi x / (2a))$ [1/cm$^3$-s].  

    (a) Determine the neutron flux $\phi(x)$ assuming it vanishes at the boundaries.
    (b) For $D = 0.84$ [cm], $\Sigma_a = 2.1\cdot 10^{-4}$, 
        $a = 10$ cm, and $s_0 = 1$ [1/cm$^3$-s], plot
        both $\phi(x)$ and $\vec{J}\cdot \hat{i} = J_x(x)$.
    (c) Verify neutron balance over slab by computing the 
        total source rate, total absorption rate, and total
        leakage rate.

