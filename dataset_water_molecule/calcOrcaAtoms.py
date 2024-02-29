from ase.calculators.orca import ORCA
from ase.io import read, write

calc = ORCA(orcasimpleinput='B3LYP def2-TZVP',
            orcablocks='%pal nprocs 1 end')
for id_m,m in enumerate(mol):
    m.set_calculator(calc)
    en = m.get_potential_energy()
    f = m.get_forces()
    m.info["energy"] = en
    m.arrays["forces"] = f
    write(f"wat{id_m}.xyz",m
)

