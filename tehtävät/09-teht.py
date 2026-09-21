import math
import random
#tehtävä 1

"""class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka


auto = Auto("ABC-123", 142)

print(auto.nopeus, auto.rekisteritunnus, auto.nopeus, auto.kuljettu_matka)

#tehtävä 2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, vauhdin_kasvu):
        self.nopeus += vauhdin_kasvu
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.nopeus - 200
            print("jarrutus")
        if self.nopeus < 0:
            self.nopeus = 0
            print("0 minimi")
    

auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(auto.huippunopeus, auto.rekisteritunnus, auto.nopeus)

#tehtävä 3

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, vauhdin_kasvu):
        self.nopeus += vauhdin_kasvu
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.nopeus - 200
        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, aika):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * aika

auto = Auto("ABC-123", 142, kuljettu_matka=2000)
auto.kiihdytä(60)
auto.kulje(1.5)

print(auto.huippunopeus, auto.rekisteritunnus, auto.nopeus, auto.kuljettu_matka)

#tehtävä 4 """

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, vauhdin_kasvu):
        self.nopeus += vauhdin_kasvu 
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.kuljettu_matka += self.nopeus * aika

Autot = []

for i in range(1,11):
    tunnus = f"ABC-{i}"
    huippunopeus = random.randint(100,200)
    autoX = Auto(tunnus, huippunopeus)
    Autot.append(autoX)

kisa = True

while kisa:
    for auto in Autot:
        vauhdin_muutos = random.randint(-10, 15)
        auto.kiihdytä(vauhdin_muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 1000:
            print("kisa on ohi ", auto.rekisteritunnus, "voitti")
            kisa = False

print("\nAutot kilpailun jälkeen:")

for auto in Autot:
    print(
        f"{auto.rekisteritunnus}: "
        f"huippunopeus {auto.huippunopeus} km/h, "
        f"nopeus {auto.nopeus} km/h, "
        f"matka {auto.kuljettu_matka} km"
    )