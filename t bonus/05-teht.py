import math
import random
"""
luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

#tehtävä 2

while True:
    Tuumat = float(input("anna tuumat"))
    if Tuumat < 0:
        print("ohi")
        break
    cm = Tuumat * 2.54
    print(f"{Tuumat} tuumat on {cm} cm")

#tehtävä 3

luvut = []

while True:
    numerot = input("anna numerot")
    if numerot == "":
        break
    luku = float(numerot)
    luvut.append(luku)
if len(luvut) > 0:
    print(f"pienin luku on {min(luvut)}")
    print(f"suurin luku on {max(luvut)}")
else:
    print("ei ollut lukua")


#tehtävä 4

oikea_luku = random.randint(1,10)

while True:
    arvaus = int(input("arvaa numero 1-10: "))
    if oikea_luku > arvaus:
        print("ali")
    if oikea_luku < arvaus:
        print("yli")
    if oikea_luku == arvaus:
        print("oikea arvaus")
        break
"""
#tehtävä 5

User = "python"
PW = "rules"
k_yritys = 0

while k_yritys <= 5:
    User_Y = input("anna käyttäjä: ")
    PW_Y = input("anna salis: ")

    if User_Y == User and PW_Y == PW:
        print("tervetuloa")
        break
    k_yritys += 1
if k_yritys == 6:
    print("pääsy evätty")

#tehtävä 6





    




