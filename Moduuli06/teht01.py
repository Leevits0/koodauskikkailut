import random

def heitä_noppaa():
    return random.randint(1, 6)

heittoja = 1
while True:
    silmäluku = heitä_noppaa()
    print(f"Heitto: {heittoja} tulos = {silmäluku}")
    heittoja += 1

    if silmäluku == 6:
        break


