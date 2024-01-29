
print(" Ohjelma muuntaa tuumat centtimetreiksi ")

while True:
    tuumat = float(input("Anna tuumat (syötä negatiivinen luku lopettaaksesi): "))

    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} senttimetriä.")
