#4
eka = input("Anna jokin kokonaisluku:")
toka = input("Anna toinen kokonaisluku:")
kolmas = input("Anna kolmas kokonaisluku:")

summa = float(eka) + float(toka) + float(kolmas)
tulo = float(eka)*float(toka)*float(kolmas)
keskiarvo = (float(eka) + float(toka) + float(kolmas))/3

print("Annettujen lukujen summa =" + str(summa))
print("Annettujen lukujen tulo =" + str(tulo))
print("Annettujen lukujen keskiarvo =" + str(keskiarvo))
