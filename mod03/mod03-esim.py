import math

#teksti = "tämä on laskukone, anna kaksi lukua"

#print(teksti)

#luku = input("anna 1. luku ")
#luku2 = input("anna 2. luku ")

#luku = float(luku)
#luku2 = float(luku2)

#summa = float(luku) + float(luku2)

#summa = str(summa)
#print("summa:"+ summa_str)

#print("lukujen " + str(luku) + " ja " + str(luku2) + " summa on " + summa + ".")

#ikä = 25 

#uusi_kayttaja = input('anna nimesi: ')

#print('Shalom hieno herra, '+ uusi_kayttaja + '!')

#print ('hauska tavata {uusi_käyttäjä}')
#print (f'Hauska tavata{uusi_kayttaja} ja ikäni on {ikä}!!!!!!')
'''
pisteet = 200
pisteet = 400 #muuttujia ylikirjoitetaan
print (pisteet)

merkkijono = "Toni"
#merkkijono = "9"
#merkkijono = ""
pisteet = 0

print(f"merkkijono: {merkkijono:20s} sijoitetaan tähän väliin")

kokonaisluku = -9
kokonaisluku_pitkä = 12_200_300_400
liukuluku = 4.911
kompleksiluku = -4 + 2j
totuusarvo = False

print (kompleksiluku)
print (kompleksiluku. real)
print (kompleksiluku. imag)

print ("muuttujan tyyppi voidaan tutkia {type(kompleksiluku)}")

print (f"{"vakio":8s}|{"arvo":<20s}")
print ("---------------")
print (f"{"pii":6s}:{math.pi:6.2f}")
'''

tuloste = '''
yhteenlasku (+), vähennyslasku (-)
kertolasku (*) ja jakolasku (/)
jakojäännösoperaatio (%)
pelkän kokonaisosan palauttava jakolasku (//)
potenssiinkorotus (**).
'''
print (tuloste)

#laskukone

#luetaan käyttäjältä kaksi lukua (str) jokta täytyy muistaa muuntaa
#liukuluvuksi elo float ja sijoittaa muuttujiin

a = float(input("anna ensimmäinen luku:\n"))
b = float(input("anna toinen luku:\n"))

yhteenlasku = a + b
vähennyslasku = a - b
kertolasku = a * b
potenssiinkorotus = a ** b
jakolasku = a / b
kokonaisosa = a // b
jakojäännös = a % b


print (f"yhteenlasku {yhteenlasku}")
print (f"vähennyslasku {vähennyslasku}")
print (f"kertolasku {kertolasku}")
print (f"potenssiinkorotus {potenssiinkorotus}")
print (f"jakolasku {jakolasku}")
print (f"kokonaisosa {kokonaisosa}")
print (f"jakojäännös{jakojäännös}")