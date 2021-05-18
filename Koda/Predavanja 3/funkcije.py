from izrisi_kvadrat import izrisi_kvadrat


def izpisi_pozdrav():  
    """
    Funkcija izpise pozdrav
    """
    print("Pozdravljeni")

def izpisi_kvadrat(x):
    """
    Funkcija izpiše kvadrat števila
    """
    print("Kvadrat števila {} je {}".format(x, x**2))


def kvadriraj(x):
    """
    Funkcija vrne kvadrat vhodnega števila 
    """
    kvadrat = x**2
    return kvadrat
    print("nrki")


def sestej(a, b):
    """
    Funkcija vrne vsoto dveh števil
    """
    return a + b


def na_potenco(x, potenca=1, pristej=0):
    """
    Funkcija število potencira in prišteje drugo število
    """
    return x**potenca + pristej


# s = izpisi_pozdrav()
# print(s)

# print(izpisi_kvadrat(3))

# kvadrat = kvadriraj(4)
# print(kvadrat)
# print(kvadriraj(5))

# vsota = sestej(5, 3)
# print(vsota)


# print(na_potenco(4, 2, 10))


def kvadriraj(x):
    """
    Funkcija vrne kvadrat vhodnega števila 
    """
    return x**2



# Lambda

kvadrat = lambda x: x**2

# print(kvadrat(2))

sestej = lambda x, y: x + y

print(sestej(3, 5))











    
