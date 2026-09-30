
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
   
import json

tallennus_data = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}
with open("save.json", "w") as tiedosto:
    json.dump(tallennus_data, tiedosto)
with open("save.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)
print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")
    







