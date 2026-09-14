"""


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
"""

class Player:
    def __init__(self, name, skill_level, inventory):
        self.name = name
        self.skill_level = skill_level
        self.inventory = inventory
        self.show_info = self.show_info

    def show_info(self):
        print(f"Pelaajan nimi: {self.name}")
        print(f"taso: {self.skill_level}")
        print(f"inventory: {self.inventory}")
        for item in self.inventory:
            print(item)
    def add_item(self, item):
        self.inventory.add(item)

        
                  

player1 = Player("Toni", 10, {"map", "knife"})
player2 = Player("Joni", 20, {"axe"})

#print(f"Pelaajan 1. nimi on {player1.name} taso on {player1.skill_level} ja inventory on {player1.inventory}")

player1.show_info()
#player2.show_info()
player1.add_item("key")
player1.show_info()
