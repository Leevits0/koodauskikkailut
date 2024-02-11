kuukausi = int(input("Syötä kuukauden numero (1-12): "))

vuodenaika = {
    (1, 2, 3): "Talvi",
    (4, 5, 6): "Kevät",
    (7, 8, 9): "Kesä",
    (10, 11, 12): "Syksy"
}

for kuukaudet, vuodenaika in vuodenaika.items():
    if kuukausi in kuukaudet:
        print(f"Kuukauden {kuukausi} vuodenaika on {vuodenaika}")
        break