# # 16. Generează o listă cu primele 10 numere din secvența Fibonacci
print("16. Generează o listă cu primele 10 numere din secvența Fibonacci")
n = 10
fibonacci = [0, 1]
for i in range(2, n):
    next = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next)
print(fibonacci)

# # 17. Afișează toate numerele prime de la 1 la 50
 #https://www.pbinfo.ro/articole/74/numere-prime
print("17. Afișează toate numerele prime de la 1 la 50")
for num in range(2, 51):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

# # 18. Transformă elementele listei ['python', 'java', 'c++'] în majuscule
print("18. Transformă elementele listei ['python', 'java', 'c++'] în majuscule")
lista = ['python', 'java', 'c++']
for i in range(len(lista)):
    lista[i] = lista[i].upper()
print(lista)

# # 19. Afișează o piramidă de numere până la 5
print("19. Afișează o piramidă de numere până la 5")
for i in range(1, 6):
    print(" " * (5 - i) + str(i) * i)

# # 20. Afișează un model (tabla) de șah 8x8 folosind "#" pentru căsuțele negre și " " pentru cele albe

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("#", end = " ")
        else:
            print(" ", end = " ")
    print()


# # 21. Afișează toate subșirurile (sublistele) listei [1, 2, 3]
print("21. Afișează toate subșirurile listei [1, 2, 3]")
lista = [1, 2, 3]
sublists = [[]]
for i in range(len(lista) + 1):
    for j in range(i + 1, len(lista) + 1):
        sub = lista[i:j]
        sublists.append(sub)
print(sublists)

#22. Găsește și afișează toate perechile de numere din intervalul 1-10 ale căror sumă este 10
print("22. Găsește și afișează toate perechile de numere din intervalul 1-10 ale căror sumă este 10")
suma_dorita = 10
for i in range(1, suma_dorita):
    for j in range(i, suma_dorita):
        if i + j == suma_dorita:
            print(f"({i}, {j})")

# 23. Afișează toate numerele de la 1 la 10 folosind o buclă while
print("23. Afișează toate numerele de la 1 la 10 folosind o buclă while")



# 24. Calculează suma numerelor începând cu 1 până când suma depășește 100
print("24. Calculează suma numerelor începând cu 1 până când suma depășește 100")

# 25. Afișează toate puterile lui 2 mai mici decât 1000
print("25. Afișează toate puterile lui 2 mai mici decât 1000")
# 2**1 -> 2
# 2**2 -> 4
# 2**3 -> 8
# ...


# # 26. Găsește cel mai mic număr n astfel încât factorialul lui n (n!) este mai mare decât 1000
# print("26. Găsește cel mai mic număr n astfel încât factorialul lui n (n!) este mai mare decât 1000")
factorial = 1
while factorial <= 1000:
    n += 1
    factorial *= n
print(f"Cel mai mic număr n pentru care n! > 1000 este {n}")

# # 27. Afișează șirul 'Python' inversat cu while
# print("27. Afișează șirul 'Python' inversat cu while")
#
#
# # 28. Afișează numărul de cifre ale numărului 12345
# print("28. Afișează numărul de cifre ale numărului 12345")
#
# # 30. Afișează seria Fibonacci până când elementele seriei depășesc 1000
# print("30. Afișează seria Fibonacci până când elementele seriei depășesc 1000")
#
#
# # 32. Determină dacă numărul 12321 este palindrom cu ajutorul while
# print("32. Determină dacă numărul 12321 este palindrom cu ajutorul while")
# # acasa
#
# # 33. Determină toate numerele prime din intervalul [2, 100] cu ajutorul while
# print("33. Determină toate numerele prime din intervalul [2, 100] cu ajutorul while")
#
#
# # 34. Calculeaza și afișează toate numerele perfecte mai mici decât 10000
# print("34. Calculeaza și afișează toate numerele perfecte mai mici decât 10000")