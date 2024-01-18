import random

def aantal_ogen(ogen):
    geworpen = 0
    pogingen = 0
    while geworpen != ogen:
        geworpen = random.randint(1,6)
        pogingen += 1

        print(f"Poging {pogingen} : {geworpen}")
    print(f"in {pogingen} pogingen werd een {geworpen} gedobbeld")

aantal = int(input("Hoeveel ogen wil je werpen?"))
print(aantal_ogen(aantal))