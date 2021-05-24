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
        for row in data[3:]:
            cleaned[row[0]][row[1]] = row[2:]
            print(row)


x = [0, 1, 2, 3, 4]
y = [2, 3, 2, 3, 1]
plt.plot(x, y)
plt.show()

if __name__ == "__main__":
    izrisi_preb()
