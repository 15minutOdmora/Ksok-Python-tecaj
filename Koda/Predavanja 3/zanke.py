
# Zanke (loops)

i = 0
"""
while i <= 5:
    print(i)
    i += 1 


print(9)
"""
"""
while True:
    print(i)
    i += 1
    if i <= 5:
        pass
    else:
        break 
"""

# Primer formatiranja nizov
niz = "Matija ima {} let, In hodi v šolo".format(22)
# print(niz)


for i in niz:
    # print(i, end="")
    pass

seznam = ["Ja", 42, 2.5, ["Ja", "Ne"], "Python"]


for element in seznam[::-1]:
    # print(element)
    pass


for i in range(0, 10):
    print(i)

