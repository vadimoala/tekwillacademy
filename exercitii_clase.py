if __name__ == "__main__":
    print("Bun venit la tema 06.01 - object oriented programming")

    ###################### clase ######################
    # ------------------ Exercițiul 1 ------------------
    print("Definiți o clasă numită 'Masina' fără atribute sau metode.")

    class Masina:
        pass

    # ------------------ Exercițiul 2 ------------------
    print("Creați o instanță a clasei 'Masina' și atribuiți-o unei variabile 'masina_mea'.")

    masina_mea = Masina()

    # ------------------ Exercițiul 3 ------------------
    print(
        "Adăugați două atribute la clasa 'Masina': 'marca' și 'model' și creați o instanță cu aceste atribute inițializate.")

    class Masina:
        def __init__(self, marca, model):
            self.marca = marca
            self.model = model

    masina_mea = Masina('Ford', 'Mustang')


    # ------------------ Exercițiul 4 ------------------
    print("Adăugați o metodă numită 'afisare_informatii' la clasa 'Masina' care printează marca și modelul mașinii.")

    class Masina:
        def __init__(self, marca, model):
            self.marca = marca
            self.model = model

        def afisare_informatii(self):
            print(f"Marca: {self.marca}, Model: {self.model}")


    masina_mea = Masina('Ford', 'Mustang')
    masina_mea.afisare_informatii()


    # ------------------ Exercițiul 5 ------------------
    print(
        "Adăugați un atribut de clasă numit 'numar_masini' la 'Masina' care ține evidența numărului total de instanțe create.")

    class Masina:
        numar_masini = 0

        def __init__(self, marca, model):
            self.marca = marca
            self.model = model
            Masina.numar_masini += 1

    masina_mea = Masina('Ford', 'Mustang')
    print(Masina.numar_masini)


    # ------------------ Exercițiul 6 ------------------
    print("Creați o metodă de clasă 'get_numar_masini' care returnează numărul total de mașini create.")


    class Masina:
        """Variabila definită cu self: Este o variabilă a instanței. Asta înseamnă că fiecare obiect (sau instanță) al
        clasei va avea propria sa copie a acestei variabile. Modificările făcute asupra acestei variabile afectează
        doar instanța respectivă. În exemplul dat, marca și model sunt variabile ale instanței, deoarece sunt
        prefixate cu self, indicând faptul că fiecare instanță a clasei Masina va avea propriile sale valori
        pentru marca și model.

        Variabila definită fără self: Este o variabilă a clasei, cunoscută și sub numele de variabilă statică.
        Aceasta este partajată între toate instanțele clasei. Orice modificare adusă acestei variabile va fi vizibilă
        tuturor instanțelor clasei. În exemplul tău, numar_masini este o variabilă a clasei, deoarece este definită în
        afara oricărei metode a instanței și este accesată folosind numele clasei (Masina.numar_masini).
        Asta înseamnă că, indiferent de numărul de instanțe Masina create, există doar o singură copie a numar_masini,
        și aceasta este partajată între toate aceste instanțe.


        Deci, de fiecare dată când o nouă instanță a clasei Masina este creată (prin apelarea __init__), numar_masini
        este incrementat cu 1. Acest comportament urmărește să țină evidența numărului total de instanțe Masina
        create în cadrul programului. Datorită naturii sale statice, numar_masini va reflecta numărul total de
        mașini create indiferent de instanță, deoarece toate instanțele clasei Masina împărtășesc aceeași
        variabilă numar_masini."""

        numar_masini = 0

        def __init__(self, marca, model):
            self.marca = marca
            self.model = model
            Masina.numar_masini += 1

        @classmethod
        def get_numar_masini(cls):
            return cls.numar_masini


    print(Masina.get_numar_masini())
    obj1 = Masina("Ford", "Mustang")
    print(Masina.get_numar_masini())
    obj2 = Masina("Ford", "Mustang")
    obj3 = Masina("Ford", "Mustang")
    print(Masina.get_numar_masini())

    # ------------------ Exercițiul 7 ------------------
    print(
        "Adăugați un atribut 'an_fabricatie' la clasa 'Masina' și modificați metoda 'afisare_informatii' pentru a include și anul de fabricație.")


    class Masina:
        def __init__(self, marca, model, an_fabricatie):
            self.marca = marca
            self.model = model
            self.an_fabricatie = an_fabricatie

        def afisare_informatii(self):
            print(f"Marca: {self.marca}, Model: {self.model}, An fabricație: {self.an_fabricatie}")


    masina_mea = Masina('Ford', 'Mustang', 2020)
    masina_mea.afisare_informatii()

    # ------------------ Exercițiul 8 ------------------
    print(
        "Creați o metodă numită 'este_veche' care returnează True dacă mașina este mai veche de 10 ani, altfel False.")


    class Masina:
        def __init__(self, marca, model, an_fabricatie):
            self.marca = marca
            self.model = model
            self.an_fabricatie = an_fabricatie

        def este_veche(self):
            return 2024 - self.an_fabricatie > 10


    masina_mea = Masina('Ford', 'Mustnag', 2005)
    print(masina_mea.este_veche())

    # ------------------ Exercițiul 9 ------------------
    print(
        "Adăugați un atribut 'kilometraj' la clasa 'Masina' și o metodă 'actualizeaza_kilometraj' pentru a actualiza kilometrajul.")


    class Masina:
        def __init__(self, marca, model, an_fabricatie, kilometraj):
            self.marca = marca
            self.model = model
            self.an_fabricatie = an_fabricatie
            self.kilometraj = kilometraj

        def actualizeaza_kilometraj(self, km):
            self.kilometraj = km


    masina_mea = Masina('Ford', 'Mustang', 2020, 50000)
    masina_mea.actualizeaza_kilometraj(55000)
    print(masina_mea.kilometraj)

    # # ------------------ Exercițiul 10 ------------------
    print("Creați o metodă numită 'descrie_kilometraj' care printează kilometrajul actual al mașinii.")


    class Masina:
        def __init__(self, marca, model, an_fabricatie, kilometraj):
            self.marca = marca
            self.model = model
            self.an_fabricatie = an_fabricatie
            self.kilometraj = kilometraj

        def descrie_kilometraj(self):
            print(f"Kilometrajul actual al mașinii este: {self.kilometraj} km")


    masina_mea = Masina('Ford', 'Mustang', 2020, 55000)
    masina_mea.descrie_kilometraj()


    # ------------------ Exercițiul 11 ------------------
    print("Modificați metoda 'actualizeaza_kilometraj' astfel încât să nu permită scăderea kilometrajului.")


    class Masina:
        def __init__(self, marca, model, an_fabricatie, kilometraj):
            self.marca = marca
            self.model = model
            self.an_fabricatie = an_fabricatie
            self.kilometraj = kilometraj

        def actualizeaza_kilometraj(self, km):
            if km >= self.kilometraj:
                self.kilometraj = km
            else:
                print("Nu se poate reduce kilometrajul.")


    masina_mea = Masina('Ford', 'Mustang', 2020, 55000)
    masina_mea.actualizeaza_kilometraj(50000)  # Nu va schimba kilometrajul

    # ------------------ Exercițiul 12 ------------------
    print(
        "Creați o metodă numită 'incrementa_kilometraj' care adaugă un număr dat de kilometri la kilometrajul actual.")


    class Masina:
        def __init__(self, marca, model, an_fabricatie, kilometraj):
            self.marca = marca
            self.model = model
            self.an_fabricatie = an_fabricatie
            self.kilometraj = kilometraj

        def incrementa_kilometraj(self, km):
            if km > 0:
                self.kilometraj += km
            else:
                print("Numărul de kilometri adăugați trebuie să fie pozitiv.")


    masina_mea = Masina('Ford', 'Mustang', 2020, 55000)
    masina_mea.incrementa_kilometraj(500)
    print(masina_mea.kilometraj)

    # ------------------ Exercițiul 13 ------------------
    print(
        "Creați o clasă 'Pisica' cu atributele 'nume' și 'varsta'. Adăugați o metodă 'miauna' care printează 'Miau!'.")


    class Pisica:
        def __init__(self, nume, varsta):
            self.nume = nume
            self.varsta = varsta

        def miauna(self):
            print("Miau!")


    pisica_mea = Pisica('Tom', 3)
    pisica_mea.miauna()

    # ------------------ Exercițiul 14 ------------------
    print(
        "Pisica vecinului: Adăugați un atribut de instanță 'culoare' la clasa 'Pisica' și modificați constructorul pentru a-l include.")


    class Pisica:
        def __init__(self, nume, varsta, culoare):
            self.nume = nume
            self.varsta = varsta
            self.culoare = culoare

        def miauna(self):
            print("Miau!")


    pisica_mea = Pisica('Tom', 3, 'gri')
    print(f"Pisica vecinului meu este {pisica_mea.culoare}.")

    # ------------------ Exercițiul 15 ------------------
    print("Creați o metodă 'descrie' în clasa 'Pisica' care printează numele, vârsta și culoarea pisicii.")


    class Pisica:
        def __init__(self, nume, varsta, culoare):
            self.nume = nume
            self.varsta = varsta
            self.culoare = culoare

        def descrie(self):
            print(f"Nume: {self.nume}, Vârsta: {self.varsta} ani, Culoare: {self.culoare}")


    pisica_mea = Pisica('Tom', 3, 'gri')
    pisica_mea.descrie()


    # ------------------ Exercițiul 16 ------------------
    print(
        "Adăugați o metodă 'e_mai_mare' în clasa 'Pisica' care compară vârsta a două pisici și returnează True dacă instanța curentă este mai mare.")


    class Pisica:
        def __init__(self, nume, varsta, culoare):
            self.nume = nume
            self.varsta = varsta
            self.culoare = culoare

        def e_mai_mare(self, alta_pisica):
            return self.varsta > alta_pisica.varsta


    pisica1 = Pisica('Tom', 3, 'gri')
    pisica2 = Pisica('Felix', 5, 'negru')
    print(pisica1.e_mai_mare(pisica2))  # False

    # ------------------ Exercițiul 17 ------------------
    print(
        "Creați o clasă 'Carte' cu atributele 'titlu' și 'autor'. Adăugați o metodă 'descriere' care printează titlul și autorul cărții.")


    class Carte:
        def __init__(self, titlu, autor):
            self.titlu = titlu
            self.autor = autor

        def descriere(self):
            print(f"Titlu: {self.titlu}, Autor: {self.autor}")


    cartea_mea = Carte('Moby Dick', 'Herman Melville')
    cartea_mea.descriere()

    # ------------------ Exercițiul 18 ------------------
    print(
        "Adăugați un atribut 'an_publicatie' la clasa 'Carte' și modificați constructorul și metoda 'descriere' pentru a include acest atribut.")


    class Carte:
        def __init__(self, titlu, autor, an_publicatie):
            self.titlu = titlu
            self.autor = autor
            self.an_publicatie = an_publicatie

        def descriere(self):
            print(f"Titlu: {self.titlu}, Autor: {self.autor}, An publicație: {self.an_publicatie}")


    cartea_mea = Carte('Ion Creanga', 'Amintiri din Copilarie', 1881)
    cartea_mea.descriere()

    # ------------------ Exercițiul 19 ------------------
    print("Creați o clasă 'Calculator' cu o metodă statică 'aduna' care primește doi parametri și returnează suma lor.")


    class Calculator:
        # Un @staticmethod este o metodă care nu primește un argument implicit precum self sau cls. Practic, este doar
        # o funcție normală care se întâmplă să fie definită în interiorul unei clase. Nu poate accesa sau modifica
        # starea clasei; este limitată la funcționalitățile pe care le definește. Staticmethod-urile sunt utile când o
        # anumită funcționalitate este legată conceptual de o clasă, dar nu accesează în mod explicit starea clasei
        # sau a instanței.
        @staticmethod
        def aduna(a, b):
            return a + b


    print(Calculator.aduna(5, 3))

    # ------------------ Exercițiul 20 ------------------
    print(
        "Adăugați metode statice 'scade', 'inmulteste' și 'imparte' în clasa 'Calculator' pentru a efectua scăderea, înmulțirea și împărțirea.")


    class Calculator:
        @staticmethod
        def aduna(a, b):
            return a + b

        @staticmethod
        def scade(a, b):
            return a - b

        @staticmethod
        def inmulteste(a, b):
            return a * b

        @staticmethod
        def imparte(a, b):
            if b != 0:
                return a / b
            else:
                return "Nu se poate împărți la zero."


    print(Calculator.scade(10, 5))
    print(Calculator.inmulteste(4, 6))
    print(Calculator.imparte(8, 2))
    print(Calculator.imparte(5, 0))

    # ------------------ Exercițiul 21 ------------------
    print(
        "Creați o clasă 'Punct' pentru a reprezenta un punct într-un spațiu bidimensional, cu atribute pentru coordonatele x și y.")


    class Punct:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    punct = Punct(5, 10)
    print(f"Punctul are coordonatele: ({punct.x}, {punct.y})")

    # ------------------ Exercițiul 22 ------------------
    print("Adăugați o metodă 'distanta' în clasa 'Punct' care calculează distanța dintre două puncte.")

    import math


    class Punct:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distanta(self, alt_punct):
            return math.sqrt((self.x - alt_punct.x) ** 2 + (self.y - alt_punct.y) ** 2)


    punct1 = Punct(0, 0)
    punct2 = Punct(3, 4)
    print(f"Distanța dintre puncte este: {punct1.distanta(punct2)}")

    # ------------------ Exercițiul 23 ------------------
    print("Creați o clasă 'Cerc' care utilizează clasa 'Punct' pentru centrul său și are un atribut 'raza'.")


    class Cerc:
        def __init__(self, centru, raza):
            self.centru = centru
            self.raza = raza


    centru = Punct(0, 0)
    cerc = Cerc(centru, 5)
    print(f"Centrul cercului este la: ({cerc.centru.x}, {cerc.centru.y}), Raza: {cerc.raza}")

    # ------------------ Exercițiul 24 ------------------
    print("Adăugați o metodă 'arie' în clasa 'Cerc' care calculează și returnează aria cercului.")


    class Cerc:
        def __init__(self, centru, raza):
            self.centru = centru
            self.raza = raza

        def arie(self):
            return math.pi * self.raza ** 2


    cerc = Cerc(Punct(0, 0), 5)
    print(f"Aria cercului este: {cerc.arie()}")

    # ------------------ Exercițiul 25 ------------------
    print("Creați o clasă 'Dreptunghi' cu atribute pentru punctele stânga-sus și dreapta-jos.")


    class Dreptunghi:
        def __init__(self, stanga_sus, dreapta_jos):
            self.stanga_sus = stanga_sus
            self.dreapta_jos = dreapta_jos


    dreptunghi = Dreptunghi(Punct(0, 10), Punct(5, 0))
    print(
        f"Punctele dreptunghiului sunt: ({dreptunghi.stanga_sus.x}, {dreptunghi.stanga_sus.y}) "
        f"și ({dreptunghi.dreapta_jos.x}, {dreptunghi.dreapta_jos.y})")

    # ------------------ Exercițiul 26 ------------------
    print("Adăugați o metodă 'arie' în clasa 'Dreptunghi' care calculează și returnează aria dreptunghiului.")


    class Dreptunghi:
        def __init__(self, stanga_sus, dreapta_jos):
            self.stanga_sus = stanga_sus
            self.dreapta_jos = dreapta_jos

        def arie(self):
            latime = self.dreapta_jos.x - self.stanga_sus.x
            inaltime = self.stanga_sus.y - self.dreapta_jos.y
            return latime * inaltime


    dreptunghi = Dreptunghi(Punct(0, 10), Punct(5, 0))
    print(f"Aria dreptunghiului este: {dreptunghi.arie()}")
