# Komentar

""" To je tudi komentar
v vec vrsticah. Izgleda, da v idle-u doloèenih šumnikov ni mogoèe napisati.
"""

# Spremenljivke ------

# Vrednost spremenljivke lahko spremenimo tako, da jo še enkrat definiramo
sprem = 4
print(sprem)
sprem = 5
print(sprem)

# Spremenljivko lahko spreminjamo(v tem primeru prištejemo 1):
sprem = sprem + 1
# Zgornje krajše zapišemo:
sprem += 1 

# Print ------

to_je_spremenljivka = 4  # V njo smo shranili število 4

print(to_je_spremenljivka)  # Izpiše vrednost spremenljivke in neviden znak \n ki predstavlja prelom v novo vrstico

print(to_je_spremenljivka, end=" ") # Ce v print ukaz dolocimo parameter end=" " vrednost tega prepiše(overwrite) zgornji znak \n

print(3)  # Ce sedaj izpišemo vrednost 3 za zgornjo spremenljivko se ti dve izpišeta v isti vrstici z presledkom, torej: 4 3

print(3, 4)  # Lahko izpisujemo tudi dva podatka hkrati



# Input -------


# Ce želimo sprejeti vhod uporabimo input, ta vedno vrne podatek tipa str(string), katerega lahko shranimo v spremenljivko

vhodni_podatek = input("Vpiši nek vhodni podatek:") # Kot parameter lahko podamo string, kateri se bo izpisal (kot pri print)
# Izpisemo vhodni podatek
print(vhodni_podatek)


# Casting(pretvarjanje tipov) ------

to_je_niz = "4"

to_je_celo_stevilo = int(to_je_niz)

""" Naslednje je zakomentirano ker vrne napako
to_je_niz = "Nek niz"

to_vrne_napako = int(to_je_niz)  # Ker v int(cela števila) lahko pretvarjamo samo stringe, ki so napisana kot števila 
"""

# Tip podatka preverimo z uporabo ukaza type()

print("Spremenljivka to_je_niz je tipa: ",type(to_je_niz))  # Z printom pa to seveda izpišemo













