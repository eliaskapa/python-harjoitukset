#tuntiesimerkkejä moduuliin 4
import random
#kolikonheitto simulaattori

rng = random.randint(0,1)

print(rng)
# if lauseen ehto muodostuu AINA True tai False arvoksi
# jos ehto on tosi suoritetaan if koodilohko, muuten else-lohko

if rng == 0:
    tulos = "naama"
    print("naama tuli")
else: 
    tulos = "numero"
    print("numero tuli")

print(f"heitit kolikkoa ja sait {tulos}n.")

#boolean
onko_totta = False

if onko_totta:
    print("onhan se totta!")

##kolikonheitto simulaattori 2
#kolikko pystyyn tod.näk oikeasti jotain 1/6000?

rng = random.random()
print(rng) #liukulukuarvo väliltä 0-1

#kolikko jää pystyyn
if rng < 0.01:
    print("kolikko jäi pystyyn")
elif rng < 0.505:
   print("numero tuli.")
else:
    print ("naama tuli")

### erilaisia ehtoja
arvo = 150
print(90 < arvo < 110)
print(100 != 101)


ikä = int(input("anna ikä: "))
if 15 <=ikä < 18:
    paino = float(input("anna paino (kg): "))

if ikä >= 18 or ikä >= 15 and paino >= 55:
    print("Lääkkeen käyttä on sallittua.")
else: print("haista kakke")

# esimerkki ehdoista (jälkimmäinen if lause) ikäarvolta 18
#print (true or (true and false))

print (True or (True and False))
