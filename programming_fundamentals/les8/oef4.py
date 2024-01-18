def energieverbruik():
    tarief = int(input("welk tarief gebruik je? [1/2] "))
    verbruik = int(input("hoeveel heb je verbruikt? "))

    VASTGOED1 = 75
    VASTGOED2 = 50
    if tarief == 1:
        prijs = VASTGOED1 + 1*verbruik
    else:
        prijs = VASTGOED2 + 2*verbruik
    
    prijs += (prijs / 100) *6
    return prijs

print(energieverbruik())

