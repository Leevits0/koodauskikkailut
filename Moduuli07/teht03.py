
airports = {}

while True:
    print("\nValitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    choice = input("Valintasi: ")

    if choice == "1":

        icao_code = input("Syötä lentoaseman ICAO-koodi: ")
        name = input("Syötä lentoaseman nimi: ")
        airports[icao_code] = name
        print("Lentoasema tallennettu onnistuneesti.")

    elif choice == "2":

        icao_code = input("Syötä haettavan lentoaseman ICAO-koodi: ")
        if icao_code in airports:
            print(f"Lentoaseman nimi: {airports[icao_code]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif choice == "3":

        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta. Yritä uudelleen.")
