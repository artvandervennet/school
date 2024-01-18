def kleinste_kwadraad():
    ingegeven = int(input("geef een getal: "))

    i = 1
    uitkomst = 1
    string = ""
    while uitkomst < ingegeven:
        uitkomst = i**2
        string += f"{i}^2 = {uitkomst}, "
        i += 1
    print(string)
kleinste_kwadraad()
