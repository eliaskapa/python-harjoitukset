import math
import random

#osa 1
""""
pituus = int(input("Kerro kuhan pituus senttimetreinä: "))

if pituus < 37:
    print("Heitä se taisin järveen")

elif pituus >= 37:
    print("nauti kuhastasi")
"""
#osa 2
"""
hytti = input("Mistä hytti luokasta haluat tietää?: ")

if hytti == "A":
    print("A on ikkunnallinen hytti autokannen yläpuolella")
elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else :
    print("Virheellinen hytti luokka")
"""
#Osa 3

sukupuoli = input("sex: ")
hemoarvo = input("hemoarvosi: ")

if sukupuoli == "N" and (hemoarvo <= 117 or >= 175):
    print("hemoarvosi on normaali")

