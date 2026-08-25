import math
import random

#tehtävä 1
#nimi = input ("anna nimesi:")
#print(f"terve, {nimi}!")

#tehtävä 2
#r = float(input("anna säde niin lasken ympyrän pinta-alan: "))
#r = float (r)
#print (r)
"""
A = math.pi * r ** 2
print (f"ympyrän pinta-ala on {A:.2f}")


#tehtävä 3

A = float(input("anna suorakulmion kanta"))
B = float(input("anna suorakulmion korkeus"))

piiri = 2 * (A + B)
#piiri2 = 2 * a + 2 * B

print(f'suorakulmion piiri on: {piiri:.2f} ja pinta-ala {(A * B):3f}')
"""
#tehtävä 5

leiviskä_lkm = float(input("anna leivisköjen määrä "))
naulat_lkm = float(input("anna naulojen määrä "))
luodit_lkm = float(input("anna luotien määrä "))

naulat_lkm = leiviskä_lkm * 20 + naulat_lkm
luodit_lkm = naulat_lkm * 32 + luodit_lkm

print("koko massa luoteina: ", luodit_lkm)

massa_g = luodit_lkm * 13.3

print(f"massa nykymittojen mukaan: {massa_g // 1000:.0f} kiloa ja {massa_g % 1000:.2f} grammaa. ")


#tehtävä 6
"""
luku = random.randint(0,9)
luku2 = random.randint(,9)
luku3 = random.randint(0,9)
print (f"{luku}, {luku2}, {luku3}")
print (f)
"""