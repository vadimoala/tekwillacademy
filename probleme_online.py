import math
# 1.Scrieţi o funcţie care primeşte ca parametru lungimea laturii unui pătrat şi returnează aria sa.

def aria(x):
    return x ** 2
print(aria(4))

# 2. Scrieţi un subprogram care primeşte ca parametru lungimea laturii unui pătrat şi returnează
# atât lungimea diagonalei, cât şi perimetrul pătratului.

def diagonala_perimetrul(latura):
    diagonala = latura * math.sqrt(2)
    perimetru = latura * 4
    return diagonala, perimetru
print(diagonala_perimetrul(4))

# 3. Scrieţi o funcţie care primeşte ca parametri de intrare lungimile celor două catete ale unui triunghi dreptunghic
# şi returnează lungimea ipotenuzei.

def lungimea(a,b):
    c = (a**2 + b**2)**0.5
    return c

ipotenuza = lungimea(3, 4)
print(f"Lungimea ipotenuzei este: {ipotenuza}")

# 4. Scrieţi o funcţie care primeşte 3 parametri de tip real, cu semnificaţia de lungimi pentru 3 segmente.
# Funcţia va returna 1 dacă cele trei segmente pot forma un triunghi şi 0, în caz contrar.

def triunghi(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 1
    else:
        return 0
print(triunghi(2,1,1))

# 5. Scrieţi o funcţie care returnează prima cifră a unui număr natural.
# De exemplu, dacă parametrul efectiv este 127, funcţia va returna 1.

def cifra(numar):
    while numar >= 10:
        numar //= 10
    return numar
print(cifra(127))

# 6. Să se tipărească toate numerele prime aflate între doi întregi citiţi.
# Programul va folosi o funcţie care testează dacă un număr este prim sau nu.

def prim(numar):
    if numar < 2:
        return False
    for i in range(2, int(numar**0.5) + 1):
        if numar % i == 0:
            return False
    return True
print(prim(10))

# 7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite,
# numere care se divid cu suma cifrelor lor.
# Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.

def suma_cifrelor(numar):
    suma = 0
    while numar > 0:
        cifra = numar % 10
        suma += cifra
        numar //= 10
        return suma

# def main():
#     try:
#         start = int(input("Introduceti primul numar: "))
#         end = int(input("Introduceti al doilea numar: "))
#
#         for numar in range(start, end + 1):
#             if numar % suma_cifrelor(numar) == 0:
#                 print(numar)
#     except ValueError:
#         print("Va rugam sa introducei numare valide")
#
# if __name__ == "__main__":
#     main()


# 8. Design triunghiular. Triunghiul de mai jos este generat de un algoritm.
# Descoperiţi acest algoritm şi folosiţi-l pentru a scrie un program care citeşte numărul n de linii
# şi generează triunghiul cu n linii corespunzător.

# 9. Scrieți un subprogram care să realizeze reuniunea, intersecția sau diferența a două mulțimi,
# în funcție de un parametru impus la apel.

def operatii_multimi(A, B, operatie):
    if operatie == "reuniune":
        return A | B
    elif operatie == "intersectie":
        return A & B
    elif operatie == "diferenta":
        return A - B
    else:
        raise ValueError("Operație nevalidă. Folosiți 'reuniune', 'intersectie' sau 'diferenta'.")

A = {1, 2, 3}
B = {3, 4, 5}

# Reuniunea
print("Reuniunea:", operatii_multimi(A, B, "reuniune"))

# Intersecția
print("Intersecția:", operatii_multimi(A, B, "intersectie"))

# Diferența
print("Diferența:", operatii_multimi(A, B, "diferenta"))