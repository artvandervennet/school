def positief_verschil():
    aantal_getallen = int(input("hoeveel getallen wil je inlezen? "))
    
    for i in range(aantal_getallen):
        getal = int(input("geef een getal: "))
        if i == 0:
            kleinste = getal
            grootste = getal
        else:
            kleinste = getal if getal < kleinste else kleinste
            grootste = getal if getal > grootste else grootste
    return grootste - kleinste

print(positief_verschil())