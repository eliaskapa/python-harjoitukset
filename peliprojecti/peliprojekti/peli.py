nimi = input("kerro nimesi: ")
ikä = int(input("kerro ikäsi: "))
print()

def päävalikko():
    print(f"Tervetuloa {nimi}\n")
    print(" päävalikko:")
    print("  aloita: ")
    print(" komennot: ")
    print("  lopeta: ")
def sammutus():
    print("peli sammuu")

def listaa():
    esine = input("mitä esineitä on: ")
    inventory.append(esine)
def info():
    print(inventory)
inventory = []

while ikä > 11:
    päävalikko() 
    komento = input("anna komento: ")
    if komento == "aloita":
        print("peli aloitettu")
    elif komento == "komennot":
        print("aloita, komennot, lopeta, inventaario, ota esine")
    elif komento == "inventaario":
        info()
    elif komento == "ota esine":
        listaa()
    elif komento == "lopeta":
        sammutus()
        break
    else:
        komento = input("Anna uusi komento: ")
if ikä <= 12:
    print("alaikä ban")
