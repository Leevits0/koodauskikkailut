class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")


# Luodaan julkaisut
aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Kirja("Hytti nro 6", "Rosa Liksom", 200)

# Tulostetaan julkaisujen tiedot
print("Aku Ankka:")
aku_ankka.tulosta_tiedot()
print("\nHytti nro 6:")
hytti_nro_6.tulosta_tiedot()