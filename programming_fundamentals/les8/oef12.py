import math

def reeks(x):
    e = math.e ** x
    term = 1
    i = 1
    berekende_e = 0.0
    while term >= 10**-6:
        berekende_e += term
        term =( x**i)/math.factorial(i)
        i += 1
    print(e)
    print(berekende_e)

reeks(10)