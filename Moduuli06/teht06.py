def laske_yksikköhinta(halkaisija, hinta):
    pinta_ala = (halkaisija / 2) ** 2 * 3.14159
    yksikköhinta = hinta / pinta_ala
    return yksikköhinta

#pizza 1
halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (senttimetreinä): "))
hinta1 = float(input("Syötä ensimmäisen pizzan hinta (euroina): "))

#pizza 2
halkaisija2 = float(input("Syötä toisen pizzan halkaisija (senttimetreinä): "))
hinta2 = float(input("Syötä toisen pizzan hinta (euroina): "))

yksikköhinta1 = laske_yksikköhinta(halkaisija1, hinta1)
yksikköhinta2 = laske_yksikköhinta(halkaisija2, hinta2)

if yksikköhinta1 < yksikköhinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikköhinta1 > yksikköhinta2:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat ovat yhtä hyvää vastinetta rahalle.")
