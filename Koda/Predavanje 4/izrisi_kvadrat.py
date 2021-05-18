
def izrisi_kvadrat(n, k):
    """
    Funkcija izrise kvadrat iz znakov *, z stranicami velikosti n
    debeline k
    """
    zgoraj = k
    spodaj = n - k
    for i in range(n):
        if i >= zgoraj and i < spodaj:
            print("*" * k + " " * (n - 2 * k) + "*" * k)
        else:
            print("*" * n)


# izrisi_kvadrat(4, 2)
# izrisi_kvadrat(7, 2)
# izrisi_kvadrat(10, 2)
# izrisi_kvadrat(10, 10)
# print([i for i in range(0, 10)])


















def izrisi_kvadrat_oneliner(n, k):
    """
    Funkcija izrise kvadrat iz znakov *, z stranicami velikosti n
    debeline k
    """
    print("".join(["*"*k+" "*(n-2*k)+"*"*k+"\n" if (i>=k and i<n-k) else "*"*n+"\n" for i in range(n)]))


#izrisi_kvadrat_oneliner(4, 1)
#izrisi_kvadrat_oneliner(7, 2)
#izrisi_kvadrat_oneliner(10, 2)
#izrisi_kvadrat_oneliner(10, 1)
























izrisi_kvadrat_dobesedno_oneliner = lambda n, k: "".join(["*"*k+" "*(n-2*k)+"*"*k+"\n" if (i>=k and i<n-k) else "*"*n+"\n" for i in range(n)])

#print(izrisi_kvadrat_dobesedno_oneliner(7, 2))


