"""
class Auto:
    def __init__ (self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus =  0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, aika):
        self.kuljettu_matka += aika * self.nopeus
        

auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)

auto.kulje(2000)


print("auton rekisteritunnus on", auto.nopeus)
print("auton huippunopeus on", auto.huippunopeus)
print("auton nopeus on", auto.nopeus)
print("auton kuljettu matka on", auto.kuljettu_matka)

print("hoi")

"""
class Auto:
    def __init__ (self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus =  0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, aika):
        self.kuljettu_matka += aika * self.nopeus
        

auto = Auto("ABC-123", 142)

auto.kiihdytä(60)
auto.kulje(1.5)

print("auton rekisteritunnus on", auto.nopeus)
print("auton huippunopeus on", auto.huippunopeus, "km/h")
print("auton nopeus on", auto.nopeus, "km/h")
print("auton kuljettu matka on", auto.kuljettu_matka, "km")

print("hoi")
