# This program will determine molar mass and present mass or moles of an element or compound given user inputs

import string
import math
# these imports were precautionary
# if more complex processes are added they may be used

# dictionaries containing the known average atomic weights and names of the elements
# does not contain synthetic elements
pTableNames = {
    "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium",
    "B": "Boron", "C": "Carbon", "N": "Nitrogen", "O": "Oxygen",
    "F": "Fluorine", "Ne": "Neon", "Na": "Sodium", "Mg": "Magnesium",
    "Al": "Aluminium", "Si": "Silicon", "P": "Phosphorus", "S": "Sulfur",
    "Cl": "Chlorine", "Ar": "Argon", "K": "Potassium", "Ca": "Calcium",
    "Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium",
    "Mn": "Manganese", "Fe": "Iron", "Co": "Cobalt", "Ni": "Nickel",
    "Cu": "Copper", "Zn": "Zinc", "Ga": "Gallium", "Ge": "Germanium",
    "As": "Arsenic", "Se": "Selenium", "Br": "Bromine", "Kr": "Krypton",
    "Rb": "Rubidium", "Sr": "Strontium", "Y": "Yttrium", "Zr": "Zirconium",
    "Nb": "Niobium", "Mo": "Molybdenum", "Ru": "Ruthenium", "Rh": "Rhodium",
    "Pd": "Palladium", "Ag": "Silver", "Cd": "Cadmium", "In": "Indium",
    "Sn": "Tin", "Sb": "Antimony", "Te": "Tellurium", "I": "Iodine",
    "Xe": "Xenon", "Cs": "Caesium", "Ba": "Barium", "La": "Lanthanum",
    "Hf": "Hafnium", "Ta": "Tantalum", "W": "Tungsten", "Re": "Rhenium",
    "Os": "Osmium", "Ir": "Iridium", "Pt": "Platinum", "Au": "Gold",
    "Hg": "Mercury", "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth",
    "Ce": "Cerium", "Pr": "Praseodymium", "Nd": "Neodymium", "Sm": "Samarium",
    "Eu": "Europium", "Gd": "Gadolinium", "Tb": "Terbium", "Dy": "Dysprosium",
    "Ho": "Holmium", "Er": "Erbium", "Tm": "Thulium", "Yb": "Ytterbium",
    "Lu": "Lutetium", "Th": "Thorium", "Pa": "Protactinium", "U": "Uranium"
}
pTableMass = {
    "H": 1.008, "He": 4.003, "Li": 6.941, "Be": 9.012,
    "B": 10.61, "C": 12.01, "N": 14.01, "O": 16.00,
    "F": 19.00, "Ne": 20.18, "Na": 22.99, "Mg": 24.31,
    "Al": 26.98, "Si": 28.09, "P": 30.97, "S": 32.07,
    "Cl": 35.45, "Ar": 39.95, "K": 39.10, "Ca": 40.08,
    "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 52.00,
    "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69,
    "Cu": 63.55, "Zn": 65.38, "Ga": 69.72, "Ge": 72.63,
    "As": 74.92, "Se": 78.96, "Br": 79.90, "Kr": 83.80,
    "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22,
    "Nb": 92.91, "Mo": 95.96, "Ru": 101.1, "Rh": 102.9,
    "Pd": 106.4, "Ag": 107.9, "Cd": 112.4, "In": 114.8,
    "Sn": 118.7, "Sb": 121.8, "Te": 127.6, "I": 126.9,
    "Xe": 131.3, "Cs": 132.9, "Ba": 137.3, "La": 138.9,
    "Hf": 178.5, "Ta": 180.9, "W": 183.8, "Re": 186.2,
    "Os": 190.2, "Ir": 192.2, "Pt": 195.1, "Au": 197.0,
    "Hg": 200.6, "Tl": 204.4, "Pb": 207.2, "Bi": 209.0,
    "Ce": 140.1, "Pr": 140.9, "Nd": 144.2, "Sm": 150.4,
    "Eu": 152.0, "Gd": 157.3, "Tb": 158.9, "Dy": 162.5,
    "Ho": 164.9, "Er": 167.3, "Tm": 168.9, "Yb": 173.1,
    "Lu": 175.0, "Th": 232.0, "Pa": 231.0, "U": 238.0
}


def heading(var):
    print "================================================================================="
    print var
    print "================================================================================="


heading("Stoichiometry calculator".upper())
# this chunk defines some needed variables for top-level code
# determines whether to convert grams to moles or moles to grams later on
elementOrCompound = str(raw_input("Are you working with an (element) or (compound)? "))
molG = False
gMol = False
convert = raw_input("Do you know (g) or (mol)? ")
if convert[0] == "g":
    gMol = True
elif convert[0] == "m":
    molG = True

# this chunk deals with compounds containing more than one element
if elementOrCompound[0] == "c":
    # creates lists that contain user inputs for later use
    elemName = "not done"
    compList = []
    subsList = []
    while elemName != "":
        if compList == list():
            elem = raw_input("\nEnter the first element, use Elemental Symbol: ")
            elemName = elem
            compList.append(elem)
            subsList.append(int(raw_input("What is the subscript? (If none, enter 1): ")))
        else:
            elem = raw_input("\nEnter next element, use Elemental Symbol: press <enter> to finish ")
            elemName = elem
            if elem != "":
                compList.append(elem)
                subsList.append(int(raw_input("What is the subscript? (If none, enter 1): ")))
    else:
        print "\nFinished inputting compound:"
        # if you want input printed back to user for verification:
        # print "Here is what you input; make sure it looks right:"
        # print compList
        # print subsList
        # print "press enter to continue"

    # this chunk calculates the total molar mass
    length = len(compList)
    totMass = 0.0
    for i in range(length):
        totMass = totMass + (pTableMass[compList[i]] * subsList[i])
    print "The Molar Mass of the compound is", totMass, "g/mol."

    # this is the stoichiometry bit
    # for moles to grams conversion
    if molG:
        conversionFactor = float(totMass)
        moles = float(raw_input("\nHow many moles of the compound do you have?: "))
        conversion = round(moles * conversionFactor, 4)
        print "The present mass of the compound is", conversion, "grams."
        raw_input("\nPress enter to close.")
    # and grams to moles conversion
    elif gMol:
        conversionFactor = float(1 / totMass)
        grams = float(raw_input("\nHow many grams of the compound do you have?: "))
        conversion = round(grams * conversionFactor, 4)
        print "The present compound contains", conversion, "moles."
        raw_input("\nPress enter to close.")

# this chunk works with individual elements
else:
    # calculates the molar mass
    elemSym = raw_input("What element do you want to convert?(Use Elemental Symbol): ")
    subs = float(raw_input("What is the subscript? (If none, input 1): "))
    mass = pTableMass[elemSym]
    molMass = subs * mass
    print "Molar mass is", molMass

    # stoichiometry
    if molG:
        conversionFactor = float(molMass)
        moles = float(raw_input("How many moles of the element do you have?: "))
        conversion = round(moles * conversionFactor, 4)
        # I round to 4 decimal places, gets needed sig figs most of the time
        # if you need more sig figs, change the number in the rounding argument
        print "The present mass of", pTableNames[elemSym] + " is", conversion, "grams."
        raw_input("Press enter to close.")

    elif gMol:
        conversionFactor = float(1 / molMass)
        grams = float(raw_input("How many grams of the element do you have?: "))
        conversion = round(grams * conversionFactor, 4)
        print "There are", conversion, "moles of " + pTableNames[elemSym] + " present."
        raw_input("Press enter to close.")
