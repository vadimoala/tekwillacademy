#listele
colors = ["red", "green", "blue"]
print(colors[0])
print(colors[2])
print(len(colors))

legume = ["cartofi", "rosii", "morcov"]
elevi = ["Vasile", "Ana", "Ion"]
lista = [5, 7, "Python", [3, "Vadim"], False, [[2.0]]]
print(legume, elevi)
print(len(lista))
print(legume[2])
print(lista[3])
print(elevi[:2])

numere = [1, 2, 3, 4, 5, 6, 7]
print(numere[::-1])

# diferenta dintre append si extend
elevi = ["Vasile", "Ana", "Ion"]
elevi.append(["Vadim", "Gheorghe"])
print(elevi)

elevi = ["Vasile", "Ana", "Ion"]
elevi.extend(["Vadim", "Gheorghe"])
print(elevi)

# inserarea in lista
elevi = ["Vasile", "Ana", "Ion"]
elevi.insert(2, "Andrei")
print(elevi)

# stergerea unui element din lista
elevi = ["Vasile", "Ana", "Ion"]
elevi.remove("Ana")
print(elevi)

# functia pop sterge elementul dupa index si face return
elevi = ["Vasile", "Ana", "Ion"]
nume = elevi.pop(0)
print(nume)

# functia index ne arata in ce pozitie se afla elementul
colors = ["red", "green", "blue"]
# colors = colors.index("blue")
# print(colors)
# sau direct fuctia
print(colors.index("green"))

# de cate ori se gaseste un element in lista
print(colors.count("red"))

# functioa revers a unei liste
print(colors[::-1])
# sau
colors.reverse()
print(colors)

# sortarea numerelor in lista in ordine crescatoare
numere = [5, -2, 10, 4, 100, 1]
numere.sort()
print(numere)

# sortarea numerelor in lista in ordine descrescatoare
numere.sort(reverse=True)
print(numere)

# functia clear sterge totul din lista
numere.clear()
print(numere)

numere = [1, 2, 3, 4, 5]
numere = range(13) # in range se contine o lista de la 1 la 12 dar apare ca range
print(numere)
# sau specificam ca este lista
numere = list(range(1, 13))
print(numere)

print(sum(numere))
print(min(numere))
print(max(numere))
print(len(numere))

# functia enumerate returneaza atat valorile cat si indexul listei
colors = ["red", "green", "blue"]
for index, culoare in enumerate(colors,1):
    print(index, culoare)

# functia for merge prin toata lista
elevi = ["Vasile", "Ana", "Ion"]
for elev in elevi:
    print("Noroc", elev)

for numar in range(4,7):
    print(numar)

# parcurgem fiecare caracter din text
text = "Eu invat Python"
for caracter in text:
    print(caracter)

numere = [45, 64, 73, 35]
print(list(range(len(numere))))
for index, value in enumerate(numere):
    print(numere[index] - numere[index -1])

# functia while executa codul atata timp cat este True
index = 0
while index <= 10:
    print("Suntem la ", index)
    index+=2
