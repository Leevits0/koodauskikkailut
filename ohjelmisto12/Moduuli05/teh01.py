import random
noppa_määrä = int(input(" Anna noppien määrä: "))
summa = 0
for i in range(noppa_määrä):
    noppa = random.randint(1,6)
    print(noppa)
    summa = summa + noppa
print(f"noppien summa {summa}")



