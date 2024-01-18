def blok_tekst(zin = ""):
    zin = zin.replace(" ", "")
    print(zin)
    zin2 = ""
    for i in range(1, (len(zin) // 5) + 2):
        zin2 += zin[(i - 1 )*5: i*5] + " "
    return zin2


print(blok_tekst("Een korte maar wel een echte zin"))