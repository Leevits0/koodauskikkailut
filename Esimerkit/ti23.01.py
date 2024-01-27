#while silmukat (loopit)

# jakolaskukone, jakaja ei voi olla nolla
""" monen rivin merkkijono käytetään myös monen rivin kommenttina
num1 = float(input(" Anna jaettava nro : "))
num2 = float(input(" Anna jakaja nro : "))

while num2 == 0:
    print(" Ei voi olla 0 ")
    num2 = float(input(" Anna jakaja! : "))

result = num1 / num2
print(f" Jakolaskun tulos on: {result}")
"""

"""
# iteroiva silmukka (käytetään "laskuria" silmukan toistokertojen määrittelyyn)

#i = 1 # iteraattori i
i = int(input("Mistä numerosta aloitetaan? "))
amount = int(input(" Kuinka monta numeroa tulostetaan?"))
offset = int(input(" Anna numeroiden väli: "))
max_number = amount * offset + i
while i < max_number :
    print(f"Numero on {i}")
    i = i+ offset
print(f" i:n lopullinen arvo silmukan jälkeen: {i}")  # 11

# voit testata ehtolauseiden toimintaa tulostamalla niiden arvoja
print(i < i+1 )  # -> True
"""
# Sisäkkäiset kontrollirakenteet ja satunnaisuus
import random

random_number = random.randint(1,3)
print(f"Arvottu numero: {random_number}")

#Pelin asetukset
player_count = 2 #voi olla myös esim. int(input(" Kuinka monta pelaajaa? :"))
current_player = 1
dice_amount = 4

best_player = None
best_result = 0

#jokainen pelaaja suorittaa vuorollaan
while current_player <= player_count :
    result = 0 #Silmälukujen summa ennen heittoja
    throw_count = 0 # Iteraattori nopan heitoille
    # noppia heitetään dice_amount -muuttujassa asetettu määrä
    while throw_count < dice_amount :
        die = random.randint(1,6)
        print(f"Pelaaja {current_player}, {throw_count+1}. heitto {die}")
        result = result + die
        throw_count += 1  #sama kuin throw_count = throw_count + 1
    print(f"Pelaajan {current_player} tulos:  {result}")
    # Testataan saatiinko uusi paras tulos, ja tallennetaan tarvittaessa edellisen
    # parhaan tuloksen tilalle. Päivitetään samalla paras pelaaja
    if result > best_result :
        best_result = result
        best_player = f"Pelaaja {current_player}"
    #Jos tulos ei ole parempi, mutta on sama kuin edellinen paras tulos
    #yhdistetään pelaajan nimi edellisen parhaan pelaajan nimen lisäksi samaan stringiin = merkkijonoon
    elif result == best_result :
        best_player = best_player + f" , Pelaaja {current_player}"
    current_player = current_player + 1
print(f"Paras tulos = {best_result}, {best_player}.")


# Break-komento "heittää" ulos aktiivisesta silmukasta, suoritus jaktuu koodilohkon jälkeen

counter = 0
while True: # Ikuinen silmukka
    print(f" Laskuri eka {counter}")
    counter += 1
    if counter == 5:
        break #Poistuu silmukan koodilohkosta samantien, alla oleva ei tulostu
    print(f" Laskuri toka {counter}")
