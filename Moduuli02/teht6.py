# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6

#Kolminumeroinen koodi:
import random

lukon_koodi = random.randint(0,999)
print("Kolminumeroisen numerolukon koodi:", lukon_koodi)


#nelinumeroinen koodi:
nelilukko1 = random.randint(1,6)
nelilukko2 = random.randint(1,6)
nelilukko3 = random.randint(1,6)
nelilukko4 = random.randint(1,6)
nelikoodi = str(nelilukko1) + str(nelilukko2) + str(nelilukko3) + str(nelilukko4)
print("Nelinumeroisen numerolukon koodi:", nelikoodi)
