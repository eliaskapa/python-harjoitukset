#tehtävä 1 (sovellettuja)
import random
import math
"""
def heitä_noppaa():
    return random.randint(1, 6)
silmaluku = heitä_noppaa()

while silmaluku != 6:
    silmaluku = heitä_noppaa()
    print(silmaluku)

#tehtävä 2 

def heitä_noppaa():
    return random.randint(1,nopan_koko)

nopan_koko = int(input("anna nopan koko (maksimi määrä): "))

silmaluku = heitä_noppaa()
while silmaluku != nopan_koko:
    silmaluku = heitä_noppaa()
    print(silmaluku)

def heitä_noppaa(noppaK):
    return random.randint(1, noppaK)

def noppapeli():
    noppaK = int(input("anna nopan koko (maksimi määrä): "))
    silmaluku = 0
    heittolaskuri = 0
    while silmaluku != noppaK:
        heittolaskuri += 1
        silmaluku = heitä_noppaa(noppaK)
        print(silmaluku)
    print(f"heitettäessä {noppaK}-tahkoista, meni {heittolaskuri} heittoa jotta sai maksimin")


while True:
    komento = input("anna komento>> ")
    if komento == "lopeta":
        print("heippa!")
        break
    if komento == "noppa":
        noppapeli()
    else: 
        print("en ymmärtänyt")
"""
#tehtävä 6

def calculate_unit_price(diamater_in_cm, price):
    # pinta-ala: pi * r*r
    r = diamater_in_cm/100/2
    area = math.pi * r**2
    print(area)
    # eur/m2
    return

calculate_unit_price(100, 10)