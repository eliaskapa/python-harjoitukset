from pelaaja import Pelaaja
from huone import Huone
from esine import Esine
import random

p_nimi = input("kerro nimesi: ")
ikä = int(input("kerro ikäsi: "))

lootti_lista = [
Esine("kulta kello", 150, 2),
Esine("graniitti", 1500, 3),
Esine("vanha kirja", 300, 1),
Esine("lompakko", 400, 4),
Esine("vanha TV", 30000, 4),
Esine("lompakko" 250, 4)
]

#tehdään esineet joita talosta löytyy
#paino grammoina
kulta_harkko = Esine("kultaharkko", 2)
#erikseen tehdään tietystä paikasta löytyvät esineet

eteinen0 = Huone("eteinen")
eteinen1 = Huone("Eteinen")
eteinen2 = Huone("Eteinen")
komero = Huone("komero" )
pesutupa = Huone("pesutupa")
olohuone = Huone("b siiven olohuone")
makuuhuone = Huone("makuuhuone")
keittiö = Huone("keittiö")
olohuone2 = Huone("a siiven olohuono")

eteinen0.esine = random.choice(lootti_lista)
eteinen1.esine = random.choice(lootti_lista)
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
    if pelaaja.sijainti == "ulkona":
        talo = input(print(f"olet {pelaaja.sijainti.nimi} ja edessäsi on kolme taloa, iso, pieni ja keski, mihin niistä haluat tunkeutua? \n"))
        print("tervetuloa pelaamaan Pvaras:ta")

    print("liiku, nappaa esine, reppu, pakene \n")


    komento2 = input("mitä aiot tehdä? \n")
    if komento2 == "liiku":

        """if pelaaja.sijainti == "ulkona":
            pelaaja.liiku(eteinen0)
            print((f"saavuit huoneeseen {pelaaja.sijainti.nimi} ja huoneessa on {pelaaja.sijainti.esine.nimi}n\n"))
            print("")

        elif pelaaja.sijainti == eteinen0:
            pelaaja.liiku(makuuhuone)
            print((f"saavuit huoneeseen {pelaaja.sijainti.nimi} ja näät {pelaaja.sijainti.esine.nimi}n\n"))

        elif pelaaja.sijainti == makuuhuone:
            print("viimeinen huone ja talon vanhat asukkaat heräävät kohta, voit ainoastaan paeta tai napata mitä voit")"""

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

    

