import datetime

def inschrijven():
    naam = input("geef jouw voornaam: ")
    geboortejaar = int(input("geef jouw geboortejaar: "))

    leeftijd = int(datetime.datetime.today().year) - geboortejaar

    if leeftijd < 6:
        string = f"{naam}, je bent nog iets te jong. Binnen {6 - (leeftijd)} jaar ben je van harte welkom!"
    else:
        if leeftijd <= 8:
            groep = "Premicroben"
        elif leeftijd <= 10:
            groep = "Microben"
        elif leeftijd <= 12:
            groep = "Benjamins"
        elif leeftijd <= 14:
            groep = "Pupillen"
        elif leeftijd <= 16:
            groep = "Miniemen"
        elif leeftijd <= 18:
            groep = "Cadetten"
        elif leeftijd <= 21:
            groep = "Juniores"
        else:
            groep = "Seniores"
        string = f"{naam}, welkom bij de {groep}!"
    print(string)
    
inschrijven()
