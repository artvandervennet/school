def aantal_verschillende_vowels(woord):
    VOWELS = "aieuo"
    aantal = 0
    woord = woord.lower()
    for vowel in VOWELS:
        for letter in woord:
            if letter == vowel :
                aantal += 1
                break
            
    return aantal


def min_max_klinkers():
    AANTAL_WOORDEN = 3
    
    woord = input("geef een woord: ")
    min_verschillende_klinkers = woord
    max_verschillende_klinkers = woord

    for i in range(AANTAL_WOORDEN-1):
        woord = input("geef een woord: ")
        min_verschillende_klinkers = woord if (aantal_verschillende_vowels(woord) < aantal_verschillende_vowels(min_verschillende_klinkers)) else min_verschillende_klinkers
        max_verschillende_klinkers = woord if (aantal_verschillende_vowels(woord) > aantal_verschillende_vowels(max_verschillende_klinkers)) else max_verschillende_klinkers
    print(f"het woord met de minste klinkers is: {min_verschillende_klinkers}")
    print(f"het woord met de meeste klinkers is: {max_verschillende_klinkers}")

min_max_klinkers()