#3 Suorakulmion Pinta-ala ja piiri

suorakulmio_kanta = input("Anna suorakulmion kanta:")
suorakulmio_korkeus = input("Anna suorakulmion korkeus:")

korkeus = float(suorakulmio_korkeus)
kanta = float(suorakulmio_kanta)

pinta_ala = (kanta*korkeus)
piiri = (kanta*2+korkeus*2)

print("Suorakulmion pinta-ala = " + str(pinta_ala))
print("Suorakulman piiri = " + str(piiri))