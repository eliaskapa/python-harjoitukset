"""
k1_rotu = "Mastiffi"
k1_nimi =  "Wuffe"
k1_syntymävuosi = "2020"

k2_rotu = "bokseri"
k2_lissu = "lissu"
k2_syntymävuosi = "2023"

k3_rotu = "labradori"
k3_nimi = "sisu"
k3_syntymävuosi = "2019"

class Koira:
    pass

#luokkka on kuin suunnitelma ja olio sen perusteella rakennettu yksilö

koira = Koira()
koira2 = Koira()


koira.nimi = "Wuffe"
koira.rotu = "Mastiffi"

koira2.nimi = "Lissu"
koira2.rotu = "Bokseri"

print("ensimmäinsen koiran", koira.nimi)
print("ensimmäinsen koiran", koira.rotu)

print("toisen koiran", koira.nimi)
print("toisen koiran", koira.rotu)



#teimme juuri luokan Koira ilman ominaisuuksia
#tämän jälkeen määrittelemme ominaisuudet yksi kerrallaan = työlästä
#näin teemme oikeasti:

#Koira:

# Koiran ominaisuudet
# - Nimi
# - Rotu
# - Syntymävuosi

# Koiran toiminnot
# - hauku
# - syö
# - nuku

class Koira:
    tehty = 0

    def __init__(self, nimi, rotu, syntymävuosi, haukahdus = "wruf wruf"): # = "x" merkkaa oletus arvoa
        self.nimi = nimi                                                    #self viittaa arvoon luokan sisällä
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = "nisäkäs"
        Koira.tehty += 1

    def hauku(self, kerrat): #osana class se on construktori ilman se on functioni
        for i in range(kerrat):
            print(f"{self.nimi} tervehtii {self.haukahdus}")
            

koira = Koira("Lissu", "Bokseri", "2022", "Hau hau")
koira2 = Koira("Wuffe", "Mastiffi", "2021", "woof woof")
koira3 = Koira("Fifi", "Puudeli", "2025") #"wruf wruf" )

print(f"1. koiran nimi on {koira.nimi}, rotu {koira.rotu} ja on syntynyt vuonna {koira.syntymävuosi}")
print(f"2. koiran nimi on {koira2.nimi},rotu {koira2.rotu} ja on syntynyt vuonna {koira2.syntymävuosi}")
print(f"3. koiran nimi on {koira3.nimi},rotu {koira3.rotu} ja on syntynyt vuonna {koira3.syntymävuosi}")

koira.hauku(4)
koira2.hauku(2)
koira3.hauku(3)

Koira.tehty

"""

inventaario = {"hakku", "kokis"}
inventaario2 = {"hakku", "kokis"}

class player