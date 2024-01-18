def ampm(tijd = ""):
    if tijd.endswith("AM") or tijd == "12PM":
        tijd = f"{tijd[:-2]}u"

    elif tijd.endswith("PM"):
        tijd = int(tijd[:-2])
        tijd += 12

    elif tijd.endswith("u"):
        tijd = int(tijd[:-1])
        if tijd == 12:
            tijd = "12PM"
        elif tijd >= 0 and tijd <= 11:
            tijd = f"{tijd}AM"
        else:
            tijd = f"{tijd-12}PM"
    return tijd
print(ampm("8AM"))
print(ampm("4PM"))
print(ampm("21u"))
print(ampm("12u"))