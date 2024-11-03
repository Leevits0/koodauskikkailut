import random

tietokoneen_luku = random.randint(1, 10)
arvaukset = 0

print("Arvaa luku väliltä 1..10")

while True:
    pelaajan_arvaus = int(input("Syötä arvauksesi: "))
    arvaukset += 1

    if pelaajan_arvaus > tietokoneen_luku:
        print("Liian suuri arvaus.")
    elif pelaajan_arvaus < tietokoneen_luku:
        print("Liian pieni arvaus.")
    else:
        print(f"Oikein! Arvasit oikein {arvaukset} yrityksellä.")
        break