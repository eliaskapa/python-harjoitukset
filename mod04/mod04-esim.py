#tuntiesimerkkejä moduuliin 4

import random

#kolikonheitto simulaattori

rng = random.randint(0,1)

print(rng)

if rng == 0:
    tulos = "naama"
    print("naama tuli")

if rng == 1: 
    tulos = "numero"
    print("numero tuli")

print(f"heitit kolikkoa ja sait {tulos}n.")

#boolean
onko_totta = False

if onko_totta:
    print("onhan se totta!")
