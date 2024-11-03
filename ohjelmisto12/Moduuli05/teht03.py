luku = int(input("Anna kokonaisluku, saat selville onko se alkuluku vai ei: "))

alkuluku = True
for i in range(2,luku-1):
        if luku %i==0:
            alkuluku = False

print(alkuluku)