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

class Sähkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


sähkoauto = Sähkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)


sähkoauto.kiihdytä(111)
polttomoottoriauto.kiihdytä(55)

for i in range(3):
    sähkoauto.kulje(1)
    polttomoottoriauto.kulje(1)

print(f"Sähköauton matkamittarilukema:", sähkoauto.matka, "km")
print(f"Polttomoottoriauton matkamittarilukema:", polttomoottoriauto.matka, "km")