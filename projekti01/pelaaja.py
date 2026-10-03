class Pelaaja:
    def __init__(self, nimi, tavaraluettelo, sijainti):
        self.nimi =  nimi
        self.tavaraluettelo = []
        self.sijainti = sijainti

    def liiku(self, eri_huone):
        self.sijainti = eri_huone

    def nappaa_esine(self, esine):
        self.tavaraluettelo.append(esine)
        print(f"{esine} lisättiin inventaarioon")