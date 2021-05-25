import csv
from matplotlib import pyplot as plt


def izrisi_gdp():
    with open("bdp_na_preb.csv", "r") as f:
        data = list(csv.reader(f))
        x = []
        y = []
        for row in data[3:]:
            if not row[1] == "...":
                x.append(int(row[0]))
                y.append(int(row[1]))

        plt.plot(x, y, marker='o', color="red")
        plt.show()


def izrisi_preb():
    with open("preb_po_star_in_spol.csv", "r") as f:
        data = list(csv.reader(f))
        cleaned = {"Moški": {}, "Ženske": {}}
        print(data)
        for row in data[3:]:

            uporabni = row[2:5] + row[11:13]
            podatki = [int(i) for i in uporabni]
            cleaned[row[0]][row[1]] = podatki

        # Seštejemo za moške in ženske
        moski = sum(cleaned["Moški"]["SLOVENIJA"])
        zenske = sum(cleaned["Ženske"]["SLOVENIJA"])
        skupaj = moski + zenske
        print(moski, zenske, skupaj)
        # Izpišemo
        print("V Sloveniji je {} prebivalcev od tega je {}% moških in {}% žensk".format(skupaj,
                                                                               round((moski/skupaj) * 100, 2),
                                                                                          round((zenske/skupaj) * 100, 2)))
        # Določimo seznam za posamezen stolpec v histogramu
        ticks = ["0 let", "1-5 let", "6-14 let", "15-64 let", "65 let ali več"]
        bars_x = [1, 2, 3, 4, 5]

        moski_po_letih = cleaned["Moški"]["SLOVENIJA"]
        zenske_po_letih = cleaned["Ženske"]["SLOVENIJA"]
        m_in_z = [moski_po_letih, zenske_po_letih]

        moski_in_zenske = [moski_po_letih[i] + zenske_po_letih[i] for i in range(len(moski_po_letih))]
        plt.bar(bars_x, height=moski_in_zenske, color="blue")
        # plt.bar(bars_x, height=moski_in_zenske, color="blue")
        plt.bar(bars_x, height=zenske_po_letih, color="red")
        plt.xticks(bars_x, ticks)
        plt.show()


if __name__ == "__main__":
    # izrisi_preb()
    visine_igralcev = [183, 185, 188, 193, 196, 198, 201, 206, 208, 213, 221, 224]  # V cm

    bars_x = ["< 190", "190 - 200", "200-210", "210 <"]  # Opisi stolpcev
    st_po_visini = [3, 2, 3, 3]  # 3 igralci so nižji od 190cm, 2 med 190cm in 200cm, ...

    plt.bar(bars_x, height=st_po_visini)
    # Nastavimo opise in naslov
    plt.xlabel("Višina v cm")
    plt.ylabel("Število igralcev")
    plt.title("Višine košarkarjev skupine Dallas Mavericks")
    # Izrišemo
    plt.show()
