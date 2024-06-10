import random

# 1. Citiţi de la tastatura datele despre un elev: numele, prenumele, nota1,
# nota2, nota3 (cele 3 note la 3 examene). Adăugaţi aceste date într-un tuplu.
# Scrieţi o funcţie care calculează media notelor, folosind indexarea tuplurilor.
# nume = input("Introduceti numele elevului: ")
# prenume = input("Indroduceti prenumele elevului: ")
# nota1 = float(input("Indroduceti nota1: "))
# nota2 = float(input("Indroduceti nota2: "))
# nota3 = float(input("Indroduceti nota2: "))
# elev = (nume, prenume, nota1, nota2, nota3)
# print(elev)

# 2. Scrieți un program Python pentru a crea un tuplu cu numere și afişaţi un element aleator la ecran.
numere = (3, 7, 4, 5, 1)
print(random.choice(numere))

# 3. Scrieţi o funcţie care primeşte ca parametru de intrare un tuplu de numere
# întregi (pozitive sau negative), şi returnează produsul numerelor din acest tuplu.

# 4. Scrieţi o funcţie care să găsească toate elementele dintr-un tuplu ce se repetă de 2
# sau mai multe ori şi să le returneze sub formă de listă.

# 5. Scrieţi o funcţie care va avea un parametru de tip tuplu, şi va returna un alt
# tuplu ce conţine elementele primului tuplu în ordine inversă. De exemplu,
# pentru tuplul (1, 2, 3, 4, 5), rezultatul returnat va fi (5, 4, 3, 2, 1)

# 6. Creaţi un tuplu ce conţine datele despre un elev: numele, prenumele, nota1, nota2, nota3 (cele 3 note la 3 examene).
# Afişaţi după aceea la ecran valorile din tuplu, folosind formatarea string-urilor.

# 7. Creaţi o listă de tupluri. Scrieţi după aceea o funcţie care scoate din listă toate
# tuplurile ce nu conţin nici un element (tuplurile de lungime zero) şi returnează lista rezultată.
# De exemplu, pentru lista [(), (), ('a'), ('a', 'b'), ('a', 'b', 'c'), ('d'), ()],
# rezultatul returnat va fi lista [('a'), ('a', 'b'), ('a', 'b', 'c'), 'd']

# 8. Scrieţi o funcţie care primeşte ca date de intrare un tuplu de cifre şi
# returnează numărul format din aceste cifre dar sub formă de int.
# De exeplu, pentru datele de intrare (1, 2, 3, 0) rezultatul va fi int-ul 1230.
# Pentru datele de intrare (3,5) rezultatul va fi 35 (de tip int).


# 9. Scrieţi un program care transformă o listă de tupluri într-o listă de liste.
# De exemplu, pentru datele de intrare [(1, 2), (2, 3), (3, 4)],
# rezultatul va fi lista de liste [[1, 2], [2, 3], [3, 4]].
lista_tupluri = [(1, 2), (2, 3), (3, 4)]
liste = [list(tuplu) for tuplu in lista_tupluri]
print(liste)
