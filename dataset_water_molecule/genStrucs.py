from ase.build import molecule
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io.trajectory import Trajectory
import ase.io
from ase import Atoms, Atom
from ase import units
h2o = molecule("H2O")
calc = EMT()

T = 300  # Kelvin
h2o.set_calculator(calc)
dyn = Langevin(h2o, 1 * units.fs, T * units.kB, 0.0002)
traj = Trajectory('h2o_emt.traj', 'w', h2o)
dyn.attach(traj.write, interval=5)
dyn.run(600)  
