class Julkaisu:
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
