# muuttuja ja tyyppi
age = 5
print(age)
age = 6
print(age + 2)
# MERKKIJONO
age_string = "seitsemän"
# Kokonaisluku
age_int = 6
# ei toimi: print(age_string + age_int)
# plus-lasku
print(age_int + 4)
# Merkkijonojen liittäminen
print(age_string + "vuotta")

#liukuluvut (float) (ei ihan sama kuin desimaaliluvuilla)
depth = 1000.0
width = 7000
area = depth * width
print(area)

# Totta vai tarua (Pythonissa 1 ja 0)
is_it_true = True
print(is_it_true)
is_it_false = False
print(is_it_false)

#Tyyppimuunnokset
age_input = input("kuinka vanha olet?")
#print(type(ageinput)) # "22"
age_int = int(age_input)
new_age = age_int + 1
print("Vuoden päästä olet " + str(new_age) + "vuotias")
# tai "f-stringillä"
