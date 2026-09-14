import random
import math
#tehtävä 1
"""
def heitä_noppaa():
    return random.randint(1, 6)

while True:
    silmäluku = (heitä_noppaa())
    print(silmäluku)
    if silmäluku == 6:
        print("sait kutosen")
        break


#tehtävä 2
tahko_lkm = int(input("anna nopan puolien määrä: "))

def heitä_noppaa(tahko_lkm):
    return random.randint(1, tahko_lkm)

while True:
    silmäluku = (heitä_noppaa(tahko_lkm))
    print(silmäluku)
    if silmäluku == tahko_lkm:
        print("sait maksimin")
        break

#tehtävä 3
gallona = int(input("anna bensiinin määrä (gallonina)"))
def bensiinin_määrä(gallona):
    return gallona * 3.785

while bensiinin_määrä(gallona) > 0:
    print(f"bensiinin määrä on {bensiinin_määrä(gallona)} litraa")
    gallona = int(input("anna bensiinin määrä (gallonina)"))
    if bensiinin_määrä(gallona) < 0:
        print("loppu")


#tehtävä 4: Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


def lista(numerot):
    return sum(numerot)
numerot = [1, 3, 5, 7]

tulos = lista(numerot)

print(tulos)



#tehtävä 5

def lista(numerot):
    parilliset = []
    for luku in numerot:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

lista1 = [1, 2, 3, 4, 5, 6]

lista2 = lista(lista1)

print(f"normaali lista: {lista1}")

print(f"uusi lista: {lista2}")

#tehtävä 6 

def yksikköhinturi(kokocm, hinta):
    r = kokocm / 100 / 2
    alue = math.pi * r**2 
    return hinta / alue

yksikköhinnat = []

N = int(input("anna pitsojen määrä: "))

for Pitsa in range(N):
    halkaisija = float(input("Anna pitsan halkaisija: "))
    hinta = float(input("Anna pitsan hinta: "))
    yksikköhinta = yksikköhinturi(halkaisija, hinta)
    yksikköhinnat.append(yksikköhinturi(halkaisija, hinta))
    print(f"{Pitsa+1} pitsan yksikköhinta (euroina/m2): {yksikköhinnat[Pitsa]:0.0f}")

min(yksikköhinnat)

yksikköhinnat.index(min(yksikköhinnat))



def noppapeli():
    return random.randint(1,6)

while True:
    noppa = noppapeli()
    print(noppa)
    if noppa == 6:
        print("loppu")
        break

tahko = int(input("anna tahkot"))
def noppapeli():
    return random.randint(1, tahko)

while True:
    noppa = noppapeli()
    print(noppa)
    if noppa == tahko:
        print("loppu")
        break


def bensa(gallonat):
    litra = gallonat * 3.78
    return litra

while True: 
    määrä = float(input("gallona määrä: "))
    if määrä < 0:
        break

litrat = bensa(määrä)
print(litrat)
"""
def bensa(gallonat):
    litra = gallonat * 3.785  
    return litra

while True: 
    määrä = float(input("gallona määrä: "))
    if määrä < 0:
        break

    # Korjaus 2: Nämä rivit pitää sisentää (siirtää sisäänpäin), 
    # jotta ne suoritetaan silmukan sisällä joka kierroksella.
    litrat = bensa(määrä)
    print(litrat)








