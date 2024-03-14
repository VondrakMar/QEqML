from ase.io import read, write
import sys

mols = read(f"{sys.argv[1]}@:",format = "extxyz")

nMol = len(mols)
partTrain = float(sys.argv[2])
partVal = float(sys.argv[3])
partTest = float(sys.argv[4])



nTrain = int(partTrain*nMol)
nVal = int(partVal*nMol)
nTest = int(partTest*nMol)

train_set = mols[:nTrain]
val_set = mols[nTrain:nTrain+nVal]
test_set = mols[nTrain+nVal:nTrain+nVal+nTest]

if len(train_set) > 0:
    write("train_set.xyz",train_set)
if len(val_set) > 0:
    write("val_set.xyz",val_set)
if len(test_set) > 0:
    write("test_set.xyz",test_set)
