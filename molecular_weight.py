# molecular_weight.py
# Determines the molecular weight of a compund, 
# given the molecular formula.

import math

def main():
    print("This program determines the molecular weight of a molecule.")
    print()

    carbons = eval(input("How many carbons: "))
    hydrogens = eval(input("How many hydrogens: "))
    nitrogens = eval(input("How many nitrogens: "))

    c_weight = 12.011
    h_weight = 1.0079
    n_weight = 15.9994

    molecular_weight = carbons * c_weight + hydrogens * h_weight + nitrogens * n_weight

    print(f"The molecular weight of this molecule is {molecular_weight}.")


main()
