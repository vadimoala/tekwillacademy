import os

# 1. Citiți de la tastatură numele, prenumele şi notele la 3 examene pentru 3 elevi
# şi salvaţi datele în fişierul catalog.txt. Folosiţi instrucţiunea for.

# Inițializăm o listă goală pentru a stoca datele elevilor
elevi = []

# Iterăm prin fiecare elev
for i in range(3):
    nume = input(f"Introduceți numele elevului {i + 1}: ")
    prenume = input(f"Introduceți prenumele elevului {i + 1}: ")
    nota1 = float(input(f"Introduceți nota la primul examen pentru elevul {i + 1}: "))
    nota2 = float(input(f"Introduceți nota la al doilea examen pentru elevul {i + 1}: "))
    nota3 = float(input(f"Introduceți nota la al treilea examen pentru elevul {i + 1}: "))

    # Calculăm media notelor
    medie = (nota1 + nota2 + nota3) / 3

    # Adăugăm datele elevului în listă
    elevi.append((nume, prenume, medie))

# Salvăm datele în fișierul "catalog.txt"
with open("catalog.txt", "w") as file:
    for elev in elevi:
        file.write(f"{elev[0]} {elev[1]}: {elev[2]:.2f}\n")

print("Datele au fost salvate în fișierul catalog.txt.")

# 2. Cu ajutorul unui program Python, adăugaţi în fişierul catalog.txt datele pentru
# încă 3 elevi.

# Inițializăm o listă goală pentru a stoca datele elevilor
elevi = []

# Iterăm prin fiecare elev nou
for i in range(3, 6):  # Adăugăm 3 elevi noi (de la 4 la 6)
    nume = input(f"Introduceți numele elevului {i + 1}: ")
    prenume = input(f"Introduceți prenumele elevului {i + 1}: ")
    nota1 = float(input(f"Introduceți nota la primul examen pentru elevul {i + 1}: "))
    nota2 = float(input(f"Introduceți nota la al doilea examen pentru elevul {i + 1}: "))
    nota3 = float(input(f"Introduceți nota la al treilea examen pentru elevul {i + 1}: "))

    # Calculăm media notelor
    medie = (nota1 + nota2 + nota3) / 3

    # Adăugăm datele elevului în listă
    elevi.append((nume, prenume, medie))

# Salvăm datele în fișierul "catalog.txt"
with open("catalog.txt", "a") as file:  # Folosim "a" pentru a adăuga la fișier
    for elev in elevi:
        file.write(f"{elev[0]} {elev[1]}: {elev[2]:.2f}\n")

print("Datele au fost adăugate în fișierul catalog.txt.")

# 3. Deschideţi fişierul catalog.txt în modul citire, citiţi datele şi după aceasta
# calculaţi nota medie a fiecărui elev. Rescrieţi din nou datele în fişierul
# catalog.txt, împreună cu media calculată pentru fiecare elev.


# 4. Modificaţi datele din fişierul catalog.txt, în aşa mod încât numele de familie al
# fiecărui elev să fie scris cu toate literele majuscule.

# Citim datele din fișier
with open("catalog.txt", "r") as file:
    lines = file.readlines()

# Modificăm numele de familie
for i, line in enumerate(lines):
    parts = line.split()
    nume = parts[0]
    prenume = parts[1]
    nume_familie = nume.upper()  # Convertim numele de familie la majuscule
    medie = parts[-1]  # Păstrăm media notelor
    lines[i] = f"{nume_familie} {prenume}: nota medie = {medie}\n"

# Scriem datele modificate înapoi în fișier
with open("catalog.txt", "w") as file:
    file.writelines(lines)

print("Datele au fost actualizate cu numele de familie în majuscule în fișierul catalog.txt.")

# 5. Pentru fiecare elev din fişierul catalog.txt, creaţi câte un folder separat cu
# numele "Date_<nume elev>". Fiecare folder va conţine câte un fişier separat
# cu numele "Agenda_<nume elev>.txt", în care vor fi doar datele fiecărui elev.
# De exemplu, folderul pentru elevul "Vasile Rotaru" se va numi
# "Date_Vasile_Rotaru" iar fişierul se va numi "Agenda_Vasile_Rotaru.txt".
# Hint: pentru a crea folderele, folosiţi modulul OS


# Citim datele din fișier
with open("catalog.txt", "r") as file:
    lines = file.readlines()

# Creăm folderele și fișierele pentru fiecare elev
for line in lines:
    parts = line.split()
    nume = parts[0]
    prenume = parts[1]
    elev_folder = f"Date_{nume}"
    agenda_file = f"Agenda_{nume}.txt"

    # Creăm folderul pentru elev
    os.makedirs(elev_folder, exist_ok=True)

    # Scriem datele în fișierul Agenda
    with open(os.path.join(elev_folder, agenda_file), "w") as agenda:
        agenda.write(line)

print("Folderele și fișierele au fost create conform cerințelor.")

# 6. Folosind modulul OS, afişaţi toate fişierele din directoriul curent.

files = os.listdir('.')
for file in files:
    print(file)
