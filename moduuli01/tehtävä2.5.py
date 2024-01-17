#5
print("Massa keskiaikaisten mittojen mukaan-->")
leiviskät_str = input("Anna leiviskät :")
naulat_str = input("Anna naulat :")
luodit_str = input("Anna luodit :")
luoti = float(luodit_str)*13.3
naula = float(naulat_str)*32*(luoti)
leiviskä = float(leiviskät_str)*20*(naula)
massa = float(luoti) + float(naula) + float(leiviskä)
print("Massa nykymittojen mukaan =" + str(massa))