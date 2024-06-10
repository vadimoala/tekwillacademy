#
# 1. Scrieţi o funcţie care primeşte 3 parametri: nume, prenume, varsta, în
# această ordine, şi calculează care va fi preţul biletului de intrare la un muzeu
# pentru persoana respectivă, în modul următor:
# ● biletul standard costă 100 lei
# ● biletul pentru copii (până la 18 ani) costă 40 lei
# ● biletul pentru persoanele a căror prenume începe cu litera "A" costă 90
# lei, dacă au mai mult de 17 ani
# Funcţia va returna preţul biletului calculat pentru fiecare persoană de o
# anumită vârstă.
# Citiţi de la tastatură datele persoanei şi apelaţi funcţia definită. Presupunem
# că "cititorul de date" are un alt standard şi citeşte datele persoanei într-o altă ordine:
# mai întâi vârsta, apoi numele, apoi prenumele. Ce tip de argumente trebuie să
# folosiţi (positional, keyword sau default)?

def calculeaza_pret_bilet(nume,prenume, varsta):
    pret_standard = 100
    pret_copii = 40
    pret_prenume_A = 90

    if varsta <= 18:
        return pret_copii
    elif prenume[0].lower() == 'a':
        return pret_prenume_A
    else:
        return pret_standard


varsta = int(input("Introduceți vârsta: "))
nume = input("Introduceți numele: ")
prenume = input("Introduceți prenumele: ")


pret_bilet = calculeaza_pret_bilet(nume=nume, prenume=prenume, varsta=varsta)

print(f"Pretul biletului este: {pret_bilet} lei")


# 2. Creaţi o funcţie care primeşte parametrul myList şi returnează numărul minim
# şi numărul maxim din lista respectivă (nu uitaţi că în Python funcţiile pot
# returna mai mulţi parametri). Folosiţi bucla for.

def min_max(myList):
    min_val = myList[0]
    max_val = myList[0]

    for num in myList:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val
min_val, max_val = min_max([4, 2, 9, 7, 5, 1])

print("Minimul este", min_val)
print("Maximul este", max_val)


# 3. Scrieţi o funcţie care permite aplicarea unei reduceri specifice unui preţ. Ca
# parametri de intrare, veţi avea preţul şi procentajul reduceriii (de exemplu,
# preţ=100, reducere=10 înseamnă ca va fi aplicată o reducere de 10% pe
# preţul de 100 lei). Implicit, reducerea este de 50%.
# După aceasta, citiţi de la tastatură un preţ şi apelaţi funcţia definită pentru a
# calcula cât va deveni preţul iniţial după o reducere de 10, 14, 15.2 şi 20%.
# Folosiţi keyword arguments atunci când apelaţi funcţia.

def aplica_reducere(pret, reducere=50):
    pret_nou = pret - (pret * reducere / 100)
    return pret_nou

pret_initial = float(input("Introduceți prețul inițial: "))

for reducere in [10, 14, 15.2, 20]:
    pret_redus = aplica_reducere(pret=pret_initial, reducere=reducere)
    print(f"După o reducere de {reducere}%, prețul devine: {pret_redus}")


# 4. Scrieți o funcție Python care ia o listă și returnează o nouă listă cu elemente
# unice ale primei liste

def elemente_unice(lista):
    return list(set(lista))
print(elemente_unice([4,67,2,4,1,1,1,2]))

