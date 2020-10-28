import numpy as np
import matplotlib.pyplot as plt
import random
import re
input = open("missing_linkers_final.txt", 'r')
i = 0
for line in input:
    cif_line = line.split()
    if len(cif_line) == 8:
        i += 1
natoms = i                               # number of atoms
input.close()
input = open("missing_linkers_final.txt", 'r')
i = 0
for line in input:
    cif_line = line.split()
    if len(cif_line) == 5:
        i += 1
nbonds = i                               # number of bonds
input.close()

atoms_index = [0] * natoms
input = open("missing_linkers_final.txt", 'r')
j = -1
for line in input:
    cif_line = line.split()
    if len(cif_line) == 8:
        j += 1
        temp = re.compile("([a-zA-Z]+)([0-9]+)")
        s = temp.match(cif_line[0]).groups()
        atoms_index[j] = int(float(s[1]))
input.close()

atoms_index_new = [0] * natoms
for i in range(len(atoms_index)):
    atoms_index_new[i] = i + 1

bond_1 = [0] * nbonds
bond_2 = [0] * nbonds
input = open("missing_linkers_final.txt", 'r')
j = -1
for line in input:
    cif_line = line.split()
    if len(cif_line) == 5:
        j += 1
        temp = re.compile("([a-zA-Z]+)([0-9]+)")
        s1 = temp.match(cif_line[0]).groups()
        s2 = temp.match(cif_line[1]).groups()
        bond_1[j] = int(float(s1[1]))
        bond_2[j] = int(float(s2[1]))
input.close()

i = -1
bond_1_new = [0] * nbonds
bond_2_new = [0] * nbonds
for k in range(len(bond_1)):
    for i in range(len(atoms_index)):
        if bond_1[k] == atoms_index[i]:
            bond_1_new[k] = i + 1
        if bond_2[k] == atoms_index[i]:
            bond_2_new[k] = i + 1

atoms_symbols = [0] * natoms
input = open("missing_linkers_final.txt", 'r')
j = -1
for line in input:
    cif_line = line.split()
    if len(cif_line) == 8:
        j += 1
        atoms_symbols[j] = str(cif_line[1])
input.close()

i = -1
bond_1_symbols = [0] * nbonds
bond_2_symbols = [0] * nbonds
for k in range(len(bond_1)):
    for i in range(len(atoms_index)):
        if bond_1[k] == atoms_index[i]:
            bond_1_symbols[k] = atoms_symbols[i]
        if bond_2[k] == atoms_index[i]:
            bond_2_symbols[k] = atoms_symbols[i]

i = -1
j = -1
k = 0
with open("missing_linkers_final.txt") as input:
    lines = input.readlines()
    with open("missing_linkers_renumbered.cif","w") as missing_linkers:
        for line in lines:
            cif_line = line.split()
            k += 1
            if k < 25:
                missing_linkers.write(line)
            elif k >= 25 and k < 25 + natoms:
                if len(cif_line) == 8:
                    i += 1
                    missing_linkers.write(
                        cif_line[1] + str(atoms_index_new[i]) + "   " + cif_line[1] + "   "
                        + cif_line[2] + "   " + cif_line[3] + "   " + cif_line[4] + "   "
                        + cif_line[5] + "   " + cif_line[6] + "   " + cif_line[7] + "\n")
            elif k >= 25 + natoms and k < 31 + natoms:
                    missing_linkers.write(line)
            elif k >= 31 + natoms:
                if len(cif_line) == 5:
                    j += 1
                    missing_linkers.write(
                    bond_1_symbols[j] + str(bond_1_new[j]) + "   " +
                    bond_2_symbols[j] + str(bond_2_new[j]) + "   " +
                    cif_line[2] + "   " + cif_line[3] + "   " + cif_line[4] + "\n")

