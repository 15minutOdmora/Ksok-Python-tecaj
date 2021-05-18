# Igra krizec krozec

polje = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# Polje:
#          1.st  2.st  3.st
#  1. vr   [" ", " ", " "]
#  2. vr   [" ", " ", " "]
#  3. vr   [" ", " ", " "]
zmagovalni_znak = ""
konec_igre = False

krog = 1
while krog < 9:
    # Izpišemo polje
    print("{}|{}|{}".format(polje[0][0], polje[0][1], polje[0][2]))
    print("-----")
    print("{}|{}|{}".format(polje[1][0], polje[1][1], polje[1][2]))
    print("-----")
    print("{}|{}|{}".format(polje[2][0], polje[2][1], polje[2][2]))

    # Preberemo ukaz igralca
    if krog % 2 == 0:
        ukaz = input("Na vrsti je 2. igralec: ")
        znak = "X"
    else:
        ukaz = input("Na vrsti je 1. igralec: ")
        znak = "O"

    # Iz ukaza dolocimo vrstico in stolpec
    vrstica = int(ukaz[0]) - 1
    stolpec = int(ukaz[1]) - 1
    # Spremenimo polje na doloceni vrsticici in stolpcu
    polje[vrstica][stolpec] = znak

    # Pregledamo ce je kdo dosegel 3 v vrsti
    # Ustvarimo seznam stolpcev, da je bolj pregledno
    stolpci = [[], [], []]
    # Gremo po vrsticah
    for vrstica in polje:
        # Za vsako vrstico preverimo ce vsebuje 3 enake znake
        # Tako da jo pretvorimo v mnozico
        if len(set(vrstica)) == 1 and vrstica[0] != " ":
            zmagovalni_znak = vrstica[0]
            konec_igre = True
        # Sproti ustvarjamo transponirano polje oz. seznam stolpcev
        # Posameznemu stolpcu dodamo znak
        stolpci[0].append(vrstica[0])
        stolpci[1].append(vrstica[1])
        stolpci[2].append(vrstica[2])
    # Preverimo še stolpce
    for stolpec in stolpci:
        # Za vsak stolpec preverimo ce vsebuje 3 enake znake
        # Tako da ga pretvorimo v mnozico
        if len(set(stolpec)) == 1 and stolpec[0] != " ":
            zmagovalni_znak = stolpec[0]
            konec_igre = True
    # Na dolgo preverimo še dve diagonali
    # Znak v levem zgornjem kotu
    znak = polje[0][0]
    if polje[1][1] == znak and polje[2][2] == znak and znak != " ":
        zmagovalni_znak = znak
        konec_igre = True
    # Znak v desnem zgornjem kotu
    znak = polje[0][2]
    if polje[1][1] == znak and polje[2][0] == znak and znak != " ":
        zmagovalni_znak = znak
        konec_igre = True

    if konec_igre:
        break
    
    krog += 1


# Ko pridemo vn iz zanke se enkrat izpisemo polje in dolocimo zmagovalca
print("{}|{}|{}".format(polje[0][0], polje[0][1], polje[0][2]))
print("-----")
print("{}|{}|{}".format(polje[1][0], polje[1][1], polje[1][2]))
print("-----")
print("{}|{}|{}".format(polje[2][0], polje[2][1], polje[2][2]))
    
if zmagovalni_znak == "O":
    print("Zmagal je 1. igralec!")
elif zmagovalni_znak == "X":
    print("Zmagal je 2. igralec!")
else:
    print("Igra je bila izenacena!")







    
    
    
