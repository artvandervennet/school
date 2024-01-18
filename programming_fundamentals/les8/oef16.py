def zoekertje(zin = ""):
    zin = zin.lower()
    zin2 = zin
    VOWELS = "aeuoi"
    i = 0
    while i < len(zin2):
        for vowel in VOWELS:
            if zin2[i] == vowel and  zin2[i-1] != " " and i != 0:
                zin2 = zin2[:i] + zin2[i+1:]
                i -= 1
        i += 1


    print(zin2)

zoekertje("Appartement Te Huur, 3 slaapkamers, ruime inkom,\ntuin en garage.")