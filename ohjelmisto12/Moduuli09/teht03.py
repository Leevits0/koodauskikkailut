class Auto:

    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000

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

auto = Auto("ABC-123", 142)

auto.kulje(1.5)
print(f"kuljettu matka {auto.matka} km")