class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"-Hissi nousi kerroksen. Olet nyt kerroksessa {self.nykyinen_kerros}.")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"- Hissi laski kerroksen. Olet nyt kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros != kerros:
            if self.nykyinen_kerros < kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for i in range(hissien_määrä)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print("Ajetaan hissiä", hissin_numero, "kohteeseen", kohde_kerros)
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Hissiä", hissin_numero, "ei ole talossa.")


talo = Talo(1,8,2)

talo.aja_hissiä(1,8)
talo.aja_hissiä(3,5)
talo.aja_hissiä(0,3)