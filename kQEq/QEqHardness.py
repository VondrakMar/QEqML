import sys
sys.path.append("/datavon1/dev_qpac_fitting_forces/qpac/")
from ase.units import Bohr,Hartree
from ase.io import read
import numpy as np
from qpac.qeq import charge_eq
from qpac.utils import addPeriodicity

mol = read("W6.xyz",format="extxyz")
qe = charge_eq(mol,radius_type="rcov",periodic=False)
A = qe.get_A()
print(A*Hartree)