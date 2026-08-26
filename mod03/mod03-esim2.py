#tuntiharjoitus 26.8
#https://github.com/ilkkamtk/python-tuntiesimerkit

#sähkälaskutunti

kulutus = float(input("syötä sähkönkulutus (kWh): "))

hinta = 0

if  kulutus <= 50:
    hinta = kulutus * 10

elif kulutus <= 200:
    hinta = 50 * 10
    hinta += (kulutus-50) * 8
else:
    hinta = 50 * 10 + 150 * 8 + (kulutus - 200) * 6

print(f"sähkön hinta: {hinta//100:.0f},{hinta%100:.0f} Euroa.")

