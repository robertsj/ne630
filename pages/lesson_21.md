# Lesson 21

<!--


-->

## Learning Objectives

### Macro Objectives


Students will be able to quantify the impact of temperature, density, and 
other factors on reactivity.


### Micro Objectives

 - Explain the relationship between reactivity and the multiplication factor.
 - Explain why the fuel temperature coefficient (FTC) is usually strongly negative.
 - Explain how the moderator (or coolant) temperature coefficient (MTC) depends on geometry.
 - Explain how the fuel and coolant temperature coefficients for a sodium-cooled fast reactor differ from 
   those of a light-water reactor.
 - Describe how excess reactivity is balanced by the introduction of control (i.e., neutron "poisons")

## Key Terms

 - reactivity
 - units of reactivity: dollars and cents; $\Delta k/k$; percent-milli (pcm)
 - fuel temperature coefficient (FTC)
 - moderator (or coolant) temperature coefficient (MTC) 
 - power coefficient of reactivity (PCR)
 - isothermal temperature coefficient
 - power defect
 - excess reactivity
 - shutdown margin
 - cold shutdown
 - cold critical
 - hot zero power
 - full power
 - control


## Before Lecture

  - Read 9.1-9.4
  - Read [this article](https://k-state.primo.exlibrisgroup.com/discovery/fulldisplay?docid=cdi_proquest_miscellaneous_743559653&context=PC&vid=01KSU_INST:NewUI&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,What%20killed%20the%20Maples%20reactors%3F&mode=Basic) on how a discrepancy between the predicted and measured power coefficient of reactivity (PCR) for the MAPLE
  reactors led to their permanent shutdown.


## After Lecture

### Homework

  - Problem 9.1.
  - Use `SFRUnitCell` to estimate the fuel and coolant temperature coefficients of reactivity
    at the default conditions of $T_f = 900$ K and $T_c = 500$ K based on a *finite difference*
    approximation.  To ensure that the uncertainty in the computed coefficients are negligible,
    set the number of particles in the `run` function to one million.  How do these coefficients
    compare to the PWR coefficients at nominal full-power conditions (i.e., $T_f = 900$ K and 
    $T_c = 300$ K)?

