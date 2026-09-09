# mod 7 - funktio tuntiesimerkkejä

print("print() on pythonin sisäänrakennettu funktio")

def do_nothing(): #suluilla merkataan funktio
    pass

do_nothing()
"""
def print_list_of_numbers(): #kutsu funktio ja pitää olla sulkeet jotta voi kutsua
    print(1)
    print(2)
    print(3)

print_list_of_numbers()
"""
# Funktion parametrit (argumentit) ovat muuttujia, joiden arvot on käytössä
# funktion sisällä, ja  joille syötetään arvot funktiota kutsuttaessa



def print_list_of_numbers(start, end): #kutsu funktio ja pitää olla sulkeet jotta voi kutsua
    print(f"tulostetaan kaikki {start}, {end}")
    for i in range(start+1, end+1, 1):
        print(i)
        return


print_list_of_numbers(1, 5)
#funktio ilman return-sanaa tai pelkk return sana ilman määritettyä paluuarvoa on: None
test_return_value = print_list_of_numbers(7, 11)
print("test return value", test_return_value)


print()
# funktio ja paluuarvo (return)
number = "01"
# int()-funktio palauttaa annetun parametrin arvon
print(int(number)) #/"01" => 1

#funktio joka ei tulosta numeroita suoraan vaan palauttaa ne listamuodossa
def create_list_of_numbers(start, end):
    print(f"tehdään lista jossa arvot {start}-{end}")
    number_list = []
    for i in range(start, end+1, 1):
        number_list.append(i)
    return number_list

print(create_list_of_numbers(3, 7))

list_of_numbers = create_list_of_numbers(11, 16)
#print(list_of_numbers)