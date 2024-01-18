import datetime

def alle_pos_getallen(getallen):
    for getal in getallen:
        if not (isinstance(getal, (int, float)) and getal >= 0): 
            return False
    return True

print(alle_pos_getallen([5,12.45,1000,27.4,0]))
print(alle_pos_getallen([5,"12.45",1000,27.4,0]))
print(alle_pos_getallen([5,12.45,1000,-27.4,0]))

print()

def som_lijsten(lijst1, lijst2):
    nieuwe_lijst = []
    if alle_pos_getallen(lijst1) and alle_pos_getallen(lijst2) and len(lijst1) == len(lijst2):
        for i in range(len(lijst1)):
            nieuwe_lijst.append(lijst1[i]+lijst2[i])
    return nieuwe_lijst

print(som_lijsten([1,2,3],[4,5,6,7]))
print(som_lijsten([1,2,3],[4,5,6]))
print(som_lijsten(["1","2","3"],["4","5","6"]))

print()

def dag_van_de_week(dag):
    match dag:
        case "maandag":
            return 1
        case "dinsdag":
            return 2
        case "woensdag":
            return 3
        case "donderdag":
            return 4
        case "vrijdag":
            return 5
        case "zaterdag":
            return 6
        case "zondag":
            return 7
        case _ :
            return False
        
print(dag_van_de_week("donderdag"))
print(dag_van_de_week("luiedag"))

print()

class Webshop:
    def __init__(self, naam, jaartal = None , verkoopcijfers_per_week = None) -> None:
        self.naam = naam
        self.jaartal = jaartal
        if not self.jaartal:
            self.jaartal = datetime.date.today().year

        if verkoopcijfers_per_week:

            for verkoopcijfers in self.verkoopcijfers_per_week.values():
                aantal_juiste_cijfers = 0
                if alle_pos_getallen(verkoopcijfers) and len(verkoopcijfers) == 7:
                    aantal_juiste_cijfers += 1
                if aantal_juiste_cijfers == len(verkoopcijfers_per_week):
                    self.verkoopcijfers_per_week = verkoopcijfers_per_week
        else:
            self.verkoopcijfers_per_week = {}

    def voeg_week_toe(self, nummer, verkoopcijfers) -> None:
        if alle_pos_getallen(verkoopcijfers) and len(verkoopcijfers) == 7:
                self.verkoopcijfers_per_week[nummer] = verkoopcijfers
    
    def __str__(self) -> str:
        verkoop_cijfers = ""
        for nummer, cijfers in self.verkoopcijfers_per_week.items():
            verkoop_cijfers += f"\nweek{nummer}:\t{cijfers}"
        string = f"Naam = {self.naam}\nJaartal = {self.jaartal}\nverkoopcijfers = {verkoop_cijfers}"
        return string

    def geef_week_gemiddelde(self, weeknummer):
        if weeknummer in self.verkoopcijfers_per_week.keys():
            return f"{round(sum(self.verkoopcijfers_per_week[weeknummer]) / len(self.verkoopcijfers_per_week[weeknummer]),2)}"
        else:
            return "geen gegevens beschikbaar"
    
    def geef_dag_gemiddelde(self, dag):
        dag = dag_van_de_week(dag)
        if dag:
            som = [0 for i in range(7)]
            for weken in self.verkoopcijfers_per_week.values():
                som = som_lijsten(som, weken)
            return round(som[dag - 1] / len(self.verkoopcijfers_per_week.values()),2)
        else:
            return "geen gegevens beschikbaar"
        
    def __add__(self, other):
        if isinstance(other, Webshop) and self.jaartal == other.jaartal and self.naam == other.naam:
            weken_te_verwijderen = []
            for keys_self in self.verkoopcijfers_per_week:
                for keys_other in other.verkoopcijfers_per_week:
                    if keys_self == keys_other:
                        self.verkoopcijfers_per_week[keys_self] = som_lijsten(self.verkoopcijfers_per_week[keys_self], other.verkoopcijfers_per_week[keys_other])
                        weken_te_verwijderen.append(keys_other)
            
            for weken in weken_te_verwijderen:
                del other.verkoopcijfers_per_week[weken]
            self.verkoopcijfers_per_week.update(other.verkoopcijfers_per_week)
            return self.__str__()



week9 =[1245.67,1490.07,1679.87,2371.46,1783.92,1461.99,2059.77]
week10 =[2541.36,2965.88,1965.32,1845.23,7021.11,9652.74,1469.36]
week13 =[2513.45,1963.22,1568.35,1966.35,1893.25,1025.36,1128.36]
week16 =[2589.55,1970.26,1468.70,1950.05,3800.25,1250.16,1111.16]
week17 =[5500.56,5065.80,5565.32,-5545.23,5021.11,5530.60,5485.12]

webshop = Webshop("bol.com")
webshop.voeg_week_toe(9, week9)
webshop.voeg_week_toe(10, week10)
webshop.voeg_week_toe(13, week13)
webshop.voeg_week_toe(16, week16)
webshop.voeg_week_toe(17, week17)
print(webshop)

print()

print(webshop.geef_week_gemiddelde(16))
print(webshop.geef_dag_gemiddelde("zondag"))

print()

week4 = [4,4,4,4,4,4,4]
week10 = [100_000, 100_000, 100_000, 100_000, 100_000, 100_000, 100_000, ]
webshop2 = Webshop("bol.com")
webshop2.voeg_week_toe(4, week9)
webshop2.voeg_week_toe(10, week10)
print(webshop + webshop2)