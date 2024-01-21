#1

käyttäjä = input('Anna nimesi: ')
print("Hauska tavata, " + käyttäjä + "!")
#2 Ympyrän pinta-ala

säde_str = input("Syötä ympyrän säde:")
säde = float(säde_str)
area = (säde*3.14159**2)
print("Ympyrän pinta-ala = " + str(area))

#3 Suorakulmion Pinta-ala ja piiri

suorakulmiokanta_str = input("Anna suorakulmion kanta:")
suorakulmiokorkeus_str = input("Anna suorakulmion korkeus:")

korkeus = float(suorakulmiokorkeus_str)
kanta = float(suorakulmiokanta_str)

pinta_ala = (kanta*korkeus)
piiri = (kanta*2+korkeus*2)

print("Suorakulmion pinta-ala = " + str(pinta_ala))
print("Suorakulman piiri = " + str(piiri))

#4
eka_str = input("Anna jokin kokonaisluku:")
toka_str = input("Anna toinen kokonaisluku:")
kolmas_str = input("Anna kolmas kokonaisluku:")

summa = float(eka_str) + float(toka_str) + float(kolmas_str)
tulo = float(eka_str)*float(toka_str)*float(kolmas_str)
keskiarvo = (float(eka_str) + float(toka_str) + float(kolmas_str))/3

print("Annettujen lukujen summa =" + str(summa))
print("Annettujen lukujen tulo =" + str(tulo))
print("Annettujen lukujen keskiarvo =" + str(keskiarvo))

#5
print("Massa keskiaikaisten mittojen mukaan-->")

leiviskät_str = input("Anna leiviskät :")
naulat_str = input("Anna naulat :")
luodit_str = input("Anna luodit :")

luoti = float(luodit_str)*13.3
naula = float(naulat_str) * ((luoti)*32)
leiviskä = float(leiviskät_str) * ((naula) *20)
massa = str(luoti) + str(naula) + str(leiviskä)

print("Massa nykymittojen mukaan =" + str(massa))