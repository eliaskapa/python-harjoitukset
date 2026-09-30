
 #datan lukeminen
with open("mod13/intro-teksti.txt") as intro_file:
    print(intro_file.read())
   # datan tallentaminen
   #tässä tapauksessa tiedoston polku määrittellään suhteessa projectin juuri kansioon

with open("mod13/data.txt", "a") as data_tiedosto:
    data_tiedosto.write("hei hoi \n")
   # datan lukeminen rivi kerrallaan

with open("mod13/data.txt") as mun_data_tiedosto:
   mun_data =  mun_data_tiedosto.readline()
   print("tiedoston data on", mun_data)
   mun_data =  mun_data_tiedosto.readlines()
   print("tiedoston data on", mun_data)

pelaajan_tiedot = { "pelaaja": "Matti", "taso": 5, "Varusteet:" ["miekka", "Kilpi", "haaniska"]}








