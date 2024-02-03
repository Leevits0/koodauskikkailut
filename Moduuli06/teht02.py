import random

def heita_noppaa(nopan_suuruus):
    return random.randint(1, nopan_suuruus)

nopan_suuruus = int(input("Syötä nopan tahkojen määrä: "))

heittoja = 1
while True:
    silmäluku = heita_noppaa(nopan_suuruus)
    print(f"Heitto: {heittoja} tulos = {silmäluku}")
    heittoja += 1

    if silmäluku == nopan_suuruus:
        break
