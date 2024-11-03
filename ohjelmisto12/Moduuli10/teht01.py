class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros +=1
        print(f"-Hissi nousi kerroksen. Olet nyt kerroksessa {self.nykyinen_kerros}.")

    def kerros_alas(self,):
        self.nykyinen_kerros -= 1
        print(f"- Hissi laski kerroksen. Olet nyt kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self,kerros):
        while self.nykyinen_kerros != kerros:
            if self.nykyinen_kerros < kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

hissi1 = Hissi(1,10)

hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(1)
