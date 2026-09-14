nimi = input("kerro nimesi: ")
ikä = int(input("kerro ikäsi: "))

while ikä > 12:
    print()
    print(f"Tervetuloa {nimi}")
    print()
    print("päävalikko:")
    print(" aloita: ")
    print(" komennot: ")
    print(" lopeta: ")
    komento = input("anna komento: ")
    if komento == "lopeta":
        print(" peli sammuu")
        break
    if komento == "komennot":
        print("aloita, komennot, lopeta ")
    if komento == "aloita":
        print("peli aloitettu")
if ikä <= 12:
    print("alaikä ban")