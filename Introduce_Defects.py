import numpy as np
import matplotlib.pyplot as plt
import random

#Number of linkers to delete
N = 216 # number of linkers to delete (432 = 50% defect density)


i = 0
j = 0
input = open("HKUST-1_3x3x3.txt", "r")
for line in input:
    L = line.split()
    if len(L) == 8:
        i = i + 1
        if L[1] == "C":
            j = j + 1
input.close()
C = np.ones((j,3))
symbol = np.empty((j), dtype="S10")

input = open("HKUST-1_3x3x3.txt", "r")
a = 79.0290 # cell length in Angstrom
i = -1
j = -1

for line in input:
    L = line.split()
    if len(L) == 8:
        i = i + 1
        if L[1] == "C":
            j = j + 1
            symbol[j] = L[0]
            for k in range(3):
                C[j,k] = float(L[k+2])*a
input.close()

j = 7776
distance = 2.8
symbol3 = []
symbol6 = []
symbol7 = []
for n in range(j):
    p = 0
    for m in range(j):
        if m != n:
            rijx = C[n,0] - C[m,0]
            rijy = C[n,1] - C[m,1]
            rijz = C[n,2] - C[m,2]
            rij2 = rijx*rijx + rijy*rijy + rijz*rijz
            rij = np.sqrt(rij2)
            if rij < distance:
                p = p + 1
    if p == 3:
        symbol3.append(symbol[n])
    if p == 6:
        symbol6.append(symbol[n])
    if p == 7:
        symbol7.append(symbol[n])

j = 7776
distance = 2.8
list1 = []
list2 = []
for n in range(j):
    list1 = []
    list1.append(symbol[n])
    for m in range(j):
        if m != n:
            rijx = C[n,0] - C[m,0]
            rijy = C[n,1] - C[m,1]
            rijz = C[n,2] - C[m,2]
            rij2 = rijx*rijx + rijy*rijy + rijz*rijz
            rij = np.sqrt(rij2)
            if rij < distance:
                list1.append(symbol[m])
    list2.append(list1)


def grouper(sequence):
    result = []

    for item in sequence:
        for members, group in result:
            if members.intersection(item):
                members.update(item)
                group.append(item)
                break
        else:
            result.append((set(item), [item]))

    return [group for members, group in result]

output = list(grouper(list2))

i = -1
flatList = []
flatList1 = []
for elem in output:
    i = i + 1
    k = 0
    flatList = []
    for item in elem:
        k = k + 1
        if k<=9:
            flatList.extend(item)
    flatList1.append(flatList)

final_list = []
for elem in flatList1:
    my_list = list(dict.fromkeys(elem))
    final_list.append(my_list)

symbol3_list = []
symbol6_list = []
symbol7_list = []
delete1_list = []
delete_list = []
threeCarbon_list = []
for elem in final_list:

    symbol3_list = []
    symbol6_list = []
    symbol7_list = []

    delete1_list = []

    for item in elem:
        if item in symbol3:
            symbol3_list.append(item)
        if item in symbol6:
            symbol6_list.append(item)
        if item in symbol7:
            symbol7_list.append(item)
    delete1_list.extend(symbol7_list)
    delete1_list.extend(symbol6_list)
    delete_list.append(delete1_list)
    threeCarbon_list.extend(symbol3_list)


# Bond information

input = open("HKUST-1_3x3x3.txt", "r")
i = 0
k = -1
bond_list1 = []
bond_list2 = []
for line in input:
    i = i + 1
    if i >= 16879 :
        L = line.split()
        k = k + 1
        bond_list1.append(L[0])
        bond_list2.append(L[1])
input.close()

# convert threeCarbon_list to ASCII
threeCarbon_list2 = []

for elem in threeCarbon_list:
    u = elem.decode('UTF-8')
    threeCarbon_list2.append(u)

delete_list2 = []
delete_list_ASCII = []
for elem in delete_list:
    delete_list2 = []
    for item in elem:
        u = item.decode('UTF-8')
        delete_list2.append(u)
    delete_list_ASCII.append(delete_list2)

#generate random numbers
randomlist = random.sample(range(0, 864), N)


H1 = []
H3 = []
for num in randomlist:
    H2 = []
    c1 = delete_list_ASCII[num][0]
    c2 = delete_list_ASCII[num][1]
    c3 = delete_list_ASCII[num][2]
    for i in range(len(bond_list1)):
        if bond_list1[i] == c1:
            if bond_list2[i][0] == 'H':
                H1.append(bond_list2[i])
                H2.append(bond_list2[i])
        if bond_list1[i] == c2:
            if bond_list2[i][0] == 'H':
                H1.append(bond_list2[i])
                H2.append(bond_list2[i])
        if bond_list1[i] == c3:
            if bond_list2[i][0] == 'H':
                H1.append(bond_list2[i])
                H2.append(bond_list2[i])
    H3.append(H2)

delete_list_carbon = []
delete_list_forH = []
delete_list_H = []
for num in randomlist:
    delete_list_carbon.extend(delete_list_ASCII[num])
for num in randomlist:
    delete_list_forH = []
    delete_list_forH.append(delete_list_ASCII[num][3])
    delete_list_forH.append(delete_list_ASCII[num][4])
    delete_list_forH.append(delete_list_ASCII[num][5])
    delete_list_H.extend(delete_list_forH)

total_delete_list = delete_list_carbon + H1

# Write cif file with missing linker
i = 0
k = 0
with open("HKUST-1_3x3x3.txt") as input:
    lines = input.readlines()
    with open("missing_linkers.txt","w") as missing_linkers:
        for line in lines:
            L = line.split()
            i = i + 1
            if i < 25:
                missing_linkers.write(line)
            elif i >= 25 and i <= 16872:
                if not L[0] in total_delete_list:
                    missing_linkers.write(line)
            elif i > 16872 and i < 16879:
                    missing_linkers.write(line)
            elif i >= 16879 :
                if not L[0] in total_delete_list and not L[1] in total_delete_list:
                    missing_linkers.write(line)
                    k = k + 1

Cxyz = np.ones((3*len(randomlist),3))
input = open("HKUST-1_3x3x3.txt", "r")

for line in input:
    l = line.split()
    if len(L) == 8:
        for i in range(len(delete_list_H)):
                if L[0] == delete_list_H[i]:
                    for k in range(3):
                        Cxyz[i,k] = float(L[k+2])
input.close()

# add hydrogens

with open("added_H.txt","w") as added_H_xyz:
    for i in range (len(H1)):
            added_H_xyz.write(
            H1[i] + "     " + "H" + "     " + str(Cxyz[i][0]) + "   "
            + str(Cxyz[i][1]) + "   " + str(Cxyz[i][2]) + "   "
            + "0.0000" + "   " + "Uiso" + "   " + "1.0" + "\n")

# adding bonds with hydrogen

C_H = []
for i in delete_list_H:
    for j in range(len(bond_list1)):
        if bond_list1[j] == i:
            if bond_list2[j] in threeCarbon_list2:
                C_H.append(bond_list2[j])
        if bond_list2[j] == i:
            if bond_list1[j] in threeCarbon_list2:
                C_H.append(bond_list1[j])

with open("added_bonds_H.txt","w") as added_bonds_withH:
    for i in range (len(H1)):
            added_bonds_withH.write(
            C_H[i] + "   " + H1[i] + "  " + str("1.498")
            + "   " + str(".") + "     " + str("S") + "\n")

#Combining all text files into one
i = 0
input = open("missing_linkers.txt", "r")
for line in input:
    L = line.split()
    if len(L) == 8:
        i = i + 1
input.close()

n = 0
input = open("missing_linkers.txt", "r")
for line in input:
    L = line.split()
    if len(L) == 5:
        n = n + 1
input.close()

k = 0
input = open("added_H.txt", "r")
for line in input:
    k = k + 1
input.close()

m = 0
input = open("added_bonds_H.txt", "r")
for line in input:
    m = m + 1
input.close()

j = 0
k = 0
with open("missing_linkers.txt") as input:
    lines = input.readlines()
    with open("missing_linkers_final.txt","w") as missing_linkers:
        for line in lines:
            j = j + 1
            if j < 25 + i:
                missing_linkers.write(line)
            elif j >= 25 + i and j < 31 + i:
                if j == 25 + i:
                    input = open("added_H.txt", "r")
                    for line1 in input:
                        missing_linkers.write(line1)
                missing_linkers.write(line)
            elif j >= 31 + i:
                missing_linkers.write(line)
                if j == 30 + i + n:
                    missing_linkers.write("\n")
                    input = open("added_bonds_H.txt", "r")
                    for line2 in input:
                        missing_linkers.write(line2)
