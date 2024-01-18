import string as s

def eerste_karakter(woord):
    if woord[0].isdigit():
        return "cijfer"
    elif woord[0].isupper():
        return "hoofdletter"
    else:
        return "kleine letter"
print(eerste_karakter("Hallo"))

def aantal_hoofdletters(zin):
    hoofdletters = 0
    for letters in zin:
        if letters.isupper():
            hoofdletters += 1
    return hoofdletters

print(aantal_hoofdletters("Ik Ben Art"))

def upper_or_lower(zin):
    if len(zin) % 2 == 0:
        return zin.upper()
    else:
        return zin.lower()

print(upper_or_lower("Ik Ben Art"))

def panagram(zin = ""):
    lettersGevonden = 0
    for letter in s.ascii_letters:
        if zin.find(letter) != -1:
            lettersGevonden += 1
    return lettersGevonden == 26

print(panagram("qwertyu iopasdfghjklzxcvbnm"))

def maand(maandNummer):
    match maandNummer:
        case 1:
            return "januari"
        case 2:
            return "februari"
        case 3:
            return "maart"
        case 4:
            return "april"
        case 5:
            return "mei"
        case 6:
            return "juni"
        case 7:
            return "juli"
        case 8:
            return "augustus"
        case 9:
            return "september"
        case 10:
            return "oktober"
        case 11:
            return "november"
        case 12:
            return "december"
        
print(maand(1))


def maand_naam(maand):
    match maand:
            case "januari":
                return 1
            case "februari":
                return 2
            case "maart":
                return 3
            case "april":
                return 4
            case "mei":
                return 5
            case "juni":
                return 6
            case "juli":
                return 7
            case "augustus":
                return 8
            case "september":
                return 9
            case "oktober":
                return 10
            case "november":
                return 11
            case "december":
                return 12

print(maand_naam("januari"))


def kortste_string():
    string = input("geef een woord: ")
    kortste = string

    while string != "stop":
        string = input("geef een woord: ")
        if string != "stop":
            kortste = string if kortste > string else kortste
            
    return kortste
print(kortste_string())

