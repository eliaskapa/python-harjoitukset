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
    # eur/m2
    return price / area

unit_prices = []

for pizza_number in range(2):
    diameter = float(input(f"anna {pizza_number+1} pitsan halkaisija (cm): "))
    price = float(input(f"anna {pizza_number+1} pitsan hinta (euro):"))
    unit_price = calculate_unit_price(diameter, price)
    unit_prices.append(calculate_unit_price(diameter, price))
    print(f" {pizza_number+1} pitsan yksikkö hinta (euro/m2): {unit_prices[pizza_number]:0.2f}")

if unit_prices[0] < unit_prices[1]:
    print("esimmäinen pitsa on halvempi.")
elif unit_prices[1] < unit_prices[0]:
    print("toinen pitsa on halvempi.")
else: 
    print("pitsat ovat saman hintaisia")

# TODO EXTRA: miten kehittää ohjelmaa niin, että se toimii N määrällä pitsoja. 
