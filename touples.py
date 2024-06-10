

# ######################### TUPLURI #########################
# # ------------------ Exercițiul 1 ------------------
print("Exercițiu 1: Creează un tuplu 'numere' care să conțină primele cinci numere naturale și afișează-l.")
numere = (1, 2, 3, 4, 5)
print(numere)
li=[1,2,3,4,5]
numere=tuple(li)
print(numere)
print(numere.count(2 ))
print(numere.index(3))

# # ------------------ Exercițiul 2 ------------------
print("Exercițiu 2: Afișează al treilea element din tuplul 'numere'.")
print(numere[3])

# # ------------------ Exercițiul 3 ------------------
print("Exercițiu 3: Afișează ultimul element din tuplul 'numere'.")
print(numere[-1])

# # ------------------ Exercițiul 4 ------------------
print("Exercițiu 4: Afișează elementele din tuplul 'numere', începând cu al doilea și terminând cu al patrulea.")
print(numere[1:5])
# # ------------------ Exercițiul 5 ------------------
print("Exercițiu 5: Verifică dacă numărul 4 este prezent în tuplul 'numere'.")
print(4 in numere)

# # ------------------ Exercițiul 6 ------------------
print("Exercițiu 6: Afișează lungimea tuplului 'numere'.")
print(len(numere))


print("Exercițiu 7: Concatenează tuplul 'numere' cu un nou tuplu care conține numerele 6 și 7. Afișează tuplul rezultat.")
tuplu_nou = numere + (6,7)
print(tuplu_nou)

# # ------------------ Exercițiul 8 ------------------
print("Exercițiu 8: Transformă tuplul 'numere' într-o listă și adaugă numărul 8. Afișează lista rezultată.")
print(list(tuplu_nou))
numere = list(tuplu_nou)
numere.append(8)
print(numere)

print("Exercițiu 9: Folosește o buclă 'for' pentru a itera prin tuplul 'numere_extins' și afișează fiecare valoare.")
for numar in numere:
    print( numar)


print("Exercițiu 10: Creează un nou tuplu 'date_personale' care să conțină numele, prenumele și vârsta ta. Afișează tuplul.")
date_personale = ("Oala", "Vadim", 32)
print(date_personale)

# # ------------------ Exercițiul 11 ------------------
print("Exercițiu 11: Afișează indexul elementului -3 în tuplul 'numere'.")
print(numere[-3])

# #------------------ Exercițiul 12 ------------------
print("Exercițiu 12: Afișează câte ori apare numărul 5 în tuplul 'numere_extins'.")
print(numere.count(5))

# # ------------------ Exercițiul 13 ------------------
print("exemplu de list comprehension")
# list comprehension
li=[]
for i in range(4):
    for j in range(i):
        if i!=j:
            li.append(tuple([i,j]))
print(li)
# aceiasi metoda simplificata
li=[tuple([i,j]) for i in range(4) for j in range(i) if i!=j]
print(li)
print("Exercițiu 13: Folosind compreensiunea de listă, creează o listă cu pătratele elementelor din tuplul 'numere'.")
li=[x*x for x in numere]
print(li)

# # ------------------ Exercițiul 14 ------------------
print("Exercițiu 14: Creează un tuplu 'mixt' care să conțină numere, șiruri de caractere și un alt tuplu."
"Afișează elementele tuplului 'mixt'.")
mixt = ("Salut", 50, "Vadim", True, (numere))
print(mixt )
# # ------------------ Exercițiul 15 ------------------
print("Exercițiu 15: Folosind o buclă 'for' și funcția 'type()', iterează prin tuplul 'mixt' și afișează tipul fiecărui element.")
for element in mixt:
    print(element, type(element))
# sau folosim list comprehension
li=[(element, type(element)) for element in mixt]
print(li)

# # ------------------ Exercițiul 16 ------------------
print("Exercițiu 16: Afișează tuplul 'date_personale' în ordine inversă.")
print(date_personale[::-1])

