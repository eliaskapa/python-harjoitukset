class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)

class Hoitola:
    def __init__(self):
        self.koirat = []

    def koira_sisään(self, koira):
         self.koirat.append(koira)
         print(koira.nimi +  " kirjattu sisään")
         koira.hauku(2)


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()
hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)

def muokkaa_listaa(muokattava_lista):
    muokattava_lista.append(6)


hoitola.koira_sisään(Koira("Bella", 2016))

hoitola.koirat[0].hauku(2)