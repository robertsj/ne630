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
        assert fuel_radius < clad_radius
        assert clad_radius < pitch/2
        self.r_fuel = fuel_radius
        self.r_clad = clad_radius
        self.pitch = pitch 
        self.shape = shape 
        self.T_cool = T_cool
        self.T_fuel = T_fuel
        self.group_bounds = group_bounds 

        self.setup_materials()
        self.setup_geometry()

    def display(self, fmt=""):
        print("lattice type: ", self.shape)
        print(" fuel radius: ", self.r_fuel)
        print(" clad radius: ", self.r_clad)

    def run(self, ng=10, np=10000):
        self.num_generations=ng
        self.num_particles=np
        self.setup_settings()
        self.setup_tallies()
        #openmc.run()
        # process tallies
        self.process_tallies()

    def setup_tallies(self):
        
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
        self.nu_fission_fuel = mgxs.FissionXS(domain=self.fuel_cell, energy_groups=groups, nu=True)
        self.scattering_fuel = mgxs.ScatterMatrixXS(domain=self.fuel_cell, energy_groups=groups)
        self.scattering_clad = mgxs.ScatterMatrixXS(domain=self.clad_cell, energy_groups=groups)
        self.scattering_cool = mgxs.ScatterMatrixXS(domain=self.cool_cell, energy_groups=groups)
        self.chi = mgxs.Chi(domain=self.fuel_cell, energy_groups=groups)
        tallies += self.absorption_fuel.tallies.values()
        tallies += self.absorption_clad.tallies.values()
        tallies += self.absorption_cool.tallies.values()
        tallies += self.nu_fission_fuel.tallies.values()
        tallies += self.scattering_fuel.tallies.values()
        tallies += self.scattering_clad.tallies.values()
        tallies += self.scattering_cool.tallies.values()
        tallies += self.chi.tallies.values() 
        tallies.export_to_xml() 

    def process_tallies(self):
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
        self.nu_fission_fuel.load_from_statepoint(sp)
        self.scattering_fuel.load_from_statepoint(sp)
        self.scattering_clad.load_from_statepoint(sp) 
        self.scattering_cool.load_from_statepoint(sp)
        self.chi.load_from_statepoint(sp)
        # Close the statepoint file now that we're done getting info
        sp.close()

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

    def setup_settings(self):
        # Use 1 MeV point source at the origin as the starting source
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

    def setup_materials(self):
        # Materials
        self.init_materials()
        self.fuel.temperature = self.T_fuel
        self.coolant.temperature = self.T_cool
        self.cladding.temperature = self.T_fuel*0.2 + self.T_cool*0.8
        # the user can override this before running
        materials = openmc.Materials([self.fuel, self.coolant, self.cladding])
        materials.export_to_xml()

    def setup_geometry(self):
        # surfaces and cell volume
        fuel_surface = openmc.ZCylinder(r=self.r_fuel)
        clad_surface = openmc.ZCylinder(r=self.r_clad)
        if self.shape == "box":
            self.volume = self.pitch**2
            outer_surface = openmc.rectangular_prism(
                width=self.pitch, 
                height=self.pitch,
                boundary_type='reflective')  
        else:
            s = self.pitch/np.sqrt(3)
            self.volume = 3*np.sqrt(3)*s**2/2 
            outer_surface = openmc.model.hexagonal_prism(
                edge_length=s,
                orientation='x',
                boundary_type='reflective')
            
        # volume fractions
        self.vf_fuel = np.pi*self.r_fuel**2/self.volume
        self.vf_clad = np.pi*(self.r_clad**2-self.r_fuel**2)/self.volume
        self.vf_cool = 1 - self.vf_fuel - self.vf_clad

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

    def plot(self):
        self.root_universe.plot(width=[1.1*self.pitch, 1.1*self.pitch])


    def init_materials(self):
        raise NotImplementedError
    
    def init_tallies(self):
        raise NotImplementedError

class LWRUnitCell(UnitCell):

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