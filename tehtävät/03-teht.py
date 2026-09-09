import math
import random

#tehtävä 1

nimesi = input("kerro nimesi: ")

print(f"terve {nimesi}")

#tehtävä 2
Säde = float(input("mikä on ympyrän säde?: "))

Pintaala = Säde * Säde * math.pi

print(f"ympyrän pinta-ala on: {Pintaala}")


#tehtävä 3

kanta = (int(input("mikä on suora kulmion kanta: ")))

korkeus = (int(input("mikä on suora kulmion korkeus: ")))

pintaala = kanta * korkeus

piiri = (kanta + korkeus) * 2

print(f"pintaala on {pintaala}")

print("piiri on ", piiri)


#tehtävä 4

luku = int(input("anna luku 1: "))

luku2 = int(input("anna luku 2: "))

luku3 = int(input("anna luku 3: "))

print(luku)
print(luku2)
print(luku3)

summa = luku + luku2 + luku3

ka = (luku + luku2 + luku3) / 3

tulo = luku * luku3 * luku2

print("summa on: ", summa)

print("ka on: ", ka)

print("tulo on: ", tulo)

#tehtävä 5

leiviskät_m = float(input("anna leiviskät "))
naulat_m = float(input("anna naulat "))
luodit_m = float(input("anna luodit "))

naulat_m = leiviskät_m * 20 + naulat_m
luodit_m = naulat_m * 32 + luodit_m


grammat = luodit_m * 13.3

kilot = grammat // 1000
grammat = grammat % 1000

print(f"paino on {kilot:.0f} kiloa ja {grammat:.1f} grammaa")

# tehtävä 6

num1 = random.randint(1,9)
num2 = random.randint(1,9)
num3 = random.randint(1,9)

print(num1, num2, num3)