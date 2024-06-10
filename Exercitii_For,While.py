#
# # 1. Citiţi de la tastatură o listă de cuvinte. Afişaţi la ecran după aceea doar cuvintele care au mai mult de 5 litere.
lista_cuvinte = input("Introduceti lista de cuvinte: ").split()
cuvinte_lungi = [cuvant for cuvant in lista_cuvinte if len(cuvant) > 5]
print("Cuvintele care au mai mult de 5 litere sunt:")
for cuvant in cuvinte_lungi:
    print(cuvant)

# #2. Citiţi de la tastatură 3 numere şi salvaţi-le într-o listă.
# # Afişaţi după aceea dublul fiecărui număr (numărul înmulţit cu 2), folosind instrucţiunea for.
numere = []
for i in range(3):
    numar = int(input("Introduceți un număr: "))
    numere.append(numar)
for numar in numere:
    print("Dublul numărului", numar, "este", numar * 2)


# 3. Salvaţi denumirile, autorii şi preţurile a 3 cărţi într-o listă de liste, în formatul:
# [[nume_carte1, autor_carte1, pret_carte1], [nume_carte2, autor_carte2, pret_carte2] ... ] .
carti = [["Toxic", "August Black", 230],
         ["Emma", "Jane Austen", 180],
         ["Mafiotul", "Diana Munteanu", 200]]
for carte in carti:
    nume, autor, pret = carte
    pret_redus = pret * 0.9
    print(f"\nNumele cartii: {nume} \nAutor: {autor} \nPretul cu reducere: {pret_redus} lei")

# 4. Citiţi de la tastatură un String şi salvaţi valoarea în variabila str1. După aceea
# creaţi variabila str2, care să conţină toate literele din str1, dar transformate în
# literele majuscule. Realizaţi acest exerciţiu cu ajutorul unei bucle for, folosind
# funcţia upper() pe o singură literă, nu pe tot şirul.
str1 = input("Scrieti un string: ")
str2 = ""
for litera in str1:
    str2 += litera.upper()
    print(str2)

# 5. Citiţi de la tastatură numărul întreg N. După aceasta, citiţi N produse şi N
# preţuri, şi salvaţi-le în formatul [[nume_produs1, pret1], [nume_produs2,
# pret2], ..., [nume_produs_N, pret_N]].
# Dacă utilizatorul scrie un preţ negativ sau egal cu zero, afişaţi o eroare şi nu
# includeţi produsul în listă.
# Afişaţi la final:
# ● suma totală a cumpărăturilor
# ● suma cumpărăturilor, cu o reducere de 10%, cu 2 cifre după virgulă
# ● care din produsele cumpărate este cel mai scump