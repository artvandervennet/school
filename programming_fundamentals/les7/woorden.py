import string as s

def plak_alles_samen():
    keer_doorlopen = int(input("hoeveel woorden wil je ingeven: "))
    woorden_samen =""
    for i in range(keer_doorlopen):
        woorden_samen += input("geef een woord: ")
    print(F"de lengte van alle woorden samen is {len(woorden_samen)}")
plak_alles_samen()

def af_en_op(woord):
    for i in range(len(woord)):
        print(woord[:-i])
    for i in range(2, len(woord)):
        print(woord[:-(len(woord) - i)])

af_en_op("hallo")

print("")

def aantal_vowels(woord):
    VOWELS = "aieuo"
    aantal = 0
    woord = woord.lower()
    for vowel in VOWELS:
        for letter in woord:
            aantal += 1 if letter == vowel else 0
    return aantal


def min_max_klinkers():
    AANTAL_WOORDEN = 3
    
    woord = input("geef een woord: ")
    min_klinkers = woord
    max_klinkers = woord

    for i in range(AANTAL_WOORDEN-1):
        woord = input("geef een woord: ")
        min_klinkers = woord if (aantal_vowels(woord) < aantal_vowels(min_klinkers)) else min_klinkers
        max_klinkers = woord if (aantal_vowels(woord) > aantal_vowels(max_klinkers)) else max_klinkers
    print(f"het woord met de minste klinkers is: {min_klinkers}")
    print(f"het woord met de meeste klinkers is: {max_klinkers}")

min_max_klinkers()


