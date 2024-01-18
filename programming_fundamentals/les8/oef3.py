def theorie1(theorie, practicum):
    if practicum < theorie:
        return practicum
    else:
        gemiddeld = (practicum + theorie) / 2
        return gemiddeld
    
print(theorie1(7,5))
print(theorie1(7,9))


def theorie2(theorie, practicum):
    gemiddeld = (practicum + theorie) / 2
    return practicum if practicum < theorie else gemiddeld

    
print(theorie2(7,5))
print(theorie2(7,9))