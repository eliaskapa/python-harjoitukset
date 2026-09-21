import random
"""vuodenajat = "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi"

kuukausi = int(input("anna kuukausi ")) - 1

print(vuodenajat[kuukausi])
"""
nimilista = []

while True: 
    nimi = input("anna nimi: ")
    if nimi == "":
        print("ohi")
        break
    elif nimi in nimilista:
        print("vanha nimi")
    elif nimi not in nimilista:
        print("uusi nimi")

    nimilista.append(nimi)

random.shuffle(nimilista)  
print(nimilista)