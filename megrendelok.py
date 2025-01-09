import megrendel
from megrendel import Megrendeles

def beolvas(fajlnev):
    megrendelesek = []
    with open(fajlnev, "r", encoding="utf-8") as fajl:
        fajl.readline()  
        for sor in fajl:
            email, rendeles = sor.strip().split("$")
            megrendelesek.append(megrendel(email, rendeles))
    return megrendelesek

def rendeles_szam(megrendelesek):
    return len(megrendelesek)