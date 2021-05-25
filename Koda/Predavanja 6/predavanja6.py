import csv
from matplotlib import pyplot as plt


def izrisi_bdp():
    """
    Funkcija izriše navaden graf bdp na prebivalca v odvisnosti od časa(let).
    Podatki pridobljeni iz SiStat, se nahajajo v datoteki bdp_na_preb.csv
    """
    with open("bdp_na_preb.csv", "r") as f:  # Odpremo datoteko
        podatki = list(csv.reader(f))  # Z csv-jem preberemo in pretvorimo v seznam, kjer je vsaka vrstica v datoteki en element
        naslov = podatki[0][0]  # Shranimo naslov, ki se je nahajal v 1. vrstici
        x_label = podatki[2][0]  # Shranimo imena osi
        y_label = podatki[2][1]
        x, y = [], []  # Ustvarimo seznama kamor bomo hranili podatke točk
        for vr in podatki[3:]:  # Se sprehodimo skozi vrstice
            if not vr[1] == "...":  # Shranimo podatke, kjer bdp ni enak "..."
                x.append(int(vr[0]))  # Dodamo na konce seznamov
                y.append(int(vr[1]))

        plt.plot(x, y, marker="o", color="red")  # Narišemo graf
        plt.title(naslov)  # Dodamo naslov
        plt.xlabel(x_label)  # Dodamo ime x-osi
        plt.ylabel(y_label)  # Dodamo ime y-osi
        plt.show()  # Prikažemo graf


def izrisi_preb_na_spol():
    """
    Funkcija izriše histogram števila prebivalcev po spolu glede na starostno skupino.
    Podatki pridobljeni iz SiStat, se nahajajo v datoteki bdp_na_preb.csv
    """
    with open("preb_po_star_in_spol.csv", "r") as f:  # Odpremo datoteko
        podatki = list(csv.reader(f))  # Preberemo z csv, pretvorimo v seznam

        ocisceni = {"Moški": {}, "Ženske": {}}  # Ustvarimo slovar kjer bomo hranili nam uporabne podatke
        for vr in podatki[3:]:  # Se sprehodimo skozi vrstice
            spol = vr[0]
            regija = vr[1]
            uporabni = vr[2:5] + vr[11:13]  # Uporabimo le določene stolpce (slicing)
            podatki = [int(i) for i in uporabni]  # Podatke pretvorimo v cela števila int
            ocisceni[spol][regija] = podatki  # Shranimo pod vstreznimi ključi v slovar

        moski = sum(ocisceni["Moški"]["SLOVENIJA"])  # Število moških
        zenske = sum(ocisceni["Ženske"]["SLOVENIJA"])  # Število žensk
        skupaj = moski + zenske  # Skupaj prebivalcev
        # Izpišemo podatke
        print("V sloveniji je {} prebivalcev, od tega je {} moških in {} žensk.".format(skupaj, moski, zenske))

        ticks = ["0 let", "1-5 let", "6-14 let", "15-64 let", "65 let ali več"]
        moski_po_letih = ocisceni["Moški"]["SLOVENIJA"]  # Seznam št. moških preb. glede na zgornje starostne skupine
        zenske_po_letih = ocisceni["Ženske"]["SLOVENIJA"]  # Enako le za ženske
        # Seznam vsot št. moških in ženskih glede na starostno skupino
        moski_in_zenske = [moski_po_letih[i] + zenske_po_letih[i] for i in range(len(moski_po_letih))]

        # Ustvarimo seznam x-pozicij podatkov
        bars = [1, 2, 3, 4, 5]

        # Ustrezno izrišemo
        plt.bar(bars, height=moski_in_zenske, color="blue")
        plt.bar(bars, height=zenske_po_letih, color="red")
        plt.xticks(bars, ticks)
        plt.show()


if __name__ == "__main__":
    # Tukaj pokličemo funkcije
    izrisi_bdp()
    izrisi_preb_na_spol()