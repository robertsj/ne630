import numpy as np
import matplotlib.pyplot as plt
import openmc
import openmc.mgxs as mgxs

class UnitCell:
    """A UnitCell represents a typical fuel element comprised of
       a cylindrical fuel pin surrounded by a thin cladding in
       a box or hex of coolant.
    """
    
    def __init__(self, fuel_radius, clad_radius, pitch, shape, T_cool, T_fuel, group_bounds):
        """Initialize a UnitCell.

        Args:
            fuel_radius (float): Radius of the fuel pin [cm]
            clad_radius (float): Outer radius of the cladding [cm]
            pitch (float): Unit-cell pitch, i.e., the distance between fuel centers [cm]
            shape (str): Either "box" or "hex"
            T_cool (float): Coolant temperature [K]
            T_fuel (float): Fuel temperature [K]
            group_bounds (np.array): Energy group boundaries for cross-section generation [eV].
        """
        assert fuel_radius < clad_radius
        assert clad_radius < pitch/2
        self.r_fuel = fuel_radius
        self.r_clad = clad_radius
        self.pitch = pitch 
        self.shape = shape 
        self.T_cool = T_cool
        self.T_fuel = T_fuel
        self.group_bounds = group_bounds 

        self._setup_materials()
        self._setup_geometry()

    def plot(self):
        """Plot the unit-cell geometry.
        """
        self.root_universe.plot(width=[1.1*self.pitch, 1.1*self.pitch])

    def run(self, ng=10, np=10000):
        """Run the simulation needed to generate the fluxes and cross sections.

        The number of generations is the *total* number simulated, but 5 are always "inactive.

        Args:
            ng (int, optional): Number of fission generations. Defaults to 10.
            np (int, optional): Number of particles per generation. Defaults to 10000.
        """
        self.num_generations=ng
        self.num_particles=np
        self._setup_settings()
        self._setup_tallies()
        openmc.run()

        # process tallies
        self._process_tallies()

        # Process group cross sections into the three regions and into 
        # a fourth "non-fuel" region.
        self._compute_group_constants()

    def plot_spectrum(self, per_unit_lethargy=False):
        if per_unit_lethargy:
            f = 0.5*(self.spectrum_group_bounds[1:]+self.spectrum_group_bounds[:-1])
        else:
            f = 1.0
        plt.stairs(f*self.spectrum_fuel, self.spectrum_group_bounds, color='k', lw=0.1, label='fuel')
        plt.stairs(f*self.spectrum_clad, self.spectrum_group_bounds, color='b', lw=0.1, label='cladding')
        plt.stairs(f*self.spectrum_cool, self.spectrum_group_bounds, color='r', lw=0.1, label='coolant')
        plt.xlabel('$E$ (eV)')
        ylab = "$E\phi(E)$" if per_unit_lethargy else "$\phi(E)$"
        plt.ylabel(ylab)
        plt.legend()
        plt.xscale('log')
        if not per_unit_lethargy:
            plt.yscale('log')
        plt.show()

    def _setup_materials(self):
        """Setup material definitions.
        """
        # Materials
        self._init_materials() # this must be implemented in the derived class.
        self.fuel.temperature = self.T_fuel
        self.coolant.temperature = self.T_cool
        self.cladding.temperature = self.T_fuel*0.2 + self.T_cool*0.8 # a modeling assumption!
        # the user can override this before running
        materials = openmc.Materials([self.fuel, self.coolant, self.cladding])
        materials.export_to_xml()

    def _setup_geometry(self):
        # surfaces and cell volume
        fuel_surface = openmc.ZCylinder(r=self.r_fuel)
        clad_surface = openmc.ZCylinder(r=self.r_clad)
        if self.shape == "box":
            self.cell_volume = self.pitch**2
            outer_surface = openmc.rectangular_prism(
                width=self.pitch, 
                height=self.pitch,
                boundary_type='reflective')  
        else:
            s = self.pitch/np.sqrt(3)
            self.cell_volume = 3*np.sqrt(3)*s**2/2 
            outer_surface = openmc.model.hexagonal_prism(
                edge_length=s,
                orientation='x',
                boundary_type='reflective')
            
        # volumes and volume fractions
        self.vf_fuel = np.pi*self.r_fuel**2/self.cell_volume
        self.vf_clad = np.pi*(self.r_clad**2-self.r_fuel**2)/self.cell_volume
        self.vf_cool = 1 - self.vf_fuel - self.vf_clad
        self.volume = {} 
        self.volume["fuel"] = self.vf_fuel * self.cell_volume
        self.volume["clad"] = self.vf_clad * self.cell_volume
        self.volume["cool"] = self.vf_cool * self.cell_volume
        self.volume["non-fuel"] = self.volume["clad"] + self.volume["cool"]

        # regions and cells
        fuel_region = -fuel_surface
        clad_region = +fuel_surface & -clad_surface
        cool_region = +clad_surface & outer_surface    

        self.fuel_cell = openmc.Cell(name='fuel')
        self.fuel_cell.fill = self.fuel
        self.fuel_cell.region = fuel_region
        self.clad_cell = openmc.Cell(name='cladding')
        self.clad_cell.fill = self.cladding
        self.clad_cell.region = clad_region
        self.cool_cell = openmc.Cell(name='coolant')
        self.cool_cell.fill = self.coolant
        self.cool_cell.region = cool_region

        self.root_universe = openmc.Universe(cells=(self.fuel_cell, self.clad_cell, self.cool_cell))
        geometry = openmc.Geometry()
        geometry.root_universe = self.root_universe
        geometry.export_to_xml()

    def _setup_settings(self):
        point = openmc.stats.Point((0, 0, 0))
        source = openmc.IndependentSource(space=point)
        source.angle = openmc.stats.Isotropic()
        source.energy = openmc.stats.Watt()
        settings = openmc.Settings()
        settings.batches = self.num_generations
        settings.inactive = 5
        settings.particles = self.num_particles
        settings.run_mode = 'eigenvalue'
        settings.temperature = {"method": "interpolation"}
        settings.export_to_xml()

    def _setup_tallies(self):
        """Setup tallies for the spectrum and for the multigroup cross sections.
        """
        
        # spectrum tally uses the lower and upper group bounds with many more divisions
        lower, upper = np.log10(self.group_bounds[0]), np.log10(self.group_bounds[-1])
        self.spectrum_group_bounds = np.logspace(lower, upper, 10000)
        self.spectrum_filter = openmc.EnergyFilter(self.spectrum_group_bounds)
        self.cell_filter = openmc.CellFilter([self.fuel_cell, self.clad_cell, self.cool_cell])
        spectrum_tally = openmc.Tally(1)
        spectrum_tally.filters = [self.cell_filter, self.spectrum_filter]
        spectrum_tally.scores = ['flux']
        tallies = openmc.Tallies([spectrum_tally])

        # two group cross sections
        groups = mgxs.EnergyGroups(self.group_bounds)
        self.absorption_fuel = mgxs.AbsorptionXS(domain=self.fuel_cell, energy_groups=groups)
        self.absorption_clad = mgxs.AbsorptionXS(domain=self.clad_cell, energy_groups=groups)
        self.absorption_cool = mgxs.AbsorptionXS(domain=self.cool_cell, energy_groups=groups)
        self.fission_fuel = mgxs.FissionXS(domain=self.fuel_cell, energy_groups=groups, nu=False)
        self.nu_fission_fuel = mgxs.FissionXS(domain=self.fuel_cell, energy_groups=groups, nu=True)
        self.scattering_fuel = mgxs.ScatterMatrixXS(domain=self.fuel_cell, energy_groups=groups)
        self.scattering_clad = mgxs.ScatterMatrixXS(domain=self.clad_cell, energy_groups=groups)
        self.scattering_cool = mgxs.ScatterMatrixXS(domain=self.cool_cell, energy_groups=groups)
        self.chi = mgxs.Chi(domain=self.fuel_cell, energy_groups=groups)
        tallies += self.absorption_fuel.tallies.values()
        tallies += self.absorption_clad.tallies.values()
        tallies += self.absorption_cool.tallies.values()
        tallies += self.fission_fuel.tallies.values()
        tallies += self.nu_fission_fuel.tallies.values()
        tallies += self.scattering_fuel.tallies.values()
        tallies += self.scattering_clad.tallies.values()
        tallies += self.scattering_cool.tallies.values()
        tallies += self.chi.tallies.values() 
        tallies.export_to_xml() 

    def _process_tallies(self):
        fname = 'statepoint.{}.h5'.format(self.num_generations)
        print("loading tallies from " + fname)
        sp = openmc.StatePoint(fname)

        # Load the spectrum
        phi = sp.get_tally().mean.reshape((3,len(self.spectrum_group_bounds)-1)).T
        dE = np.diff(self.spectrum_group_bounds)
        self.spectrum_fuel = phi[:, 0]/dE
        self.spectrum_clad = phi[:, 1]/dE
        self.spectrum_cool = phi[:, 2]/dE

        # Load the tallies from the statepoint into each MGXS object
        self.absorption_fuel.load_from_statepoint(sp)
        self.absorption_clad.load_from_statepoint(sp)
        self.absorption_cool.load_from_statepoint(sp)
        self.fission_fuel.load_from_statepoint(sp)
        self.nu_fission_fuel.load_from_statepoint(sp)
        self.scattering_fuel.load_from_statepoint(sp)
        self.scattering_clad.load_from_statepoint(sp) 
        self.scattering_cool.load_from_statepoint(sp)
        self.chi.load_from_statepoint(sp)

        # Close the statepoint file now that we're done getting info
        sp.close()

    def _compute_group_constants(self):
        """Use the loaded cross sections to define easy-to-access arrays for each region.
        """

        self.SigmaF = {"fuel": self.fission_fuel.get_xs()}
        self.nuSigmaF = {"fuel": self.nu_fission_fuel.get_xs()}
        self.nu = {"fuel": self.nu_fission_fuel.get_xs()/self.fission_fuel.get_xs()}

        self.SigmaA = {}
        self.SigmaA["fuel"] =  self.absorption_fuel.get_xs()
        self.SigmaA["clad"] =  self.absorption_clad.get_xs()
        self.SigmaA["cool"] =  self.absorption_cool.get_xs()

        self.SigmaS = {}
        self.SigmaS["fuel"] =  self.scattering_fuel.get_xs()
        self.SigmaS["clad"] =  self.scattering_clad.get_xs()
        self.SigmaS["cool"] =  self.scattering_cool.get_xs()

        # OpenMC fluxes are integrated over volume (because region-wise 
        # volumes are not always explicitly known)
        self.flux = {} 
        self.flux["fuel"] = self.absorption_fuel.get_flux()/self.volume["fuel"]
        self.flux["clad"] = self.absorption_clad.get_flux()/self.volume["clad"]
        self.flux["cool"] = self.absorption_cool.get_flux()/self.volume["cool"]

        # compute the non-fuel values by equating reaction rates, i.e., 
        #   V_NF * phi_NF * Sigma_NF = V_clad*phi_clad*Sigma_clad + V_cool*phi_cool*Sigma_cool
        self.flux['non-fuel'] = (self.flux['cool']*self.volume['cool'] +    \
                                 self.flux['clad']*self.volume['clad']) /   \
                                (self.volume['cool']+self.volume['clad'])
        
        self.SigmaA['non-fuel'] = \
            (self.SigmaA["cool"]*self.flux['cool']*self.volume['cool'] +    \
             self.SigmaA["clad"]*self.flux['clad']*self.volume['clad']) /   \
                 (self.flux["non-fuel"]*self.volume["non-fuel"])
        
        self.SigmaS['non-fuel'] = np.zeros_like(self.SigmaS["cool"])

        for g in range(0, len(self.group_bounds)-1):
            self.SigmaS["non-fuel"][g, :] = \
                (self.SigmaS["cool"][g, :]*self.flux['cool']*self.volume['cool'] +    \
                 self.SigmaS["clad"][g, :]*self.flux['clad']*self.volume['clad']) /   \
                (self.flux["non-fuel"]*self.volume["non-fuel"])

    def _init_materials(self):
        raise NotImplementedError


class LWRUnitCell(UnitCell):

    def __init__(self, fuel_radius=0.45, clad_radius=0.47, pitch=1.2, T_cool=600, T_fuel=1200, 
                 group_bounds=np.array([1e-3, 1.0, 1e7]),
                 enrichment=4.0, pressure=15.5, boron_ppm=0.0):
        """Create a light-water reactor unit cell.  Defaults to typical PWR values.

        Args:
            fuel_radius (float, optional): _description_. Defaults to 0.45.
            clad_radius (float, optional): _description_. Defaults to 0.47.
            pitch (float, optional): _description_. Defaults to 1.2.
            T_cool (int, optional): Coolant (water) temperature [K]. Defaults to 600.
            T_fuel (int, optional): Fuel temperature [K]. Defaults to 1200.
            group_bounds (np.array, optional): Group bounds for cross sections [eV]. Defaults to np.array([1e-3, 1.0, 1e7]).
            enrichment (float, optional): Uranium enrichment [%]. Defaults to 4.0.
            pressure (float, optional): Coolant (water) pressure [MPa]. Defaults to 15.5.
            boron_ppm (float, optional): Coolant boron concentration [ppm]. Defaults to 0.0.
        """
        self.enrichment = enrichment
        self.pressure = pressure
        self.boron_ppm = boron_ppm
        self.spectrum_group_bounds = np.logspace(-3, np.log10(2.5e7), 10000)

        super().__init__(fuel_radius, clad_radius, pitch, "box", T_cool, T_fuel, group_bounds)
    
    def _init_materials(self):
        """Initializes materials for a light-water reactor.
        """
        uo2 = openmc.Material(name="uo2")
        uo2.add_element('U', 1.0, enrichment=self.enrichment)
        uo2.add_element('O', 2.0)
        uo2.set_density('g/cc', 10.0)

        zirconium = openmc.Material(name="zirconium")
        zirconium.add_element('Zr', 1.0)
        zirconium.set_density('g/cc', 6.6)

        water = openmc.model.borated_water(boron_ppm=self.boron_ppm, 
                                           temperature=self.T_cool, 
                                           pressure=self.pressure, 
                                           temp_unit='K', 
                                           press_unit='MPa')

        self.fuel = uo2 
        self.cladding = zirconium 
        self.coolant = water



class SFRUnitCell(UnitCell):

    def __init__(self, fuel_radius, clad_radius, pitch, T_cool=600, T_fuel=1200, 
                 group_bounds=np.array([1e-3, 1.0, 1e7]),
                 enrichment=4.0, pressure=15.5):
        self.enrichment = enrichment
        self.pressure = pressure

        self.spectrum_group_bounds = np.logspace(-3, np.log10(2.5e7), 10000)

        super().__init__(fuel_radius, clad_radius, pitch, "box", T_cool, T_fuel, group_bounds)
    
    def init_materials(self):
        uo2 = openmc.Material(name="uo2")
        uo2.add_element('U', 1.0, enrichment=self.enrichment)
        uo2.add_element('O', 2.0)
        uo2.set_density('g/cc', 10.0)

        zirconium = openmc.Material(name="zirconium")
        zirconium.add_element('Zr', 1.0)
        zirconium.set_density('g/cc', 6.6)

        water = openmc.model.borated_water(0.0, 
                                           temperature=self.T_cool, 
                                           pressure=self.pressure, 
                                           temp_unit='K', 
                                           press_unit='MPa')

        self.fuel = uo2 
        self.cladding = zirconium 
        self.coolant = water

if __name__ == "__main__":

    a = LWRUnitCell(0.45, 0.47, 1.2)
    a.display()
    a.plot()