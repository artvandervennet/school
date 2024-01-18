def patroon(hoogte):
    even = ((hoogte % 2) == 0)
    bezig = True
    while even and bezig:
        print("+----+")
        for i in range(int(hoogte/2)):
            print("\    /")
            print("/    \\")
        print("+----+")
        bezig = False

patroon(6)
print("\n")

def tekenreeks(aantal_per_lijn, aantal_lijnen, teken = "*"):
    for i in range(aantal_lijnen):
        print(teken * aantal_per_lijn)
        print("")
tekenreeks(8,3,"*")

print("\n")

def kerstboom(hoogte):
    for i in range(hoogte + 1):
        print("*" * (hoogte - (hoogte - i)))

kerstboom(5)

print("\n")

def driehoek(grootte):
    i = 0
    while i < grootte :
        print(" " * ((grootte-1)-i) + "*" * i +  "*" + "*" * i + " " * ((grootte - 1) - i))
        i+=1

driehoek(6)