

print("Sumați toate elementele dintr-o listă dată.")
lista = [4, 5, 6]
print(sum(lista))

# 2. Verificați dacă elementul 'x' există în lista dată.
print("Verificați dacă elementul 'x' există în lista dată.")
lista = [1, 'x', 3]
print('x' in lista)

# 3. Verificați dacă un string este palindrom (se citește la fel și de la dreapta la stânga).
print("Verificați dacă un string este palindrom (se citește la fel și de la dreapta la stânga).")
text = "radar"
print(text == text [::-1])


# 4. Verificați dacă o listă este sortată crescător.
print("Verificați dacă o listă este sortată crescător.")
lista = [1, 2, 3, 4, 5]
print(lista == sorted(lista))

# 5. Verificați dacă o listă este subsecvență a altei liste.
# Exemplu: lista ['a', 'b', 'c'] este subsecventa a listei ['a', 'b', 'c', 'd', 'e'] dar nu este secventa a listei ['a', 'b', 'f', 'c', 'd', 'e']
print("Verificați dacă o listă este subsecvență a altei liste.")
lista1 = ['a', 'b', 'c']
lista2 = ['a', 'b', 'c', 'd', 'e']
lista3 = ['a', 'b', 'f', 'c', 'd', 'e']

# 6. Creați o sub-listă care să contina doar elementele interioare ignorand elementele de pe margini.
print("# 6. Creați o sub-listă care să contina doar elementele interioare ignorand elementele de pe margini.")
matrice_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


# 7. Verificați dacă un string introdus este 'da', 'nu' sau altceva.
print("7. Verificați dacă un string introdus este 'da', 'nu' sau altceva.")
str = input("Introduceti da/nu sau altceva: ")
if str == "da":
    print("Ati indrodus da")
elif str == "nu":
    print(" Ati indrodus nu")
else:
    print("Ati indrodus altceva")


# 8.Verificați dacă un număr este într-un interval dat. e.g. intre 1 si 10
print("8. Verificați dacă un număr este într-un interval dat. e.g. intre 1 si 10")



# 9. Dată fiind o variabilă `an`, verificați dacă este un an bisect.
print('9. Dată fiind o variabilă `an`, verificați dacă este un an bisect.')
an = 1900
