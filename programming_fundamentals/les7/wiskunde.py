def tafels():
    for i in range(1,11):
        for j in range (0,11):
            print(f"{i} * {j} = {i * j}")
        print("")
tafels()

def kwadraad():
    gemiddeld = 0
    for i in range(7):
        getal = int(input("geef een getal: "))
        kwadraad = getal**2
        print(f"het kwadraad is: {kwadraad}")
        gemiddeld += getal
    gemiddeld /= 7
    print(f"het gemiddelde is: {gemiddeld}")
    
kwadraad()

def is_priemgetal(getal):
    deelbaar = 0
    for i in range(2, getal):
        deelbaar += 1 if (getal % 2 == 0) else 0
    return True if (deelbaar == 0) else False

print(is_priemgetal(11))
print(is_priemgetal(10))

print("\n")

def fibonnaci(aantal_nummers):
    fibonacci_min_1 = 1
    fibonacci_min_2 = 1
    for i in range(aantal_nummers):
        fibonnaci = fibonacci_min_1 + fibonacci_min_2
        print(f" {fibonacci_min_2} + {fibonacci_min_1} = {fibonnaci}")
        fibonacci_min_2 = fibonacci_min_1
        fibonacci_min_1 = fibonnaci

fibonnaci(12)


