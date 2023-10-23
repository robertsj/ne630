# Lesson 22

## Learning Objectives

### Macro Objectives


Students will be able to quantify the impact of xenon buildup on reactivity.


### Micro Objectives

 - Model the impact of reactivity control, fission products, and depletion 
   by proper adjustments to the four-factor formula.
 - Quantify how the addition of chemical shim impacts the moderator temperature coefficient.
 - List the primary long-term changes in a nuclear reactor core

## Key Terms

 - reactivity control (all the methods by which $\rho$ can be adjusted, e.g., control rods)
 - reactivity worth (the change in $\rho$ due to the introduction/removal of a specific component or material, e.g., a control rod)
 - control rod (removable rods, blades, etc., made of neutron poisons like boron)
 - chemical shim (neutron poisons like boron dissolved in the coolant)
 - burnable poison (neutron poisons directly mixed with fuel)
 - fission product yield $\gamma_{\text{fp}}$
 - equilibrium xenon

## Before Lecture

  - Read 10.1-10.3


## After Lecture

### Homework

 The problems below may *look* very long, but the amount of number 
 crunching should be reasonably small if you organize your calculations
 well.  I highly recommend using a Python script or a spreadsheet so 
 that values can be reused (or easily modified) at each step.

 - [22.1] Consider the PWR described by Problem 4.6 in the book.  We'll walk through 
   the basic steps that bring a reactor from cold shutdown conditions to 
   criticality at full power conditions.  Where needed, use cross sections 
   listed in Table 3.2.

    (a) Compute the 4 factors for $T_f = T_m = 300$ K (i.e., room temperature).
        Assume that the probability of non-leakage is $P_{NL} = 0.95$ and compute 
        the reactivity $\rho$.  This reactivity is the **excess reactivity**, $\rho_{\text{ex}}$, which is
        the core reactivity with all removable control (e.g., control rods and 
        [chemical shim](https://www.nuclear-power.com/glossary/boron-10/boric-acid-chemical-shim/)) completely 
        removed.
    (b) Suppose that the **shutdown margin** is -4% $dk/k$, i.e., when all control rods are 
        completely inserted, the core reactivity is -0.04.  The total **reactivity worth** of these 
        control rods is $\Delta \rho = \rho_{\text{ex}} - 0.04$. What must $\Sigma_{\gamma}^{\text{con}}$ be 
        in this **cold shutdown** state?  You may want to re-read page 244.  
    (c) Assume that the partial insertion of control rods can be represented by 
        a fraction $x$ and that the corresponding macroscopic cross section 
        is $x\Sigma_{\gamma}^{\text{con}}$.  This means that, as a function of $x$, the 
        core reactivity should range from $\rho_{\text{ex}}$ (for $x=0$) down to 
        $-0.04$ (for $x=1$). Determine $x$ so that our reactor is critical.
        We'll call this $x_{\text{cc}}$ ("cc" for cold critical).
    (d) Next, the reactor coolant pumps are run until the coolant (and fuel) reach 
        600 K, i.e., **hot zero-power** conditions. You may assume the coolant 
        density is 0.66 g/cm$^3$.
        Recompute $\rho$ (with $x = x_{\text{cc}}$).  
        This $\rho$ is the **temperature defect**.
        Find $x$ so that our reactor is critical; we'll call this $x_{hzp}$.
    (e) Finally, the reactor is brought to **full power** conditions, and the fuel temperature 
        increases to 1200 K.  Recompute  $\rho$ (with $x = x_{\text{hzp}}$).
        This $\rho$ is the **power defect**.  Determine $x = x_{\text{fp}}$.

 - [22.2] Consider the hot, full-power conditions from part (e) of Problem 22.1.  
   For PWRs, excess reactivity is most often balanced by the use of boric acid dissolved in 
   the coolant, not by partial insertion of control rods (which would lead to asymmetric
   power distributions along the length of the fuel elements).  Now, set $x = 0$ and assume
   that $\Sigma_{\gamma}^m = N_H \sigma^H_{a} + N_O \sigma^O_{a} + N_B \sigma^B_{a}$.
   
    (a) What concentration (in parts-per-million or ppm) of ${}^{10}$B in the water is 
        needed to achieve criticality? Use cross sections listed in Table 3.2.
    (b) Without doing the calculation, predict how $\alpha_m$ changes from part (e) of Problem 22.1
        to part (a) of this problem.

 - [22.3] After several days at full power, we know that the concentration of 
   ${}^{135}$Xe reaches equilibrium values.  Assume that the thermal flux
   in our PWR at full power is $\phi = 3 \times 10^{13}$ 1/cm$^2$-s.

    (a) Determine the equilibrium concentration of ${}^{135}$Xe.
    (b) Compute the corresponding macroscopic cross section $\Sigma_{a}^{\text{fp}}$.
        Use cross sections listed in Table 3.2.
    (c) With $x = x_{\text{fp}}$, recompute $\rho$ with the equilibrium ${}^{135}$Xe.
        This reactivity is called the **equilibrium xenon worth**.
    (d) If the reactor were shutdown, the ${}^{135}$Xe concentration grows because it 
        is no longer being absorbed, peaks at 11.3 hours after shutdown, and 
        then diminishes with decay.  Repeat (c) with this peak concentration to 
        compute the **peak xenon worth**.
        Does our reactor have sufficient excess reactivity to go back to 
        full power?


 