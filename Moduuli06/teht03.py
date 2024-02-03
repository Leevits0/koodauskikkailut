def muunna_gallonoiksi(gallona):
    return gallona * 3.785

while True:
    gallona = int(input("Syötä bensiinin määrä Yhdysvaltain nestegallonoina (negatiivinen luku lopettaa): "))

    if gallona < 0:
        print("Ohjelma päättyy.")
        break

    litrat = muunna_gallonoiksi(gallona)
    print(f"{gallona} nestegallonaa on {litrat:.2f} litraa.")