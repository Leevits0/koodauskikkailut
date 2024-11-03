sukupuoli = input("Kerro biologinen sukupuolesi: (M/N) ")
hemoglobiini_arvo = int(input(" Mikä on sinun hemoglobiini arvo g/l? :"))

if sukupuoli == "M":
    if hemoglobiini_arvo >= 134 and hemoglobiini_arvo <= 195:
        print(f"Hemoglobiini {hemoglobiini_arvo} g/l on normaali ")
    elif hemoglobiini_arvo > 195:
        print(f"Hemoglobiini arvo {hemoglobiini_arvo} g/l on korkea ")
    elif  hemoglobiini_arvo < 134:
        print(f"Hemoglobiini arvo {hemoglobiini_arvo} g/l on matala ")


if sukupuoli == "N":
    if  hemoglobiini_arvo >= 117 and hemoglobiini_arvo <= 175:
        print(f"Hemoglobiini arvo on normaali {hemoglobiini_arvo}")
    elif  hemoglobiini_arvo > 175:
        print(f"Hemoglobiini arvo on korkea {hemoglobiini_arvo}")
    elif  hemoglobiini_arvo < 117 :
        print(f"Hemoglobiini arvo on matala {hemoglobiini_arvo}")
    else :
        print("Virhe, syötä arvot uudelleen. ")

