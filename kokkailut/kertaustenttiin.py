""" while loop käyttöä:
import math

print(f"{math.pi:10.3f}")


nimi = input(" Anna nimesi:  ")

while True:
    if nimi != "James":
        nimi = input(" Anna nimesi uudelleen ")
    else:
        break

print(f"Tervetuloa {nimi}! ")
"""


"""
lista1 =[1, 5, 'Juha', 3.14, [2, 5], (1, 2, 8), {'eka': 4, 'toka': False}]

print(lista1[6]["eka"])

#start,end,step esim- [x:x:x] missä x = on luku

print(lista1[3::-1])

print("Juha" in lista1)
lista1.append(100)
print(lista1)
"""
"""
#RANGE käytössä sama kuin lista (start,end,step)

for luku in range(8):
    print(luku)

for kerta in range(8):
    print("moi")
"""

"""
monikko = (1,5,10)
eka, toka, kolmas = monikko
print(eka)
"""
###
"""
def lista2(lista):
    lista2 = lista[1]
    return lista2

l1 = [1,3,4,5,6]
palautus = lista2(l1)
print(palautus)
"""
###

def ananas(sanakirja):
    return sanakirja["nimi"]
sanak = {"nimi": "Jukka", "ikä": 28, "ammatti": "inssi"}
sanak2 = {"nimi": "Jussi", "ikä": 30, "ammatti": "lääkäri"}
palautus = ananas(sanak)
print(palautus)

def parittomat(lista):
    tyhjä_lista = []
    for item in lista:
        if item % 2 != 0:
            tyhjä_lista.append(item)
    return tyhjä_lista

luvut = [12, 5, 21, 4, 8, 0 ,11]
parit_list = parittomat(luvut)
print(f'alkuperäiset luvut: {luvut}')
print(f'parittomat luvut: {parit_list}')

def double(nums):
    tyhjä_lista2 = []
    for item in nums:
        tyhjä_lista2.append(item*2)
    return tyhjä_lista2

numbers = [12, 5]


def operate(lista, rajat):
    tyhj = []
    for item in lista:
        if rajat[0] < item < rajat[1]:
            tyhj.append(item)
    return sum(tyhj)


list = [15, 1, 8, 18, 33, 1, 2]
borders = (0, 9)
result = operate(list, borders)
print(f"Sallittujen lukujen summa: {result} ")

