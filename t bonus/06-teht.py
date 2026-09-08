import random
"""
#tehtävä 1 "Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta."

määrä = int(input("anna arpakuutioiden määrä: "))

summa = 0

for i in range(määrä):
    heitto = random.randint(1, 6)
    summa += heitto

print(f"summa on {summa}")



#tehtävä 2: Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista-
# viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

jono = []

while True:
    luku = input("anna luku: ")
    if luku == "":
        print()
        print("järjestellään")
        print()
        break
    jono.append(luku)


jono.sort(reverse=True)

for luku in jono[:5]:
    print(luku)
"""

#TEHTÄVÄ 3 kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

k_luku = int(input("anna kokonaisluku: "))

if k_luku > 1:
    for i in range(2, k_luku):
        if k_luku % i == 0:
                print("ei ole alkuluku")
                break
        if k_luku % i != 0:
            print("on alkuluku")
            break

            