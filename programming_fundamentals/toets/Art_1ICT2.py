def geldige_parameter(woord):
    '''Gaat na of een ingegeven woord een parameter voorstelt'''

    geldig = woord.startswith("?") and (woord[1:].upper() == woord[1:]) and (len(woord) > 1)
    
    return "Dit is een correcte parameter" if geldig else "Dit is geen correcte parameter"


def zoek_parameter(template):
    '''deze functie zoekt een parameter in een meegegeven template en geeft de eerste parameter terug mee, als er geen parameter in zit geeft hij False terug'''
    
    template = template.split(" ")
    parameter = ""
    for woord in template:
        parameter = woord if (woord.find("?") == 0) else parameter

    return parameter if (geldige_parameter(parameter) == "Dit is een correcte parameter") else False


def personaliseer_template(template, waarde):
    '''vervangt de parameter in het template met waarde'''
    
    parameter = zoek_parameter(template) if zoek_parameter(template) else False
    template = template.replace(parameter, waarde) if parameter else template

    return template


def personaliseer_template2(template):
    '''vervangt meerdere parameters in het template met een gekozen waarde'''

    while zoek_parameter(template):
        parameter = zoek_parameter(template) if (zoek_parameter(template)) else False
        waarde = input(f"geef een waarde voor {parameter}: ")
        template = template.replace(parameter, waarde) if parameter else template
    
    return template


woord = input("Geef een parameter: ")
print(geldige_parameter(woord))

woord = input("Geef een parameter: ")
print(geldige_parameter(woord))



template1 = "Hier zit een ?PARAMETER in"
print(zoek_parameter(template1))
print(zoek_parameter("Wat als er geen parameter in zit ?  "))



print(personaliseer_template(template1, "lol"))
template1 = "Hier zit een PARAMETER in"
print(personaliseer_template(template1, "lol"))



template2 = "Beste ?ONTVANGER ik geniet momenteel van een welverdiende vakantie, Ik ben terug op ?DATUM grtjs ?AFZENDER Odisee campus Gent."
print(personaliseer_template2(template2))