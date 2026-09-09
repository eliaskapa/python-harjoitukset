#mod08 esimerkkejä

import random
"""
viikonpaivat = "maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"
print(viikonpaivat)
print("ensimmäinen viikonpäivä on", viikonpaivat[0]) 

# monikko monikon sisällä (kaksi- tai moniulotteinen monikko)
print("\narkipäivät ja viikonlopun päivät ovat omissa monikoissaan samassa monikossa")
viikonpaivat_2 = (("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai"), ("lauantai", "sunnuntai"))
print(viikonpaivat_2)
print("arkipäivät ovat: ", viikonpaivat_2[0])
print("viikonlopun päivät ovat: ", viikonpaivat_2[1])
print("ensimmäinen arkipäivä on. ", viikonpaivat_2[0][0])

# yksittäisten arvojen purku muuttujiin (pitää vastata määrässä)
(eka, toka, kolmas, nejäs, viides, kuudes, seitsemäs) = viikonpaivat
print(eka, kolmas, viides, seitsemäs)

## monikko ja funktio (esimerkiksi materiaalista)

print("\nTuplanoppa")

def heitä():
    # luodaan kaksialkiomonikko ja palautetaan se suoraan
    return (random.randint(1, 6), random.randint(1, 6))

nopat = heitä()
print(f"Nopista tuli {nopat [0]} ja {nopat [1]}.")

print("\nJoukkoja")
viikonpaivat = {"maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai" }
print(viikonpaivat)

viikonpaivat.add("extrapäivä")
viikonpaivat.add("extrapäivä")
for paiva in viikonpaivat:
    print(paiva)
viikonpaivat.remove("keskiviikko")
print(viikonpaivat)

numerot = {"Viivi": "050-1234567",
           "Ahmed": "040-1112223",
           "Pekka": "050-7654321"}
#avaimet on uniikkeja ja niitä verrataan arvoihin
numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

#sama arvo voi toistua
numerot["Pekka"] = "poistettu"
numerot["Ahmed"] = "050-9123456"

print(numerot)
print("olgan numero on", numerot ["Olga"])
nimi = input("Anna nimi: ")
if nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")

print("olgan numero on", numerot ["Olga"])
#if lauseessa voi testata esiintyykö avain sanakirjassa
#if nimi in numerot
"""

#sisäkkäiset tietorakenteet

print("\nEsimerkki pelaajien mahdollisesta tietorakenteesta jossain moninpelissä")

players = [
    {
        "name": "player1",
            "skill_level": 10,
            "inventory": {"map", "knife"}
    },
    {
            "name": "player2",
            "skill_level": 20,
            "inventory": {"axe"}
    }
]

#tulostetaan pelaajien tiedot

for player in players:
    print(player)
    print(f"pelaajan {player["name"]} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")