class Auto:

    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


auto = Auto("ABC-123", 142)

print(f"Uuden auton rekisteritunnus: {auto.rekisteritunnus},huippunopeus {auto.huippunopeus}km/h,kuljettu matka: {auto.nopeus},Tämänhetkinen nopeus: {auto.matka}.")
