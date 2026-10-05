nimi = input("kerro nimesi: ")
ikä = int(input("kerro ikäsi: "))
print()
inventory = []


def päävalikko():
    print(f"Tervetuloa {nimi}\n")
    print(" päävalikko:")
    print("  aloita: ")
    print(" komennot: ")
    print("  lopeta: ")

def aloita():
    print("peli alkaa")

def komennot():
    print("\nKomennot:")
    print("komennot")
    print("inventaario")
    print("ota esine")
    print("lopeta")

def sammutus():
    print("peli sammuu")

def etsi():
    esine = input("minkä esineen löysit?: ")
    inventory.append(esine)
    print(f"{esine} lisättiin inventaarioon")

def info():
    print("inventaario \n")
    if len(inventory) == 0:
        print("et ole löytänyt mitään")
    else:
        for esine in inventory:
            print(esine)

game_running = False

while True:
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
        break

while game_running == True:
    print("")
    print("lopeta, inventaario, etsi \n")
    komento = input("anna komento: ")

    if komento == "inventaario":
        info()
    elif komento == "etsi":
        etsi()
    elif komento == "lopeta":
        sammutus()
        game_running = False

if ikä <= 12:
    print("alaikä ban")


