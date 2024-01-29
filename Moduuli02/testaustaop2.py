import random
raha = 5
ehto = raha > 5
print(2+5*3)

a = False
b = False
c = True


d1 = (a and b) or c
d2 = a and (b or c)
d3 = c or b and a
print(d1)
print(d2)
print(d3)
# Tässä d1 = d3, eli _and_ menee _or_ edelle


rand_numero = random.randint(10,52)
print(rand_numero)

nopan_heitto = random.randint(1,6)
print(nopan_heitto)

sukupuoli = random.randint(1,2)
if sukupuoli == 1:
    print(" Poika🥸 ")
else:
    print(" Tyttö🥹 ")
    
