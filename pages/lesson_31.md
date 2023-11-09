# Lesson 31

## Learning Objectives

### Macro Objectives

Students will be able to show that neutrons are conserved (or not) in a spatial volume given the neutron flux and appropriate cross-section data.

### Micro Objectives

 - Write down, in plain English, a statement that describes neutron balance in a control volume.
 - Explain what the neutron current $\vec{J}$ represents.  Note that a vector $\vec{x}$ can also be written $\mathbf{x}$.
 - Given a neutron flux $\phi(\vec{r})$ and a diffusion coefficient $D(\mathbf{r})$, compute the neutron current.
 - Integrate the neutron continuity equation (Lewis, Eq. (6.10)) or the neutron diffusion equation (Lewis, Eq. (6.12)) over a control volume.
 - Describe how the neutron diffusion equation is similar to and different from other conservation equations in engineering.

## Key Terms

 - leakage
 - diffusion coefficient
 - Fick's law
 - gradient (of a function), $\vec{\nabla} f$
 - divergence (of a vector),  $\vec{\nabla} \cdot \vec{v}$
 - Laplacian (of a function), $\vec{\nabla}^2 f = \vec{\Delta} f$


## Before Lecture

You are responsible for doing the following:

  - Read Sections 6.1 and 6.2, and **take notes**, **upload your notes** by 1 pm (before lecture), and **bring these to class**.  On the Lesson 7 page, I provided [this example](https://k-state.instructure.com/courses/144758/files/33983345/download?download_frd=1) of notes I took while reading Sections 3.1--3.3.  In your notes, include definitions for the Key Terms above and questions you have as you read related to vocabulary and symbols. Then, make an effort to answer your questions!  As an example, if you get to Eq. (6.10) and don't recognize $\vec{\nabla}$, then you need to review your MATH 222 materials and add the appropriate definitions, examples, etc., to your notes.  This is the standard of preparation I expect for the rest of the semester.
 

## After Lecture

### Homework

  - [31.1] Consider a nonmultiplying, homogeneous system defined over $x \in [-1, 1]$, $y \in [-1, 1]$, and $z \in [-1, 1]$, and characterized by a 
           diffusion coefficient $D$ and absorption cross section $\Sigma_a$. 
           Suppose the steady-state neutron flux is $\phi(\vec{r}) = \phi(x, y, z) = (1-x^2)(1-y^2)$.
           What is the source distribution $s(\vec{r})$ [1/cm$^3$-s]?
  - [31.2] For the same system, compute the (1) total absorption rate [1/s] in the system and (2) the leakage rates [1/s] through each of its 6 faces.
           Show that the sum of the absorption rate and leakage rates equals the volume integral of your source distribution from [30.1].

