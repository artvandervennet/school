import random

def blad_steen_schaar():

    bezig = True

    while bezig:
        computer = random.randint(1,3) # 1=blad, 2=steen, 3=schaar
        speler = input("kies blad, steen of schaar: ")

        if speler == "blad":
            if computer == 1:
                print("de computer koos blad")
                print("gelijkspel")
            if computer == 2:
                print("de computer koos steen")
                print("je hebt gewonnen")
            if computer == 3:
                print("de computer koos schaar")
                print("je hebt verloren")
            bezig = False

        if speler == "steen":
            if computer == 1:
                print("de computer koos blad")
                print("je hebt verloren")
            if computer == 2:
                print("de computer koos steen")
                print("gelijkspel")
            if computer == 3:
                print("de computer koos schaar")
                print("je hebt gewonnen")
            bezig = False

        if speler == "schaar":
            if computer == 1:
                print("de computer koos blad")
                print("je hebt gewonnen")
            if computer == 2:
                print("de computer koos steen")
                print("je hebt verloren")
            if computer == 3:
                print("de computer koos schaar")
                print("gelijkspel")
            bezig = False

blad_steen_schaar()