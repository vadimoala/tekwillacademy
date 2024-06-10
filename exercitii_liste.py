#
# # 1. Creaţi lista lst1 = [1, 2, 3, 4].
# # Adăugaţi după aceasta elementele 5, 6, 7 la finalul acestei liste. Afişaţi rezultatul
lista1 = [1, 2, 3, 4]
lista1.extend([5, 6, 7])
print(lista1)
#
# # 2. Creaţi lista lst2 = [1, 2, 3, 4]. Sortaţi descrescător această listă.
lista2 = [1, 2, 3, 4]
lista2.sort(reverse=True)
print(lista2)
#
# # 3. Creaţi lista lst3 = [1, 2, "asd", 4]. Aflaţi index-ul elementului 4.
lista3 = [1, 2, 'asd', 4]
index = lista3.index(4)
print(f"Indexul elementului 4 este: {index}")
#
# # 4. Creaţi lista date_personale. Citiţi după aceasta de la tastatură numele,
# # prenumele, vârsta, înălţimea şi ocupaţia utilizatorului şi adăugaţi aceste valori în lista creată.
date_personale = []
nume = input("Introduceți numele: ")
prenume = input("Introduceți prenumele: ")
varsta = input("Introduceți vârsta: ")
inaltime = input("Introduceți înălțimea: ")
ocupatie = input("Introduceți ocupația: ")
date_personale.append(nume)
date_personale.append(prenume)
date_personale.append(varsta)
date_personale.append(inaltime)
date_personale.append(ocupatie)
print(date_personale)

# 5 Creaţi 2 liste: elev1 şi elev2. Pentru fiecare elev, cititi de la tastatură numele,
# prenumele şi nota obţinută la examen şi salvaţi datele în listele elev1 şi elev2.
# După aceasta, afişaţi la ecran:
# ● care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi
# prenumele)
# ● care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi
# prenumele)
# ● pentru fiecare elev, transformaţi numele sa fie scris cu toate literele
# majuscule, iar prenumele să înceapă cu literă mare. De exemplu,
# pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
# ● afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în
# exemplul de mai jos (liniile ce separă datele nu trebuie neapărat să
# concidă):

elev1 = []
elev2 = []
nume = input("Introduceți numele primului elev: ")
prenume = input("Introduceți prenumele primului elev: ")
nota = int(input("Introduceți nota primului elev: "))
elev1 = [nume, prenume, nota]
nume = input("Introduceți numele celui de-al doilea elev: ")
prenume = input("Introduceți prenumele celui de-al doilea elev: ")
nota = int(input("Introduceți nota celui de-al doilea elev: "))
elev2 = [nume, prenume, nota]
if elev1[2] > elev2[2]:
    print(f"{elev1[0]} {elev1[1]} are o notă mai mare la examen.")
elif elev1[2] < elev2[2]:
    print(f"{elev2[0]} {elev2[1]} are o notă mai mare la examen.")
else:
    print("Ambii elevi au aceeași notă la examen.")
elev1[0] = elev1[0].upper()
elev1[1] = elev1[1].capitalize()
elev2[0] = elev2[0].upper()
elev2[1] = elev2[1].capitalize()
print(f"\n{'Nume':<10} {'Prenume':<10} {'Notă':<7}")
print(f"{elev1[0]:<10} {elev1[1]:<10} {elev1[2]:<7}")
print(f"{elev2[0]:<10} {elev2[1]:<10} {elev2[2]:<7}")

