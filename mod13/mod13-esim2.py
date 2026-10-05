import json

class Player:
    def __init__(self,age):
        self.age = age
        self.pisteet = 0
    def go_forward(self):
        self.pisteet += 1
        print("pisteitä on nyt", self.pisteet)
    def info(self):
        print(f"Pelaajan ikä on {self.age} ja pisteet {self.pisteet}")

    def save_game(self):
        while True:
            try:
                with open("mod13/save.txt", "w") as file:
                    data = {"age": self.age, "points": self.pisteet,}
                    json.dump(data, file)

            except IOError:
                print("Tiedoston käsittelyssä ")
            except FileNotFoundError:
                print("tiedostoa ei löydy")

    def load_game(self):
        while True:
            try:
                with open("mod13/save.txt", "w") as file:
                    data = json.load(file)
                    print("latattu tai tallennettu tiedosto", data)
                    self.age = data["age"]
                    self.points = data["points"]
            except IOError:
                print("Tiedoston käsittelyssä ")
            except FileNotFoundError:
                print("tiedostoa ei löydy")
            

def start_game():
    game_running = True
    while game_running: 
        command = input("Anna komento: ")
        if command == "tallenna":
            player.save_game()
            print("tallennettu")
        elif command == "lataa":
            player.load_game
            player.info
        elif command == "etene":
            player.go_forward()
        elif command == "lopeta":
                game_running = False
        else:
            print("virheellinen komento")

print("Peli alkaa")

age = 0

while True:
    try:
        age = int(input("anna pelaajan ikä "))
        break

    except ValueError:
        print("Virheellinen syöte ei ole kokonaisluku")

print(f"pelaajan ikä on: {age}")
print("ohjelman suoritus loppui")

if age > 11:
    player = Player(age)
    start_game()
    