import random
class Auto:

    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenmuutos):
        uusi_nopeus = self.nopeus + nopeudenmuutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus
    def kulje(self, tunnit):
        kokonais_matka = self.nopeus * tunnit
        self.matka += kokonais_matka

autot = []
for i in range(1,11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))
kilometritavoite = 10000

# Kilpailu
while max(auto.matka for auto in autot) < kilometritavoite:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)

print("Kilpailun tulokset:")
print("{:<20} {:<20} {:<20} {:<20}".format("Rekisteritunnus", "Huippunopeus: km/h", "Kuljettu matka: km", "Nykyinen nopeus: km/h"))
for auto in autot:
    print("{:<20} {:<20} {:<20} {:<20}".format(auto.rekisteritunnus, auto.huippunopeus, auto.matka, auto.nopeus))