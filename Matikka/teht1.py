import numpy as np
#Muunna asteiksi:
# a) 2,493 rad

a = 2,493
b = 0,911
a_2 = 137.7
b_2 = 62.3

print(f"\nTehtävän 1. a) vastaus: {np.degrees(a)}.")
print(f"Tehtävän 1. b) vastaus: {np.degrees(b)}.")
print(f"Tehtävän 2. a) vastaus: {np.radians(a_2)}.")
print(f"Tehtävän 2. b) vastaus: {np.radians(b_2)}.")

print(f"\nLista asteista radiaaneiksi:")
lista = np.array([30,45,60,120,135,180,270,360])

for i in lista:
    print(f"{np.radians(i):2.3f}")
