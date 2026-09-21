
#tehtävä 1

kuukaudet = ("tammi", "helmi", "maalis", "huhti", "touko", "kesä", "heinä", "elo", "syys", "loka", "marras", "joulu")

kuukausi = int(input("anna kuukauden numero: "))

kk_nimi = kuukaudet[kuukausi - 1]

print(kk_nimi)

#tehtävä 2

nimilista = set()

while True:
    nimi = input("anna nimi ")
    if nimi == "":
        print("loppu")
        break
    if nimi in nimilista:
        print("vanha nimi")
    else :
        print("uusi nimi")
        nimilista.add(nimi)

for nimi in nimilista:
    print(nimi)


lentoasema = {}

while True:
    kysymys = input("haluatko syöttää uuden lentoaseman (u), hakea vanhan lentoaseman tiedot (v) vai lopettaa (l)? ")
    if kysymys == "u":
        Nimi = input("anna uuden lentoaseman nimi")
        koodi = input("anna uuden lentoaseman ICAO koodi (kolme kirjainta)")
        lentoasema[koodi] =  Nimi

    elif kysymys == "v":
        koodi = input("anna vanhan lentoaseman ICAO koodi (kolme kirjainta)")
        if koodi in lentoasema:
            print(lentoasema[koodi])    

    elif kysymys == "l":
        print("loppu")
        break

print(lentoasema)

if lentoasema not in 