

print("while true, break example")
i = 3
while True:
    print("i: ", i)
    if i <= 0:
        print("almost negative i: ", i)
        break

    i -= 1 # i = i - 1 # echivalent

print("valoarea lui i inainte de for: ", i)
for j in range(10):
    print("J", j)
    i -= 1
    # if i < 0:
    #     print("i este negativ")
    #     break
print("valoarea lui i inainte dupa for: ", i)

# 1. Afișează toate numerele de la 1 la 10 folosind o buclă for
print("1. Afișează toate numerele de la 1 la 10 folosind o buclă for")
for i in range(1,11):
    print(i)


# 2. Afișează elementele listei ['Python', 'C++', 'Java'] folosind o buclă for
print("2. Afișează elementele listei ['Python', 'C++', 'Java'] folosind o buclă for")
languages = ['Python', 'C++', 'Java']
for languages in languages:
    print(languages)

# 3. Calculează suma numerelor de la 1 la n (unde n este un număr dat)
print("3. Calculează suma numerelor de la 1 la n (unde n este un număr dat)")
n = 2 # Se poate schimba valoarea lui n
suma = 0
for i in range(1, n + 1):
    suma += i
    print(suma)

# 4. Afișează tablei de înmulțire pentru numărul 5
print("4. Afișează tablei de înmulțire pentru numărul 5")
# 1 * 5 = 5
# 2 * 5 = 10 ...
numar = 2
for i in range(1,11):
    print(f"{numar} * {i} = {numar * i}")


# 5. Afișează caracterele șirului 'Python' folosind o buclă for
print("Afișează caracterele șirului 'Python' folosind o buclă for")
for caracter in 'Python':
    print(caracter)

# 6. Afișează toate numerele pare de la 1 la n
print("6. Afișează toate numerele pare de la 1 la n")
n = 10  # Se poate schimba valoarea lui n
for i in range(2, n + 1, 2):
    print(i)

# 7. Calculează produsul numerelor de la 1 la n
print("7. Calculează produsul numerelor de la 1 la n")
n = 5
produs = 1
for i in range(1, n + 1):
    produs *= i
    print(produs)

# 8. Afișează numărul de vocale din șirul 'hello world'
print("8. Afișează numărul de vocale din șirul 'hello world'")
text = 'heelloo world'
vocale = ['a', 'e', 'i', 'o', 'u']
numar_vocale = 0
for caracter in text:
    if caracter in vocale:
        numar_vocale += 1
        print(numar_vocale)


# 9. Afișează elementele listei ['Python', 'C++', 'Java'] în ordine inversă
print("9. Afișează elementele listei ['Python', 'C++', 'Java'] în ordine inversă")
programming_languages = ['Python', 'C++', 'Java']
for language in programming_languages [::-1]:
#for language in reversed(programming_languages):
    print(language)

# 10. Afișează indicii și valorile din lista ['Python', 'C++', 'Java']
print("10. Afișează indicii și valorile din lista ['Python', 'C++', 'Java']")
programming_languages = ['Python', 'C++', 'Java']
# (0, 'Python'),
# (1, 'C++')
for index, language in enumerate(programming_languages):
    print(f"Index: {index}, Valoare: {programming_languages}")


# 11. Afișează toți divizorii numărului 36
print("11. Afișează toți divizorii numărului 36")
numar = 36
for i in range(1, numar + 1):
    if numar % i == 0:
        print(i)


# 12. Generează o listă cu pătratele numerelor de la 1 la 10
print("12. Generează o listă cu pătratele numerelor de la 1 la 10")
patrate = [i ** 2 for i in range (1,11)]
print(patrate)

# 13. Afișează elementele comune dintre listele [1, 2, 3, 4, 5] și [4, 5, 6, 7, 8]
print("13. Afișează elementele comune dintre listele [1, 2, 3, 4, 5] și [4, 5, 6, 7, 8]")
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
for element in lista1:
    if element in lista2:
        print(element)


#14. Calculează factorialul numărului 5
print("14. Calculează factorialul numărului 5")
n = 5
factorial  = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial)

# 15. Afișează prima literă din fiecare cuvânt al propoziției 'Hello World Python'
print("15. Afișează prima literă din fiecare cuvânt al propoziției 'Hello World Python'")
fraza  = 'Hello World Python'
cuvinte = fraza.split()
for cuvant in cuvinte:
    print(cuvant[0])

