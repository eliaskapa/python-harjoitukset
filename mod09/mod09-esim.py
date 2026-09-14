"""
k1_rotu = "Mastiffi"
k1_nimi =  "Wuffe"
k1_syntymävuosi = "2020"

k2_rotu = "bokseri"
k2_lissu = "lissu"
k2_syntymävuosi = "2023"

k3_rotu = "labradori"
k3_nimi = "sisu"
k3_syntymävuosi = "2019"
"""
class Koira:
    pass

#luokkka on kuin suunnitelma ja olio sen perusteella rakennettu yksilö

koira = Koira()
koira2 = Koira()


koira.nimi = "Wuffe"
koira.rotu = "Mastiffi"

koira2.nimi = "Lissu"
koira2.rotu = "Bokseri"

print("ensimmäinsen koiran", koira.nimi)
print("ensimmäinsen koiran", koira.rotu)

print("toisen koiran", koira.nimi)
print("toisen koiran", koira.rotu)

#teimme juuri luokan Koira ilman ominaisuuksia
#tämän jälkeen määrittelemme ominaisuudet yksi kerrallaan = työlästä
#näin teemme oikeasti:
