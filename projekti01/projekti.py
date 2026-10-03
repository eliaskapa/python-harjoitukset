from pelaaja import Pelaaja
from huone import Huone
from esine import Esine

p_nimi = input("kerro nimesi: ")
#tehdään pelaajalle nimi muuttuja
ikä = int(input("kerro ikäsi: "))

kello = Esine("Kulta kello", 1)
grani = Esine("graniitti", 5)
#tehdään esineet

eteinen = Huone("Eteinen", grani)
makuuhuone = Huone("Makuuhuone", kello)
#Huone luokkalle annetaan parametreinä huoneille nimi ja niissä sisältävät esineet

pelaaja = Pelaaja(p_nimi, [], None)
#pelaajan nimi muuttuja lisätään Pelaaja luokkaan
#annetaan pelaajalle lista tavaraluetteloksi ja 
#pelaajalla ei ole toistaiseksi sijaintia joten None olkoon arvo

def päävalikko():
    print(f"Tervetuloa {Pelaaja}\n")
    print(" päävalikko:")
    print("  aloita: ")
    print(" komennot: ")
    print("  lopeta: ")

def aloita():
    print("peli alkaa\n")

def komennot():
    print("\nKomennot:")
    print("inventaario")
    print("liiku")
    print("nappaa esine")
    print("lopeta")

def sammutus():
    print("peli sammuu")

def info():
    print("inventaario \n")
    if len(Player.tavaraluettelo) == 0:
        print("et ole ottanut mitään")
    else:
        for esine in inventory:
            print(esine)

game_running = False

while ikä > 11:
    päävalikko()
    komento = input("anna komento: ")
    if komento == "lopeta":
        sammutus()
        break
    if komento == "komennot":
        komennot()
        break
    if komento == "aloita":
        aloita()
        game_running = True
        break

while game_running == True:
    print("")

    print("lopeta, inventaario, etsi \n")

    komento = input("anna komento: ")

    if komento == "inventaario":
        info()
    elif komento == "nappaa esine":
        nappaa_esine()
    elif komento == "lopeta":
        sammutus()
        game_running = False

if ikä <= 12:
    print("alaikä ban")


