import math
import time

if __name__ == "__main__":
    print("Bun venit la tema pentru acasa 05.05 - functii de ordin inalt, decorator")

    # ------------------ Exercițiul 1 ------------------
    print("1. Transforma fiecare element dintr-o lista de numere în valoarea sa pătrată.")

    numere = [2, 3, 4, 5]
    patrate = list(map(lambda x: x ** 2, numere))
    print(patrate)

    # Metoda 2 - cu ajutorul functiei map
    # map(functie, iterabil)

    # ------------------ Exercițiul 2 ------------------
    print("2. Converteste fiecare element dintr-o lista de string-uri în format inversat.")

    cuvinte = ["python", "cod", "programare"]
    inversat = list(map(lambda x: x[::-1], cuvinte))
    print(inversat)

    # ------------------ Exercițiul 3 ------------------
    print("3. Converteste fiecare temperatura din grade Celsius în grade Fahrenheit.")
    temperaturi_celsius = [0, 32, 100]
    # Solutia: c->f este (c * 9/5) + 32

    fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturi_celsius))
    print(fahrenheit)

    # ------------------ Exercițiul 4 ------------------
    print("4. Elimina spatii albe de la inceputul si sfarsitul fiecarui string din lista.")
    cuvinte_spatii = [" ana ", " are ", " mere "]

    fara_spatii = list(map(lambda x: x.strip(), cuvinte_spatii))
    print(fara_spatii)

    # ------------------ Exercițiul 1 ------------------
    print(
        "1. Data fiind o lista de puncte tridimensionale in format de tuplu: (coordonata_x, coordonata_y, coordonata_z)"
        "creeaza o lista noua care sa contina distantele punctelor de la originea sistemului de coordonate (0, 0, 0)"
    )
    puncte = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

    # Metoda 2 - cu map

    # ------------------ Exercițiul 1 ------------------
    print("1. Filtrare numere mai mari de 5 dintr-o listă.")
    numere = [1, 4, 6, 7, 8]
    # Solutia:

    # ------------------ Exercițiul 2 ------------------
    print("2. Filtrare cuvinte care contin litera 'a'.")
    cuvinte = ["mama", "tata", "frate", "sor"]
    # Solutia:

    # ------------------ Exercițiul 3 ------------------
    print("3. Filtrare numere pozitive dintr-o listă.")
    numere = [-2, -1, 0, 1, 2]
    # Solutia:

    # ------------------ Exercițiul 4 ------------------
    print("4. Selecteaza doar numerele care sunt pătrate perfecte din lista.")
    numere = [1, 2, 3, 4, 5, 16, 25]
    # math.sqrt(number) = number ** (0.5)
    # Solutia:

    # ------------------ Exercițiul 2 ------------------
    print(
        "2. Data fiind o lista imbricata continant raspunsuri la un test de algebra, filtreaza (scoate) elementele"
        "unde elevii nu au dat raspuns (notate print NaN - din engleza - not a number)"
    )
    import math

    NaN = float('nan')
    print(NaN, type(NaN))
    scores = [[NaN, 12, 0.5, 78, math.pi],
              [2, 13, 0.5, 0.7, math.pi / 2],
              [2, NaN, 0.5, 78, math.pi],
              [2, 14, 0.5, 39, 1 - math.pi]]

    # Solutie

    # ------------------ Exercițiul 1 ------------------
    print("1. Calculează suma elementelor unei liste.")
    numere = [1, 1, 1, 1, 5]
    from functools import reduce

    # Solutia:

    # ------------------ Exercițiul 1.1 ------------------
    print("1.1. Calculează media elementelor unei liste.")
    numere = [1, 2, 3, 4, 5]
    # Solutia:

    # ------------------ Exercițiul 2 ------------------
    print("2. Folosind reduce, determină diferența dintre cel mai mare și cel mai mic număr din listă.")
    numere = [5, 2, 8, 3, 9, 1]
    # Solutia:

    # ------------------ Exercițiul 3 ------------------
    print("3. Folosind reduce, obține numărul de caractere din toate cuvintele unei liste.")
    cuvinte = ["Python", "este", "minunat"]


    # Solutia:

    # ====================== Lucru Decoratori ======================
    def hello_solar_system(old_function):
        def wrapper_function(planet=None):
            print("Hello Solar System")
            old_function(planet)

        return wrapper_function


    def hello_galaxy(old_function):
        def wrapper_function(planet=None):
            print("Hello Milky Way Galaxy")
            old_function(planet)

        return wrapper_function


    @hello_galaxy
    @hello_solar_system
    def hello(planet=None):
        if planet:
            print(f"Hello, {planet}")
        else:
            print("Hello, world!")


    hello("Mars")

    # ------------------ Exercițiul 1 ------------------
    print("1. Creeaza un decorator simplu care printeaza 'Inainte de apelul functiei' si 'Dupa apelul functiei'.")


    # Solutia

    def decorator_simplu(func):
        def wrapper():
            print('Inainte de apelul functiei')
            start = time.time()
            func()
            end = time.time()
            print('Dupa apelul functiei')
            print(f"Total timp de executie a functiei {func.__name__} este: ", end - start)

        return wrapper


    @decorator_simplu
    def functie_simpla():
        print("Executie in functie simpla.")


    functie_simpla()

    # # ------------------ Exercițiul 2 ------------------
    # print("2. Scrie un decorator care sa printeze numele functiei apelate.")
    # # Solutia
    #
    #
    # ------------------ Exercițiul 3  ------------------
    print("3. Implementeaza un decorator care sa dubleze valoarea returnata de o functie.")


    # Solutia
    def decrator_dubleaza(func):
        def wrapper(multiplication_number):
            return multiplication_number * func()

        return wrapper


    @decrator_dubleaza
    def returneaza_10():
        return 10


    print(returneaza_10(multiplication_number=3))

    # # ------------------ Exercițiul 3.1  ------------------
    # print("3.1. Modifica implementarea de mai sus ca sa ia orice numar, nu doar 2 (adica nu doar sa dubleze).")
    # # Solutia

    # ------------------ Exercițiul 3.2  ------------------
    print("3.2. Acum modifica implementarea de mai sus ca sa ia orice numar, nu doar 2 (adica nu doar sa dubleze)"
          " ci si sa returneze orice numar - nu doar 10 (intainte de dublura)")


    # Solutia

    def decrator_dubleaza(func):
        def wrapper(multiplication_number, target_nr):
            return multiplication_number * func(target_nr)

        return wrapper


    @decrator_dubleaza
    def returneaza_numar(target_nr):
        return target_nr


    print(returneaza_numar(multiplication_number=5, target_nr=9))

    # ------------------ Exercițiul 4 ------------------
    print(
        "Foloseste *args si **kwargs pentru a permite decoratorului sa accepte orice functie, indiferent de argumentele sale.")


    # Solutia
    def decrator_dubleaza(func):
        def wrapper(*args, **kwargs):
            print("Se executa functia cu argumente variablie")
            return func(*args, **kwargs)

        return wrapper


    @decrator_dubleaza
    def functie_cu_variabile(a, b, c=3):
        print(a, b, c)


    functie_cu_variabile(1, 2)
    functie_cu_variabile(1, 2, c=4)

    # ------------------ Exercițiul 5 ------------------
    print(
        "5. Foloseste **kwargs in decorator prin implementarea unui decorator care adauga argumente suplimentare.")


    # Solutia
    def adauga_argument_suplimentar(func):
        def wrapper(*args, **kwargs):
            kwargs['argument_nou'] = "Valoarea noua"
            kwargs['argument_cel_mai_nou'] = "Valoarea cea mai noua"
            return func(*args, **kwargs)

        return wrapper


    @adauga_argument_suplimentar
    def functie_cu_kwargs(**kwargs):
        for cheie, valoare in kwargs.items():
            print(f"{cheie}: {valoare}")


    functie_cu_kwargs(argument_initial="Voaloarea initiala")

    # # ------------------ Exercițiul 6 ------------------
    # print(
    #     "6. Demonstreaza cum *args si **kwargs permit unui decorator sa fie folosit cu functii care au un numar variabil de argumente.")

    def decorator_flexibil(func):
        def wrapper(*args, **kwargs):
            print("Argumente pozitionale:", args)
            print("Argumente cuvant-cheie:", kwargs)
            return func(*args, **kwargs)

        return wrapper


    @decorator_flexibil
    def functie_flexibila(*args, **kwargs):
        print("Functie cu argumente variabile")


    functie_flexibila(1, 2, 3, nume="Andrei", varsta=30)



    #
    # # ------------------ Exercițiul 7 ------------------
    # print("7. Utilizeaza *args si **kwargs pentru a crea un decorator care modifica argumentele unei functii.")
    # # Solutia
    #
    # # ------------------ Exercițiul 8 ------------------
    # print("8. Scrie un decorator care afiseaza timpul de executie al unei functii.")
    # # Solutia
    #
    # # ------------------ Exercițiul 9 ------------------
    # print("9. Implementeaza un decorator 'autentificare' care cere un parola inainte de a permite apelul unei functii.")
    # # Solutia
    #
