from pelaaja import Pelaaja
from huone import Huone
from huone import Varasto
from esine import Esine
from talo import Talo
import random

p_nimi = input("kerro nimesi: ")
ikä = int(input("kerro ikäsi: "))

loot_pool = [
Esine("kulta kello", 150, 2, 400),
Esine("graniitti kimpale", 1500, 3, 1),
Esine("vanha kirja", 300, 1, 4),
Esine("lompakko", random.randint(100,500), random.randint(0,6), random.randint(1,1000)),
Esine("vanha TV", 30000, 4, 20),
Esine("älypuhelin", random.randint(200,300), random.randint(1,5), random.randint(10,330))
]

#tehdään esineet joita rakennuksesta löytyy
#paino grammoina, äänekkys ja lopussa hinta euroina

kulta_harkko = Esine("kultaharkko", 250, 3, 30000)
kengät = Esine("kengät", 250, 2, 20)
#erikseen tehdään tietystä paikasta löytyvät esineet

aula = Huone("aula")

#A siiven huoneet ("kuntoilu ja suihkutilat")
A_eteinen = Huone("Suuri eteinen")
sali = Huone("Suuri jumppasali")
suihkut = Huone("Suihkutila")

#B siiven huoneet ("toimisto tila")
B_eteinen = Huone("Keskikoinen eteinen")
olohuone = Huone("B siiven olohuone")
toimisto = Huone("B siiven toimisto")
Kabinetti = Huone("Kabinetti")

#C siiven huoneet ("asumis tila")
C_eteinen = Huone("Pieni eteinen")
olohuone = Huone("C siiven olohuone")
keittiö = Huone("keittiö")
makuuhuone = Huone("makuuhuone")



kassakaappi = Varasto("kassakaappi", kulta_harkko) #B kabinetti
komero = Varasto("komero", kengät) #C makkari
#varastot jotka sijaitsee tietyissä huoneissa

#A siipi
A_eteinen.esine = random.choice(loot_pool)
A_pukuhuone = random.choice(loot_pool)
A_sali = random.choice(loot_pool)

#B siipi
B_eteinen.esine = random.choice(loot_pool)
B_olohuone = random.choice(loot_pool)
B_toimisto = random.choice(loot_pool)
B_asunto = random.choice(loot_pool)
B_kabinetti = random.choice(loot_pool)
#C siipi

C_eteinen.esine = random.choice(loot_pool)
C_olohuone = random.choice(loot_pool)
C_keittiö = random.choice(loot_pool)
C_makuuhuone = random.choice(loot_pool)

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

def komennot():
    print("\nKomennot:")
    print("reppu")
    print("liiku")
    print("nappaa esine")
    print("lopeta")

def sammutus():
    print("peli sammuu")

def vanha_tulos():
    print(info)

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
        #lasketaan yhteen esineiden paino ja ääni arvot

        if game_over == True:
            tulos = sum(esine.arvo for esine in pelaaja.tavaraluettelo)
            #esineiden 
            return tulos

game_over = False

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
        #pelin valikko sulkeutuu ja peli käynnistyy

while game_running == True:
    if pelaaja.sijainti == "ulkona":
        print("tervetuloa pelaamaan Pvaras:ta")
        print("olet ulkona ja edessäsi on suuri tiilistä noin vuonna 1960 rakennettu talo joka näyttää haarautuvan useisiin eri siipiin")

        alku = input("haluatko mennä sisälle? y/n: ")
        if alku == "n":
            print("ehkä tämä on kaikille parhaaksi")
            break

        elif alku == "y":
            pelaaja.liiku(aula)
            print(f"olet rakennuksen {pelaaja.sijainti.nimi}ssa. Edessä näkyy kolme siipeä, iso (A), keski (B) ja pieni (C)\n")
            print("valitse siipi mihin haluat mennä, A, B vai C? \n")
            komento2 = input("anna komento: ")

            #A siipi
            if komento2== "A" and pelaaja.sijainti == aula:
                pelaaja.liiku(A_eteinen)
                print("saavuit A siipeen ja edessäsi on suuri aukea eteinen")
                print(f"huoneessa on {pelaaja.sijainti.esine.nimi}")
                print("joko liiku, nappaa esine, reppu, pakene \n")
                #print(pelaaja.sijainti.nimi)

            elif komento2 == "liiku" and pelaaja.sijainti == A_eteinen:
                pelaaja.liiku(A_pukuhuone)
                print("saavuit pukuhuoneeseen jossa on paljon vaatteita")
                print("seuraavassa huoneessa kuuluu paljon ääntä ja mekkalaa")
                print(f"huoneessa on {pelaaja.sijainti.esine.nimi}")

            elif komento2 == "liiku" and pelaaja.sijainti == A_pukuhuone:
                pelaaja.liiku(A_sali)
                
            #B siipi
            elif komento2 == "B":
                print("saavuit B siipeen ja edessäsi on normaali eteinen")
                pelaaja.sijainti = B_eteinen
                print(f"huoneessa on {pelaaja.sijainti.esine.nimi}")
                print(pelaaja.sijainti.nimi)
                print("joko liiku, nappaa esine, reppu, pakene tai kysy komentoja\n")

            elif komento2 == "liiku" and pelaaja.sijainti == B_eteinen:
                pelaaja.liiku(B_olohuone)
                print("saavuit olohuoneeseen jossa on mukava sohva ja televisio")
                print(f"huoneessa on {pelaaja.sijainti.esine.nimi}")
        
            elif komento2 == "liiku" and pelaaja.sijainti == B_olohuone:
                pelaaja.liiku(B_toimisto)
                print("saavuit toimistoon jossa on paljon papereita ja tietokoneita")
                print(f"huoneessa on {pelaaja.sijainti.esine.nimi}")

            elif komento2 == "liiku" and pelaaja.sijainti == B_toimisto:
                pelaaja.liiku(B_kabinetti)
                print("saavuit hienosti sisustettuun kabinettiin joka käy pienestä asunnosta")
                print(f"huoneessa on {pelaaja.sijainti.esine.nimi}")

            #C siipi
            elif komento2 == "C":
                print("saavuit C siipeen ja edessäsi on pieni eteinen")
                pelaaja.sijainti = C_eteinen
                print(f"huoneessa on {pelaaja.sijainti.esine.nimi}")
                print(pelaaja.sijainti.nimi)

            elif komento2 == "komennot":
                komennot()
            
            elif komento2 == "nappaa esine":
                if pelaaja.sijainti != "ulkona" and pelaaja.sijainti.esine is not None:
                    #katsotaan ettei pelaaja ole ulkona ja jottei huoneen esinettä ole jo otettu
                    napattu_esine = pelaaja.sijainti.esine
        
                    pelaaja.nappaa_esine(napattu_esine)
                    #pelaaja luokasta olevalla funktiolla napattiin esine ja tallennettiin se tavaraluetteloon
        
                    pelaaja.sijainti.esine = None
                    #poistetaan esine oton jälkeen
                else:
                    print("et löydä mitään mitä voisit ottaa tai se on jo otettu")
            else:
                            print("valintaa ei löydy")
        elif komento2 == "reppu":
            info()

    elif komento2 == "pakene":
            game_over = True
            info()
            print("pakenit paikalta")
            break
            #printataan kaikki tarvittavat tiedot ja jotta tulos toimisi niin game_over = True        

    elif komento2 == "reppu":
            info()

    elif komento2 == "pakene":
            game_over = True
            info()
            print("pakenit paikalta")
            break
            #printataan kaikki tarvittavat tiedot ja jotta tulos toimisi niin game_over = True