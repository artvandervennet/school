def ggd(getal1, getal2):
    kleinste = getal1 if getal1 < getal2 else getal2
    for i in range(1,kleinste+1):
        deler = i if getal1 % i == 0 and getal1 % i == 0 else deler
    return deler
print(ggd(10,20))

def kgv(getal1, getal2):
    start = getal1 if getal1 > getal2 else getal2
    veelvoud = 0
    while not veelvoud :
        veelvoud = start if start % getal1 == 0 and start % getal2 == 0 else veelvoud
        start += 1
    return veelvoud
print(kgv(10,21))