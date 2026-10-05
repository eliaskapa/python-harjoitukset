from pelaaja import Pelaaja
from huone import Huone
from esine import Esine

p_nimi = input("kerro nimesi: ")
ikä = int(input("kerro ikäsi: "))

kello = Esine("Kulta kello", 1, 2)
grani = Esine("graniitti", 15, 3)
kirja = Esine("Vanha kirja", 4, 1)
lompakko = Esine("Lompakko", 3, 4)
tv = Esine("Vanha TV", 50, 4)
#tehdään esineet joita talosta löytyy


komero = Huone("komero", kirja)
pesutupa = Huone("pesutupa",lompakko )
olohuone = Huone("Olohuone", tv )
eteinen = Huone("Eteinen", grani)
makuuhuone = Huone("Makuuhuone", kello)
#Huone luokkalle annetaan parametreinä huoneille nimi ja niissä sisältävät esineet

pelaaja = Pelaaja(p_nimi)
#pelaajan nimi muuttuja lisätään Pelaaja luokkaan
#pelaajalla on jo sijainti annettu parametrinä pelaaja luokassa

def päävalikko():
    print(f"Tervetuloa {pelaaja.nimi} \n")
    print(" päävalikko:")
    print("  aloita: ")
    print(" komennot: ")
    print("  lopeta: ")

def aloita():
    print("")
    print("peli alkaa")
    print("olet ulkona\n")

def komennot():
    print("\nKomennot:")
    print("reppu")
    print("liiku")
    print("nappaa esine")
    print("lopeta")

def sammutus():
    print("peli sammuu")

def info():
    print("repun sisältö: \n")
    if len(pelaaja.tavaraluettelo) == 0:
        print("et ole ottanut mitään")
        #katsotaan onko listassa mitään ja jos ei ole niin printataan se
    else:
        for esine in pelaaja.tavaraluettelo:
            print(esine.nimi)
        #luetellaan listan sisältö
        print(sum(esine.paino for esine in pelaaja.tavaraluettelo))
        print(sum(esine.ääni for esine in pelaaja.tavaraluettelo))



valikko = False
#katsotaan ettei valikko avaudu ennen iän tarkistamista

if ikä <= 12:
    print("alaikä ban")

else:
    valikko = True
    game_running = False
    while valikko == True:
        päävalikko()
        komento = input("anna komento: ")
        if komento == "lopeta":
            sammutus()
            break
        if komento == "komennot":
            komennot()
        if komento == "aloita":
            aloita()
            game_running = True
            valikko = False
            break
        #peli valikko sulkeutuu ja peli käynnistyy

while game_running == True:
    print("liiku, nappaa esine, reppu, pakene \n")
    komento2 = input("mitäpä pitäisi tehdä? \n")
    if komento2 == "liiku":

        if pelaaja.sijainti == "ulkona":
            pelaaja.liiku(eteinen)
            print((f"saavuit huoneeseen {pelaaja.sijainti.nimi} ja näät {pelaaja.sijainti.esine.nimi}n\n"))
            print("")

        elif pelaaja.sijainti == eteinen:
            pelaaja.liiku(makuuhuone)
            print((f"saavuit huoneeseen {pelaaja.sijainti.nimi} ja näät {pelaaja.sijainti.esine.nimi}n\n"))

        elif pelaaja.sijainti == makuuhuone:
            print("viimeinen huone ja talon vanhat asukkaat heräävät kohta, voit ainoastaan paeta tai napata mitä voit")

    elif komento2 == "nappaa esine":
        if pelaaja.sijainti != "ulkona" and pelaaja.sijainti.esine is not None:
        #katsotaan ettei pelaaja ole ulkona ja jotta alueella on oikeasti esine
            napattu_esine = pelaaja.sijainti.esine
            pelaaja.nappaa_esine(napattu_esine)
            pelaaja.sijainti.esine = None
            #poistetaan esine

    elif komento2 == "reppu":
        info()

    elif komento2 == "pakene":
        info()
        print("pakenit paikalta")
        break

    

