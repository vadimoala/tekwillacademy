


# 1.Definiți o funcție care acceptă un număr și returnează dacă numărul este par sau impar.

def myFunc(numar):
    if numar % 2 == 0:
        return "este par"
    else:
        return "este impar"
print(myFunc(5))

#  2.Defi niţi o funcţie care calculează valoarea expresiei de mai jos,
#  având ca date de intrare x şi y: f(x, y) = x2 + 2y + 10

def f(x,y):
    return x** + 2*y + 10
print(f(2,2))

# 3.Definiți o funcție numită dist_to_zero, cu un singur argument (alegeți orice nume de argument
# doriți). Dacă tipul argumentului este int sau float, funcția trebuie să returneze valoarea absolută
# (modulul) numărului. În caz contrar, funcția ar trebui să returneze "Nu!". Verifi cați dacă apelarea
# funcției funcționează cu -5.6 în primul caz și "Python" în al doilea caz.

def dist_to_zero(numar):
    if isinstance(numar, (int,float)):
        return abs(numar)
    else:
        return "Nu"
print(dist_to_zero(-5.6))
print(dist_to_zero("Python"))

# 4.Definiți o funcție numită shut_down, care primește un argument s.
# Dacă funcția shut_down primește un s egal cu "yes", ar trebui să returneze "Shutting down" Alternativ,
# dacă s este egal cu "no", atunci funcția ar trebui să returneze "Shutdown aborted".
# În cele din urmă, dacă shut_down primește orice altceva decât aceste intrări, funcția ar trebui să returneze "Sorry".

def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"
print(shut_down("altceva"))

# 5.Definiți o funcție pentru a calcula costurile călătoriei dumneavoastră. Funcţia va fi numită
# hotel_cost cu un singur argument nr_nights ca date de intrare. Hotelul costă 140 de dolari pe
# noapte. Funcţia trebuie să returneze preţul total, având ca argument nr_nights - câte nopţi a stat un
# turist într-un hotel.

def hotel_cost(nr_nights):
    cost_nigt = 140
    return  cost_nigt * nr_nights
print(hotel_cost(4))

# 6.Modificaţi funcţia precedentă, cu ajutorul argumentelor implicite, astfel încât să puteţi modifi ca
# dinamic preţul hotelului (de exemplu, pentru alt hotel preţul va fi de 100 dolari pe noapte)

# 7.Defi niți o funcție numită plane_ride_cost care primește ca intrare un șir de caractere, city. Funcția
# ar trebui să returneze un preț diferit în funcție de oraşul-destinaţie al călătoriei. Mai jos sunt
# prezentate destinațiile valide și prețurile corespunzătoare pentru călătoria dus-întors:
# "Pittsburgh": 222 euro
# "Los Angeles": 475 euro
# "Ohio": 183 euro
# "Chisinau": 300 euro

def plane_ride_cost(city):
    city_prices = {
        "Pittsburgh": 222,
        "Los Angeles": 475,
        "Ohio": 183,
        "Chisinau": 300
    }
    if city in city_prices:
        return city, city_prices[city]
    else:
        return "Aceasta destinatie nu exista"
print(plane_ride_cost("Chisinau"))

# 8.Scrieţi o funcţie care transformă o valoare din mile (unitate de măsură a distanţei) în km,
# ştiind că 1 milă este egală cu 1.60934 km:

def mila(x):
    return x * 1.60934
print(mila(3))

# 9.Scrieți o funcție care să calculeze aria unui dreptunghi

def aria(lungime,latime):
    return lungime * latime
print(aria(4,4))

# 10.Scrieţi o funcţie care verifică dacă o variabilă este de tip int, float sau String.
# Dacă este de tip String, va afişa "Hello world"!.
# Dacă este de tip float sau int, va returna numărul iniţial împreună cu dublul acestui număr.

def tip(x):
    if isinstance(x, str):
        return "Hello world!"
    elif isinstance(x, (int,float)):
        return x * 2
print(tip("str"))

# 11.Scrieţi o funcţie care ia ca parametru de intrare o listă.
# După aceasta, funcţia inter-schimbă primul element al listei cu ultimul element al listei şi returnează rezultatul.

def schimb(lista):
    if len(lista) < 2:
        return lista
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista
lista_mea = ["vadim", "ana", "vasile", 5]
print(schimb(lista_mea))

# 12.Scrieţi o funcţie care calculează suma cifrelor unui număr şi returnează rezultatul.

def suma_cifrelor(numar):
    suma = 0
    while numar:
        suma += numar % 10
        numar //= 10
    return suma
print(suma_cifrelor(1234))

# 17. Scrieţi o funcţie care dată fiind o listă de numere întregi, returnează True
# dacă lista conține un 3 lângă un 3 pe oricare poziţii consecutive din listă, ca în exemplul de mai jos:
# has_33([1, 3, 3]) → True (deoarece pe pozitiile 2 si 3 sunt cate un 3)
# has_33([1, 3, 1, 3]) → False (deoarece nu există doi de 3 pe poziţii consecutive)
# has_33([3, 3, 3, 3, 3, 3]) → True (deoarece pe oricare din perechile de index-uri (0, 1), (1, 2), etc. se află valoarea 3)

def has_33(lista):
    for i in range(len(lista) - 1):
        if lista[i] == 3 and lista[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 3, 3, 3, 3, 3]))

