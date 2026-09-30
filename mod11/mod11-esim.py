class Eläin:

    eläimet_lkm = 0

    def __init__(self, nimi, paino, syntymä_aika):
        self.nimi = nimi
        self.paino = paino
        self.syntymäaika = syntymä_aika

    def liiku(self):
        print(f"{self.nimi} liikkuu jotenkin jonnekkin..")

    def kaikki_tiedot(self):
        print("Nimi on", self.nimi,"ja painaa", self.paino/1000, "kg sekä on syntynyt",  self.syntymäaika )

class Peto:
    def __init__(self, on_metsästäjä):
        self.on_metsästäjä = on_metsästäjä

class Ilves(Eläin, Peto):
    def kilju(self):
        print(f"ilves {self.nimi} kiljuu ")
    def kaikki_tiedot(self):
        super().kaikki_tiedot()
    

class Karhu(Eläin, Peto):
    def __init__(self, nimi, paino, syntymä_aika, on_horroksessa, on_metsästäjä):
        self.on_horroksessa = on_horroksessa
        Eläin.__init__(self, nimi, paino, syntymä_aika)
        Peto.__init__(self, on_metsästäjä)

    def karju(self):
        print(f"karhu {self.nimi} karjuu ")
    def kaikki_tiedot(self):
        super().kaikki_tiedot()

class Eläintarha():
    def __init__(self, nimi):
        self.nimi = nimi
        self.eläimet = []

    def lisää_eläin(self,elain):
        self.eläimet.append(elain)

    def listaa_eläimet(self):
        print(f"kaikki eläimet {self.nimi},  kaikki eläimet (len{self.eläimet}) kpl")
        for Eläin in self.eläimet:
            Eläin.kaikki_tiedot()


tarha = Eläintarha("Korkeasaari")

uusi_eläin = Eläin("Joku Elukka", 1500, 2025)
#uusi_eläin.liiku()

ilves = Ilves("Joni", 63000, 2025)
#ilves.liiku()
#ilves.kilju()

karhu = Karhu("Nalle", 155000, 2018, False, True)
#print(karhu.on_horroksessa)
#karhu.karju()
#karhu.kaikki_tiedot()

kaikki_eläimet = [karhu, ilves, uusi_eläin]

tarha.lisää_eläin(Karhu("Isonalle", 200000, 2011, True, True))

tarha.lisää_eläin(ilves)
tarha.lisää_eläin(karhu)
tarha.lisää_eläin(uusi_eläin)


listaa_eläimet()
