#5
import math

print("Massa keskiaikaisten mittojen mukaan-->")

luoti = 13.3
naula = 32 * luoti
leiviskä = 20 * naula

leiviskät = float(input("Anna leiviskät"))
naulat = float(input("Anna naulat :"))
luodit = float(input("Anna luodit :"))

luotigramma = luodit * luoti
naulagramma = naula * naulat
leiviskätgramma = leiviskät * leiviskä

massa = luotigramma + naulagramma + leiviskätgramma
kilogrammoina = math.floor (massa/1000)
grammoina = math.floor (massa - kilogrammoina * 1000)

print("Massa nykymittojen mukaan = " + str(kilogrammoina) + (" kilogrammaa ja ") + str(grammoina) + " grammaa.")
