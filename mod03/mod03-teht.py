import math
import random

#tehtävä 1
#nimi = input ("anna nimesi:")
#print(f"terve, {nimi}!")

#tehtävä 2
r = float(input("anna säde niin lasken ympyrän pinta-alan: "))
#r = float (r)
#print (r)

A = math.pi * r ** 2
print (f"ympyrän pinta-ala on {A:.2f}")


#tehtävä 3

A = float(input("anna suorakulmion kanta"))
B = float(input("anna suorakulmion korkeus"))

piiri = 2 * (A + B)
#piiri2 = 2 * a + 2 * B

print(f'suorakulmion piiri on: {piiri:.2f} ja pinta-ala {(A * B):3f}')

#tehtävä 6

luku = random.randint(0,9)
luku2 = random.randint(,9)
luku3 = random.randint(0,9)
print (f"{luku}, {luku2}, {luku3}")
print (f)