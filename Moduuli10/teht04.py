import random

#Auto luokka
class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeudenmuutos):
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

#Kilpailu luokka
class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailun ({self.nimi}) tilanne kun aikaa kulunut = {tunti}h :")
        for auto in self.autot:
            print(f"Auto: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}km/h, kuljettu matka: {auto.matka} km")
        print()



    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False


# Pääohjelma
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:  # Tulostetaan tilanne joka 10. tunnin välein
        kilpailu.tulosta_tilanne()

#lopputilanne
kilpailu.tulosta_tilanne()