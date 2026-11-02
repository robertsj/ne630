# Model snapshot from notebooks/lesson_19.ipynb, code cells 2 and 4.
# Notebook SHA256: d51136a6fe47be0817432889df3160342f567c3c43b496b0603b0ce8717ffabb
# Only the model builder is retained; no notebook calculations execute on import.
import os
import tempfile
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import openmc
import pandas as pd

cross_sections = os.environ.get("OPENMC_CROSS_SECTIONS")
if not cross_sections or not Path(cross_sections).is_file():
    raise RuntimeError(
        "Set OPENMC_CROSS_SECTIONS to an installed OpenMC "
        "continuous-energy cross_sections.xml file."
    )
openmc.config["cross_sections"] = cross_sections

REGION_NAMES = ("fuel", "cladding", "coolant")

PITCH = 1.1897       # cm, nearest-neighbor pin pitch
FUEL_RADIUS = 0.4742 # cm
CLAD_RADIUS = 0.5419 # cm
CELL_HEIGHT = 1.0    # cm
HEX_SIDE = PITCH / np.sqrt(3.0)
CELL_AREA = np.sqrt(3.0) * PITCH**2 / 2.0

VOLUMES = np.array(
    [
        np.pi * FUEL_RADIUS**2 * CELL_HEIGHT,
        np.pi * (CLAD_RADIUS**2 - FUEL_RADIUS**2) * CELL_HEIGHT,
        (CELL_AREA - np.pi * CLAD_RADIUS**2) * CELL_HEIGHT,
    ]
)
VOLUME_FRACTIONS = VOLUMES / VOLUMES.sum()

U235_MASS = openmc.data.atomic_mass("U235")
U238_MASS = openmc.data.atomic_mass("U238")


def uranium_atom_fraction_from_weight_fraction(weight_fraction):
    n_235 = weight_fraction / U235_MASS
    n_238 = (1.0 - weight_fraction) / U238_MASS
    return n_235 / (n_235 + n_238)


def uranium_weight_fraction_from_atom_fraction(atom_fraction):
    m_235 = atom_fraction * U235_MASS
    m_238 = (1.0 - atom_fraction) * U238_MASS
    return m_235 / (m_235 + m_238)


LESSON16_ENRICHMENT_WEIGHT_FRACTION = 0.15
LESSON16_ENRICHMENT_ATOM_FRACTION = (
    uranium_atom_fraction_from_weight_fraction(
        LESSON16_ENRICHMENT_WEIGHT_FRACTION
    )
)

TEMPERATURE = 294.0  # K
SPECTRUM_EDGES = np.geomspace(1.0e2, 2.0e7, 121)  # eV
SPECTRUM_CENTERS = np.sqrt(SPECTRUM_EDGES[:-1] * SPECTRUM_EDGES[1:])
DELTA_U = np.log(SPECTRUM_EDGES[1:] / SPECTRUM_EDGES[:-1])

NONLEAKAGE_PROBABILITY = 0.90
TARGET_K_INFINITY = 1.0 / NONLEAKAGE_PROBABILITY

CLADDING_COMPOSITION = {
    "C": 3.5740e-4,
    "O": 3.9924e-4,
    "Ti": 5.3824e-4,
    "Cr": 1.7753e-2,
    "Fe": 5.3872e-2,
    "Ni": 3.6588e-4,
    "Mn": 2.3441e-4,
    "P": 2.7718e-5,
    "Al": 9.1482e-3,
    "Co": 2.1852e-4,
    "Cu": 1.0135e-4,
    "Y": 2.6616e-4,
}

PURPLE = "#512888"
ORANGE = "#CA7C1B"
TEAL = "#008080"


def build_sfr_model(
    *,
    enrichment=LESSON16_ENRICHMENT_ATOM_FRACTION,
    particles=1600,
    batches=50,
    inactive=10,
    seed=19001,
    include_spectrum=False,
):
    '''Build the explicit-region Lesson 16 SFR unit cell.'''
    if not 0.0 < enrichment < 1.0:
        raise ValueError("enrichment must be an atom fraction in (0, 1)")
    if not 0 < inactive < batches:
        raise ValueError("require 0 < inactive < batches")

    fuel = openmc.Material(name="UO2 fuel")
    fuel.add_nuclide("U235", enrichment)
    fuel.add_nuclide("U238", 1.0 - enrichment)
    fuel.add_element("O", 2.0)
    fuel.set_density("g/cm3", 10.5)
    fuel.temperature = TEMPERATURE

    cladding = openmc.Material(name="ODS steel cladding")
    for element, amount in CLADDING_COMPOSITION.items():
        cladding.add_element(element, amount, "ao")
    cladding.set_density("g/cm3", 7.13)
    cladding.temperature = TEMPERATURE

    coolant = openmc.Material(name="sodium coolant")
    coolant.add_nuclide("Na23", 1.0)
    coolant.set_density("g/cm3", 0.837)
    coolant.temperature = TEMPERATURE

    fuel_surface = openmc.ZCylinder(r=FUEL_RADIUS)
    clad_surface = openmc.ZCylinder(r=CLAD_RADIUS)
    outer_surface = openmc.model.HexagonalPrism(
        edge_length=HEX_SIDE,
        orientation="x",
        boundary_type="reflective",
    )
    z_min = openmc.ZPlane(z0=-CELL_HEIGHT / 2.0, boundary_type="reflective")
    z_max = openmc.ZPlane(z0=+CELL_HEIGHT / 2.0, boundary_type="reflective")
    axial_region = +z_min & -z_max
    prism = -outer_surface & axial_region

    cells = (
        openmc.Cell(
            name="fuel", fill=fuel, region=-fuel_surface & axial_region
        ),
        openmc.Cell(
            name="cladding",
            fill=cladding,
            region=+fuel_surface & -clad_surface & axial_region,
        ),
        openmc.Cell(
            name="coolant", fill=coolant, region=+clad_surface & prism
        ),
    )
    for cell, volume in zip(cells, VOLUMES, strict=True):
        cell.volume = float(volume)

    settings = openmc.Settings(run_mode="eigenvalue")
    settings.batches = int(batches)
    settings.inactive = int(inactive)
    settings.particles = int(particles)
    settings.seed = int(seed)
    settings.source = openmc.IndependentSource(
        space=openmc.stats.Point((0.0, 0.0, 0.0)),
        angle=openmc.stats.Isotropic(),
        energy=openmc.stats.Discrete([2.0e6], [1.0]),
    )
    settings.temperature = {"method": "interpolation"}

    cell_filter = openmc.CellFilter(cells)
    rates = openmc.Tally(name="regional one-group rates")
    rates.filters = [cell_filter]
    rates.scores = ["flux", "absorption", "nu-fission"]
    tallies = [rates]

    if include_spectrum:
        spectrum = openmc.Tally(name="regional spectrum")
        spectrum.filters = [
            cell_filter,
            openmc.EnergyFilter(SPECTRUM_EDGES),
        ]
        spectrum.scores = ["flux"]
        tallies.append(spectrum)

    model = openmc.Model(
        geometry=openmc.Geometry(cells),
        materials=openmc.Materials([fuel, cladding, coolant]),
        settings=settings,
        tallies=openmc.Tallies(tallies),
    )
    return model


