import math
import random
"""
suorita = True

while suorita:
    print("Tämä on printtaantuu vain kerran")
    suorita = False

print ("suoritus loppui")

luku = int(input("luku tähän: "))                 #alkuarvo / kierrosmuuttuja

while luku >= 1:           #ehto
    print(luku)
    luku -= 1              #muuuttjuan arvon muutaminen

    #print ("jatketaan ohjelmaan")

Salasana = input("Anna salasana (python): ")

while Salasana != "python":
    print("Väärä salasana")
    Salasana = input("Anna salasana uudestaan (python): ")

print("tere tulemast")


# while / else rakenne
# suoritus siirtyy else-haaraan kun toistoehto on epätosi
# ei suoriteta jos poistutaan break-lauseella
# else rakenne on harvemmin käytetty

komento = input("anna komento (lopeta, APUA): ").strip().lower()

while komento != "lopeta":
    if komento == "APUA":
        break
    print("annoit komennon: ", komento)
    komento = input("anna uusi komento: ")
else:
    print("annoit käskyn lopeta")

print("ohjelma jatkuu")


noppa1 = noppa2 = heitot = 0

while (noppa1 != 6 and noppa2 != 6):
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print (noppa1, noppa2)
    heitot = heitot + 1

print(f"tarvittiin  {heitot:d} heittoa")

#sama nopaneheitto uudestaan, nyt sisäkkäisellä toistorakenteella

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka-toka:d}")
        toka = toka + 1
eka = eka + 1


heitot = 0
pelikerta = 0
while pelikerta < 1000:
    noppa1 = noppa2 = 0
    while (noppa1 != 6 and noppa2 != 6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        print (noppa1, noppa2)
        heitot = heitot + 1

    pelikerta += 1



print ("pelikertoja meillä oli:", pelikerta)
print(f"tarvittiin {heitot:d} heittoa")
print(f"jokaisella kierroksella oli keskimäärin {heitot/pelikerta} heittoa")

# tehtävä 1

luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1
    

# tehtävä 4 modattuna (tee tehtävä loppuun)
oikea_numero = 7
arvaus = int(input("arvaa numero 1-10: "))

while arvaus != oikea_numero:
    print("väärin")
    arvaus = int(input("arvaa numero 1-10"))



print (f"oikea numero oli tosiaan {oikea_numero}")
"""
#usein while rakenttetta käytettään ja varsinkin teidän projeceteissa!!
# ns. pääsilmukka eli main loop

peli_käynnistyy = True
#main loop
while peli_käynnistyy:
    print("tere tulemasta peliini (j tai l) eli jatka tai lopeta")
    # j jatkaa peli' ja l lopettaa
    valinta = input("anna komento: ")
    if valinta == "j":
        print("jatkoit peliä")
    if valinta == "l":
        peli_käynnistyy = False
    