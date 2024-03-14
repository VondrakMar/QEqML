from ase.io import read, write
import sys

mols = read(f"{sys.argv[1]}@:",format = "extxyz")

nMol = len(mol)
partTrain = float(sys.argv[2])
partVal = float(sys.argv[3])
partTest = float(sys.argv[4])



nTrain = int(partTrain*nMol)
nVal = int(partVal*nMol)
nTrain = int(partTrain*nMol)

train_set = mols[:nTrain]
val_set = mols[nTrain:nTrain+nVal]
test_set = mols[nTrain+nVal:nTrain+nVal+nTest]

print(len(train_set))
print(len(val_set))
print(len(test_set))
