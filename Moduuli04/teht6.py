import random
# alustetaan pisteiden lkm-laskurit
N = n = 0
while N < 10:
    #arvotaan yksi piste
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    N += 1
    print(f" Arvottu piste: {x},{y}")
    if x * x + y * y < 1:
        n += 1
        print(f"Pisteitä yhteensä {N}, joista ympyrän sisällä {n}. ")

# TODO: Laske piin likiarvo
