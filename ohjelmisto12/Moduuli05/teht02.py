luvut = []


luku = input("Syötä luku, tai lopeta painamalla enter : ")
while luku!= "" :
    luvut.append(luku)
    luku = input("Syötä luku, tai lopeta painamalla enter : ")


luvut.sort(reverse=True)

for n in range(5):
    print(luvut[n])

