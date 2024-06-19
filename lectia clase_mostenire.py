
if __name__=="__main__":

# Polimorfism
# Problema 1: Crează două clase, Animal și Mamifera, unde Mamifera moștenește de la Animal.
# Implementează metoda sune() în ambele clase astfel încât să fie diferite pentru fiecare clasă.
# Apoi, creează un obiect al clasei Mamifera și apelă metoda sune(). Ce se întâmplă?

    class Animal:
        def __init__(self, nume, culoare) -> None:
            self.nume = nume
            self.culoare = culoare

        def sunet(self):
            print("GAF GAF")
            return "gaf gaf"


    class Mamifer(Animal):
        def __init__(self, nume, culoare) -> None:
            super().__init__(nume, culoare)

        def sunet(self):
            print("Miau Miau")

    # Problema 2: Suprascrie metoda sune() în clasa Mamifera pentru a modifica comportamentul acesteia.
    # Creează un alt obiect al clasei Mamifera și apelă din nou metoda sune(). Cum se comportă acum metoda?

    # Moștenire
    # Problema 1: Defineste o clasă bază numită FormaGeometrica cu un atribut laturi.
    # Implementează un constructor care initializează acest atribut.
    # Apoi, creează două clase derivate, Pentagon și Cerc, care moșteneesc de la FormaGeometrica.
    # Pentru fiecare clasă derivată, adaugă un constructor care setează valoarea atributului laturi într-un mod corespunzător.

    # Problema 2: În clasa Cerc, suprascrie metoda __init__ pentru a permite definirea razei cercului în loc de laturile sale.
    # Demonstrează cum poți crea un obiect al clasei Cerc folosind noul constructor definit.

    # Încapsulare
    # Problema 1: Creează o clasă ContBancar cu atributul privat sold.
    # Implementează metode getter și setter pentru acest atribut.
    # Demonstrează cum poți accesa și modifica valoarea atributului sold prin intermediul acestor metode.

    class ContBancar:
        def __init__(self) -> None:
            self.__sold = 0

        def set_sold(self, sold_nou):
            self.__sold = sold_nou

        def get__sold(self):
            return self.__sold

    cont = ContBancar()
    print(cont.get__sold())


# Problema 2: În clasa ContBancar, implementează o metodă transferaza_bani care preia suma de bani
# și destinatarul ca parametri și transferă banii dintre conturile pe care le reprezintă.
# Demonstrează cum poți utiliza metodele getter și setter pentru a gestiona soldul conturilor în timpul operației de transfer.


# Abstracție
# Problema 1: Definește o clasă abstractă Transport cu metoda abstractă deplaseaza().
# Implementează clase derivate concrete Masina și Vapor care implementează metoda deplaseaza().
# Demonstrează cum poți crea instanțe ale acestor clase și cum poți apela metoda deplaseaza() pe ele.


from abc import ABC, abstractmethod


# Problema 2: În clasa abstractă Transport, adaugă un alt atribut abstract tip_de_transport.
# Implementează acest atribut în clasele derivate Masina și Vapor.
# Demonstrează cum poți crea instanțe ale acestor clase și cum poți accesa atributul tip_de_transport pe ele.
