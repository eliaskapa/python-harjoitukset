print("\nEsimerkki pelaajien mahdollisesta tietorakenteesta jossain moninpelissä")

players = [
    {
        "name": "Player 1",
        "skill_level": 10,
        "inventory": {"map", "knife"}
    },
    {
        "name": "Player 2",
        "skill_level": 20,
        "inventory": {"axe"}
    }
]

# Tulostetaan pelaajien tiedot
#print(players)
for player in players:
    #print(player)
    print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")

#miten kuvata tätä luokkana esim pelaaja?

