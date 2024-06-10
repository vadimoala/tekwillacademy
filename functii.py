# 4.1 Funcţii (introducere) - Exerciţii
# Partea 1:
# 1. Creaţi o funcţie care adună 2 numere şi returnează rezultatul

def adunare(a,b):
    c=a+b
    return c
print(adunare(2,7))

# 2. Creaţi o funcţie care primeşte un parametru - un număr, şi afişează la ecran
# dacă acest număr este mai mare, mai mic sau egal cu 5.

def comparatie_5(x):
    if x<5:
        return "mai mic"
    elif x>5:
        return "mai mare"
    else:
        return  "egal"
print(comparatie_5(5))


# 3. Creaţi funcţia mediaNumere, care primeşte un parametru de tip listă, şi
# returnează media numerelor din lista respectivă.

def media(lista):
    return sum(lista)/len(lista)
print(media([2,4,5,6,1]))



# 4. Scrieți o funcție Python care găseşte maximul a trei numere

def maxim_3(x, y, z):
    return max([x,y,z])
print(maxim_3(3,4,5))

def maxim_3(x, y, z):
   li=[x, y, z]
   return sorted(li, reverse=True)[0]
print(maxim_3(5,-8,7))

# 5. Ce va afişa codul din imaginea de mai jos?

# 6. Scrieți o funcție Python care să înmulțească toate numerele dintr-o listă şi să
# returneze rezultatul

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
print(multiply_list([1,5,2,54,6]))

# 7. Creaţi funcţia myName, care primeşte parametrul nume(de tip String), şi
# afişează la ecran "Salut, <nume>", dar înainte de aceasta transformă numele
# să fie scris cu prima literă mare.

def myName(nume):
    nume = nume.capitalize()
    print("Salut, " + nume)
print(myName("vadim"))

# 8. Scrieți o funcție Python care primeşte ca date de intrare un șir de caractere și
# calculează numărul de litere majuscule și minuscule. Funcţia trebuie să
# returneze ambele rezultate

def calculeaza_litere(sir):
    litere_majuscule = sum(1 for c in sir if c.isupper())
    litere_minuscule = sum(1 for c in sir if c.islower())
    return litere_majuscule, litere_minuscule

majuscule, minuscule = calculeaza_litere("Salut, Sunt Microsoft Copilot!")
print("Numărul de litere majuscule este:", majuscule)
print("Numărul de litere minuscule este:", minuscule)
