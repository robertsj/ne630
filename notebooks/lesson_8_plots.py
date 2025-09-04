"""
Data preparation and plot generation for Lesson 8
"""

import numpy as np
import matplotlib.pyplot as plt
import glob 
from scipy.interpolate import interp1d 

N_A = 6.022e23 # Avogadro's number

def load_cross_sections(n=2e5):
    """ Load the cross sections for U-235, U-238, H-1, and O-16.  Place them
        on a single energy grid.
    """

    files = glob.glob("./cross_section_data/*.txt")

    E_grid = np.logspace(-3, 7, int(n))

    cross_section_data = {}
    cross_section_data["E"] = E_grid
    for file in files:
        nuclide_reaction = file.replace(".txt", "").replace("./cross_section_data/", "")
        
        E, v = np.loadtxt(file, skiprows=1, unpack=True, delimiter=",")
        f = interp1d(E, v, fill_value=(0.0, 0.0), bounds_error=False)
        v_grid = f(E_grid)
        cross_section_data[nuclide_reaction] = v_grid 

    return cross_section_data

def water(rho=1.0):
    data = load_cross_sections()

    N_O16 = rho * N_A / 18.0 
    N_H1  = 2 * rho * N_A / 18.0

    Sigma_S = N_O16 * (data["O16_e"]+data["O16_in"]) + N_H1 * data["H1_e"]
    Sigma_A = N_O16 * data["O16_g"] + N_H1 * data["H1_g"]

    return data["E"], Sigma_S, Sigma_A

def uo2(enrich=0.04, rho=10.0):
    data = load_cross_sections()

    U_mass= enrich*235+(1-enrich)*238
    N_U235 = rho * enrich * U_mass / (U_mass + 32) * N_A / 235
    N_U238 = rho * (1-enrich) * U_mass / (U_mass + 32) * N_A / 238
    N_O16 = rho * 32 / (U_mass + 32) * N_A / 16
    
    Sigma_S = N_O16 * (data["O16_e"]+data["O16_in"]) + \
              N_U235 * (data["U235_e"]+data["U235_in"]) + \
              N_U238 * (data["U238_e"]+data["U238_in"]) 
    Sigma_A = N_O16 * data["O16_g"] + \
              N_U235 * (data["U235_g"]+data["U235_f"]) + \
              N_U238 * (data["U238_g"]+data["U238_f"])
    nu_Sigma_F = N_U235 * (data["U235_nubar"]*data["U235_f"]) + \
                 N_U238 * (data["U238_nubar"]*data["U238_f"])
    
    return data["E"], Sigma_S, Sigma_A, nu_Sigma_F


if __name__ == "__main__":

    load_cross_sections()
    uo2()