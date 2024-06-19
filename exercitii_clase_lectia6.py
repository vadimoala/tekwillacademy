
if __name__=="__main__":
    print("Bun venit la tema pentru acasa 06.01 - object oriented programming")

    # ==================== clase ====================
    # ------------------ Exercițiul 1 ------------------
    print("Creați o clasă 'Bicicleta' cu atributele 'marca' și 'viteza_maxima' și inițializați-le prin constructor.")

    class Bicicleta:
        def __init__(self, marca, viteza_maxima):
            self.marca = marca
            self.viteza_maxima = viteza_maxima

    # ------------------ Exercițiul 2 ------------------
    print("Adăugați o metodă 'descrie' în clasa 'Bicicleta' care afișează marca și viteza maximă.")

    class Bicicleta:
        def __init__(self, marca, viteza_maxima):
            self.marca = marca
            self.viteza_maxima = viteza_maxima

        def descrie(self):
            print(f"Marca: {self.marca}, Viteza: {self.viteza_maxima}, km/h")


    # ------------------ Exercițiul 3 ------------------
    print(
        "Creați o clasă 'Student' cu atributele 'nume' și 'an_studiu' și un atribut de clasă 'numar_studenti' care numără instanțele create.")

    class Student:
        numar_studenti = 0
        def __init__(self, nume, an_studiu):
            self.nume = nume
            self.an_studiu = an_studiu
            Student.numar_studenti += 1


    # ------------------ Exercițiul 4 ------------------
    print("Adăugați o metodă 'salut' în clasa 'Student' care afișează un mesaj de salut cu numele studentului.")


    class Student:
        def __init__(self, nume, an_studiu):
            self.nume = nume
            self.an_studiu = an_studiu

        def salut(self):
            print(f"Salut! Numele meu este {self.nume}.")



    # ------------------ Exercițiul 5 ------------------
    print("Creați o clasă 'CarteBiblioteca' cu atributele 'titlu', 'autor' și 'an_aparitie'.")

    class CarteBiblioteca:
        def __init__(self, titlu, autor, an_aparitie):
            self.titlu = titlu
            self.autor = autor
            self.an_aparitie = an_aparitie




    # ------------------ Exercițiul 6 ------------------
    print(
        "Adăugați o metodă 'este_veche' în clasa 'CarteBiblioteca' care verifică dacă cartea este mai veche de 50 de ani.")

    class CarteBiblioteca:
        def __init__(self, titlu, autor, an_aparitie):
            self.titlu = titlu
            self.autor = autor
            self.an_aparitie = an_aparitie

        def este_veche(self):
            return 2024 - self.an_aparitie > 50


    # ------------------ Exercițiul 7 ------------------
    print(
        "Creați o clasă 'Frigider' cu atributele 'marca' și 'temperatura' și o metodă 'seteaza_temperatura' care ajustează temperatura.")

    class Frigider:
        def __init__(self, marca, temperatura):
            self.marca = marca
            self.temperatura = temperatura

        def seteaza_temperatura(self, new_temperatura):
            self.temperatura = new_temperatura


    # ------------------ Exercițiul 8 ------------------
    print(
        "Adăugați o metodă 'verifica_temperatura' în clasa 'Frigider' care afișează dacă temperatura este în intervalul optim.")

    class Frigider:
        def __init__(self, marca, temperatura):
            self.marca = marca
            self.temperatura = temperatura

        def verifica_temperatura(self):
            if 2 <= self.temperatura <5:
                print("Temperatura este in intervalul optim")
            else:
                print("Temperatura nu este optima")


    # ------------------ Exercițiul 9 ------------------
    print(
        "Creați o clasă 'Telefon' cu atributele 'model' și 'memorie' și o metodă 'upgrade_memorie' care mărește memoria telefonului.")

    class Telefon:
        def __init__(self, model, memorie):
            self.model = model
            self.memorie = memorie

        def upgrade_memorie(self, extra_memorie):
            self.memorie =+ extra_memorie


    # ------------------ Exercițiul 10 ------------------
    print("Adăugați o metodă 'info' în clasa 'Telefon' care afișează modelul și memoria actuală a telefonului.")

    class Telefon:
        def __init__(self, model, memorie):
            self.model = model
            self.memorie = memorie

        def info(self):
            print(f"Model: {self.model}, Memorie: {self.memorie}GB")


    # ------------------ Exercițiul 11 ------------------
    print(
        "Creați o clasă 'Ceas' cu atributele 'marca' și 'an_fabricatie' și o metodă 'varsta' care calculează vârsta ceasului.")

    class Ceas:
        def __init__(self, marca, an_fabricatie):
            self.marca = marca
            self.an_fabricatie = an_fabricatie

        def varsta(self):
            return 2024 - self.an_fabricatie


    # ------------------ Exercițiul 12 ------------------
    print("Adăugați o metodă 'este_antichitate' în clasa 'Ceas' care verifică dacă ceasul are peste 100 de ani.")

    class Ceas:
        def __init__(self, marca, an_fabricatie):
            self.marca = marca
            self.an_fabricatie = an_fabricatie

        def este_antichitate(self):
            return self.varsta() > 100

    # ------------------ Exercițiul 13 ------------------
    print(
        "Creați o clasă 'Lampa' cu atributele 'culoare' și 'intensitate_lumina' și o metodă 'schimba_intensitatea' care ajustează intensitatea luminii.")

    class Lampa:
        def __init__(self, culoare, intensitatea_lumina):
            self.culoare = culoare
            self.intensitate_lumina = intensitatea_lumina

        def schimba_intensitatea(self, new_intensitate):
            self.intensitate_lumina = new_intensitate


    # ------------------ Exercițiul 14 ------------------
    print(
        "Adăugați o metodă 'este_aprinsa' în clasa 'Lampa' care returnează True dacă intensitatea luminii este mai mare decât 0.")

    class Lampa:
        def __init__(self, culoare, intensitatea_lumina):
            self.culoare = culoare
            self.intensitate_lumina = intensitatea_lumina

        def este_aprinsa(self):
            return self.intensitate_lumina > 0


    # ------------------ Exercițiul 15 ------------------
    print(
        "Creați o clasă 'Agenda' cu un atribut de instanță 'contacte' ca un dicționar și metode pentru 'adauga_contact', 'sterge_contact' și 'afiseaza_contacte'.")

    class Agenda:
        def __init__(self):
            self.contacte = {}

        def adauga_contact(self, nume, numar):
            self.contacte[nume] = numar

        def sterge_contact(self, nume):
            if nume in self.contacte:
                del self.contacte[nume]
            else:
                print("Contactul nu există.")

        def afiseaza_contacte(self):
            for nume, numar in self.contacte.items():
                print(f"Nume: {nume}, Număr: {numar}")



    # ------------------ Exercițiul 16 ------------------
    print(
        "Creați o clasă 'Playlist' cu un atribut 'melodii' ca o listă și metode pentru 'adauga_melodie', 'sterge_melodie' și 'afiseaza_playlist'.")

    class Playlis:
        def __init__(self):
            self.melodii = []

        def adauga_melodie(self, melodie):
            self.melodii.append(melodie)

        def sterge_melodie(self, melodie):
            if melodie in self.melodii:
                self.melodii.remove(melodie)
            else:
                print("Melodia nu exista in Playlist")

        def afiseaza_playlist(self):
            for melodie in self.melodii:
                print(melodie)

    # ------------------ Exercițiul 17 ------------------
    print(
        "Creați o clasă 'Proiector' cu atributele 'marca' și 'luminozitate' și o metodă 'afiseaza_info' care afișează marca și luminozitatea.")

    class Proiector:
        def __init__(self, marca, luminiozitate):
            self.marca  = marca
            self.luminiozitate = luminiozitate

        def afiseaza_info(self):
            print(f"Marca: {self.marca}, Luminiozitate: {self.luminiozitate}, lumeni")



    # ------------------ Exercițiul 18 ------------------
    print(
        "Adăugați o metodă 'este_suficient_de_luminos' în clasa 'Proiector' care verifică dacă luminozitatea este peste un anumit prag.")

    class Proiector:
        def __init__(self, marca, luminiozitate):
            self.marca  = marca
            self.luminiozitate = luminiozitate

        def este_suficient_de_luminos(self, prag):
            return self.luminiozitate > prag



    # ------------------ Exercițiul 19 ------------------
    print(
        "Creați o clasă 'Mouse' cu atributele 'marca' și 'tip' (ex: 'wireless', 'wired') și o metodă 'conecteaza_la_pc' care afișează un mesaj de conectare.")

    class Mouse:
        def __init__(self, marca, tip):
            self.marca = marca
            self.tip = tip

        def conecteaza_la_pc(self):
            print(f"Mouse-ul {self.marca} de tip {self.tip} a fost conectat la PC.")


    mouse_logitech = Mouse(marca="Logitech", tip="wireless")
    mouse_logitech.conecteaza_la_pc()




    # ------------------ Exercițiul 20 ------------------
    print("Adăugați o metodă 'este_wireless' în clasa 'Mouse' care returnează True dacă mouse-ul este wireless.")


    class Mouse:
        def __init__(self, marca, tip):
            self.marca = marca
            self.tip = tip

        def este_wireless(self):
            return self.tip == 'wireless'


    # ------------------ Exercițiul 21 ------------------
    print("""
    Crează un joc simplu de tipul 'Evadare din Labirint' folosind programarea orientată pe obiect. Jucătorul începe 
    dintr-un colț al labirintului și trebuie să găsească ieșirea. Labirintul este reprezentat ca o matrice de 5x5, 
    unde 'X' reprezintă un zid, ' ' (spațiu) reprezintă un coridor liber prin care se poate trece, 'S' este punctul de 
    start, iar 'E' este ieșirea.

    Labirintul:
    S ' ' ' 'X'X'
    'X' 'X' ' ' 'X'
    ' ' ' ' ' ' ' '
    'X' ' ' 'X' ' '
    'X' 'X' 'X' 'E'

    Jucătorul poate să se miște în sus (U), jos (D), stânga (L) și dreapta (R). Creează o clasă 'Labirint' care să 
    stocheze harta și poziția jucătorului. Adaugă metode pentru mișcarea jucătorului și verifică la fiecare pas dacă 
    jucătorul a ajuns la ieșire. Jocul se termină când jucătorul găsește ieșirea. Afișează mesaje corespunzătoare 
    atunci când jucătorul încearcă să se miște printr-un zid sau când găsește ieșirea.""")

    #
    # class Labirint:
    #     def __init__(self, harta):
    #         self.harta = harta
    #         self.poziție_jucător = (0, 0)  # Coordonatele inițiale ale jucătorului
    #
    #     def afișează_harta(self):
    #         for linie in self.harta:
    #             print(' '.join(linie))
    #
    #     def mută_jucător(self, direcție):
    #         x, y = self.poziție_jucător
    #         if direcție == 'U':
    #             x -= 1
    #         elif direcție == 'D':
    #             x += 1
    #         elif direcție == 'L':
    #             y -= 1
    #         elif direcție == 'R':
    #             y += 1
    #
    #         if 0 <= x < len(self.harta) and 0 <= y < len(self.harta[0]) and self.harta[x][y] != 'X':
    #             self.poziție_jucător = (x, y)
    #             if self.harta[x][y] == 'E':
    #                 print("Felicitări! Ai găsit ieșirea!")
    #                 return True
    #             return False
    #         else:
    #             print("Nu poți merge în această direcție.")
    #             return False
    #
    #
    # # Exemplu de utilizare:
    # harta_labirint = [
    #     ['S', ' ', ' ', ' ', 'X', 'X'],
    #     ['X', 'X', ' ', ' ', 'X', 'X'],
    #     [' ', ' ', ' ', ' ', ' ', ' '],
    #     ['X', ' ', 'X', ' ', ' ', ' '],
    #     ['X', 'X', 'X', ' ', 'E', ' ']
    # ]
    #
    # labirint = Labirint(harta_labirint)
    # labirint.afișează_harta()
    #
    # while True:
    #     direcție = input("Introdu direcția (U/D/L/R): ").upper()
    #     if labirint.mută_jucător(direcție):
    #         break

    class Labirint:
        def __init__(self):
            # Definim harta labirintului
            self.harta = [
                ['S', ' ', 'X', ' ', ' '],
                ['X', 'X', ' ', 'X', ' '],
                [' ', ' ', ' ', 'X', ' '],
                [' ', 'X', 'X', 'X', ' '],
                [' ', ' ', ' ', 'E', ' ']
            ]
            self.poziție_jucător = (0, 0)  # Coordonatele inițiale ale jucătorului

        def afișează_harta(self):
            for rând in self.harta:
                print(' '.join(rând))

        def mutare(self, direcție):
            x, y = self.poziție_jucător
            if direcție == 'U':
                x -= 1
            elif direcție == 'D':
                x += 1
            elif direcție == 'L':
                y -= 1
            elif direcție == 'R':
                y += 1

            # Verificăm dacă noua poziție este validă
            if 0 <= x < 5 and 0 <= y < 5 and self.harta[x][y] != 'X':
                self.poziție_jucător = (x, y)
                if self.harta[x][y] == 'E':
                    print("Felicitări! Ai găsit ieșirea!")
                    return True
                else:
                    print("Te-ai mutat la ({}, {}).".format(x, y))
            else:
                print("Nu poți să te muți acolo!")

            return False


    # Exemplu de utilizare
    labirint = Labirint()
    labirint.afișează_harta()

    while True:
        direcție = input("Introdu direcția (U/D/L/R): ").upper()
        if labirint.mutare(direcție):
            break







