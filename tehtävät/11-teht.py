"""class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
    def tulosta_tiedot(self):
        print(f"Lehti on {self.nimi}, {self.päätoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.sivumäärä = sivumäärä
        self.kirjoittaja = kirjoittaja
    def tulosta_tiedot(self):
            print(f"Kirja on {self.nimi}, {self.kirjoittaja}, {self.sivumäärä}")
    


Aku = Lehti("Aku Ankka", "Aki Hyyppä")
Hytti = Kirja("Hytti No6", "Rosa Liksom", "200")

Lehti.tulosta_tiedot(Aku)
Kirja.tulosta_tiedot(Hytti)
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

class Sähköauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akku,):
        super().__init__(rekisterinumero, huippunopeus)
        self.akku = akku

class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, bensatankki):
        super().__init__(rekisterinumero, huippunopeus)
        self.bensatankki = bensatankki
    
Tesla = Sähköauto("ABC-123", 180, 52.5)
Fiat = Polttomoottoriauto("ACD-123", 165, 32.3 )

Tesla.kiihdytä(100)
Fiat.kiihdytä(150)

Tesla.kulje(3)
Fiat.kulje(3)

print(Tesla.kuljettu_matka)
print(Fiat.kuljettu_matka)


