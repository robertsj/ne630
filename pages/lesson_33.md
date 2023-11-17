# Lesson 33

## Learning Objectives

### Macro Objectives

Students will be able to define and solve the equations representing multi-region, source-driven, slab systems subject to vacuum and reflecting boundary conditions. 

### Micro Objectives

 - Explain in plain English what is meant by "partial current."
 - List the quantities involved in the diffusion equation that
   must be continuous throughout the domain.
 - For a homogeneous region within a slab system of one or more regions,
   determine the particular solution given the source term $s(x)$ in 
   that region.
 - Given the homogeneous and particular solutions for each of $N$ regions of 
   a heterogeneous slab and the boundary conditions at the left and 
   ride surfaces of the slab, write down the system of $2N$ equations
   needed to determine each constant of integration.
 - Use `numpy.linalg.solve` or other tools (perhaps from MATH 551) to 
   solve linear systems.

## Key Terms

 - boundary condition
 - vacuum boundary condition
 - reflective boundary condition
 - albedo boundary condition
 - extrapolated flux boundary condition
 - continuity condition
 - partial current
 - surface source
  

## Before Lecture

You are responsible for doing the following:

  - Read Section 6.4.
  - Review how to solve linear systems.  As I've mentioned, I'm usually against doing pages of algebra just to find expressions for the constants of integration when solving ODEs (unless the resulting expressions are of some unique value---and that's rare in my experience). Thus, I strongly recommend the use of numerical tools when appropriate, and for solving matrix systems, I recommend [NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html).  
    
 

## After Lecture

### Homework

  - [33.1] Consider a slab of width $a$ divided into two, 
    equal-sized regions having unique but constant 
    $D$, $\Sigma_a$, and $s$.  The first region extends
    from $x=0$ to $x=a/2$ and is subject to reflection at 
    its left boundary.  The second region is subject to
    vacuum at its right boundary.  

    a. The full solution (after determining the particular solution) 
       includes 4 constants of integration
       determined by a system of linear equations.  Define this system.
    b. Use `numpy.linalg.solve` (or, if you prefer, solve the system 
       by hand) for $D^I = 1.0$, $\Sigma^I_a = 0.2$, $D^{II} = 1.5$,
       $\Sigma_a^{II} = 0.02$, $s^I = 1$, $s^{II} = 0$, and
       $a=50$, and plot
       the resulting flux.

  - [33.2] Consider a source-free slab of width $a$.
    An incident partial current of $J^L_{in}$ enters at the left 
    boundary, while the right boundary is adjacent to vacuum.
    
    a. Determine the reflection coefficient $R = J^L_{out}/J^L_{in}$
    and the transmission coefficient $T = J^R_{out}/J^L_{in}$.
    
    b. Given $J^L_{in}$, $R$, and $T$, what is $\Sigma_a \int^a_0 \phi(x) dx$?
    

