def poista_parittomat(lista):
    parilliset = [x for x in lista if x % 2 == 0]
    return parilliset

alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 551, 513, 122]


karsittu_lista = poista_parittomat(alkuperäinen_lista)

print("Alkuperäinen lista:", alkuperäinen_lista)
print("Karsittu lista (parilliset luvut):", karsittu_lista)
