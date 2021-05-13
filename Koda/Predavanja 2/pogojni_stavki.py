# Pogojni stavki: IF, ELIF, ELSE

# print(3 == 5)
# print(3 == 3)
# print(3 != 5)

# print(3 < 5)
# print(3 > 5)

# print(3 > 5 and 3 < 6)
# print(3 < 5 and 3 < 6)

# print(4 == 5 or 4 != 5)
# print(4 == 5 or 4 == 3)

seznam = [2, 3, 4]
# print(2 in seznam)
# print(5 in seznam)

st = 4
pogoj = 3 > st

"""
if pogoj:
    print("Pogoj velja")
else:
    print("Pogoj ne velja")
    print(2)
    # kom
    print(3)
"""
st1 = 250
st2 = 100
st3 = 200


if st1 < st2:
    print("st1 < st2")
elif st3 >= st1 >= st2:
    print("st1 >= st2")

if True:
    print("To se vedno izvede")
else:
    print("Nic od zgoraj navedenega")
















