class Hissi:
    def __init__(self, nimi, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nimi = nimi


    def siirry_kerrokseen(self, kohde_kerros):
        print("painettu nappia")
        while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylös(self,):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self,):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi("hissi", alin_kerros, ylin_kerros))

    def aja_hissiä(self, numero, kohdekerros):
         self.hissit[numero - 1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self,):
        print("palohälytys")
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin)
         

talo = Talo(2, 12, 3)

#talo.hissit[0].siirry_kerrokseen(5)
talo.aja_hissiä(1,5)
talo.aja_hissiä(1,7)
talo.aja_hissiä(2,9)
talo.palohälytys()




"""hissi1 = Hissi("Pääaula 1", 1, 12)
hissi2 = Hissi("Henkilökunnan hissi", 5, 20)

hissi1.siirry_kerrokseen(8)
hissi1.siirry_kerrokseen(4)
hissi1.siirry_kerrokseen(2)
hissi2.siirry_kerrokseen(9)
"""