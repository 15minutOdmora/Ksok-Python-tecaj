osebe = [
    {"ime": "Franc", "priimek": "Novak", "starost": 43},
    {"ime": "Zala", "priimek": "Horvat", "starost": 16},
    {"ime": "Janez", "priimek": "Kovačič", "starost": 20},
    {"ime": "Marko", "priimek": "Krajnc", "starost": 25},
    {"ime": "Marija", "priimek": "Vidmar", "starost": 88}
]


class Oseba:
    def __init__(self):
        self.ime = None
        self.priimek = None
        self.starost = 0
        self.sola = None

    def dolocitev_imena(self, ime, priimek):
        self.ime = ime
        self.priimek = priimek

    def staranje(self, st_let=1):
        self.starost += st_let
        print("{} {} se je postaral za {} let.".format(self.ime, self.priimek, st_let))

    def vpis_v_solo(self, ime_sole):
        self.sola = ime_sole
        print("{} {} se je vpisal v osnovno šolo {}".format(self.ime, self.priimek, self.sola))

    def diplomiral(self):
        print("{} {} je diplomiral na {}".format(self.ime, self.priimek, self.sola))
        self.sola = True


class Delavec(Oseba):
    def __init__(self, oseba):
        super().__init__()
        self.ime = oseba.ime
        self.priimek = oseba.priimek
        self.starost = oseba.starost
        self.sola = oseba.sola
        self.delovna_doba = 0

    def delal_1_leto(self):
        self.delovna_doba += 1

    def __repr__(self):
        opis = "Delavec: {} {} je star {} let in dela že {}".format(self.ime, self.priimek, self.starost, self.delovna_doba)
        return opis


dojencek = Oseba()
dojencek.dolocitev_imena("Jan", "Kranjc")
dojencek.staranje(5)
dojencek.vpis_v_solo("OŠ Lucija")
dojencek.staranje(13)
dojencek.diplomiral()

# Smo šef
delavec = Delavec(dojencek)
delavec.staranje(3)
delavec.delal_1_leto()
print(delavec)









