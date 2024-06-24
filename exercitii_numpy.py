import numpy as np
from colorama import init, Back

init(autoreset=True)


def g(sir):
    return Back.BLACK + sir + "\n"



if __name__ == "__main__":
    print("Bun venit la tema 07.01 - NumPy, Pandas")

    # ------------------ Exercițiul 1 ------------------
    print(g("Creați un array NumPy unidimensional de 10 zerouri."))

    arr = np.zeros(10)
    print(arr)

    # types at https://numpy.org/doc/stable/user/basics.types.html

    # ------------------ Exercițiul 2 ------------------
    print(g("Creați un array NumPy de dimensiunea 10x10 plin cu valori de 3.14."))

    arr = np.full((10, 10), 3.14)
    print(arr)

    # ------------------ Exercițiul 3 ------------------
    print(g("Creați un array NumPy care conține toate numerele pare între 10 și 50."))

    arr = np.arange(10, 50, 2)
    print(arr)

    # ------------------ Exercițiul 4 ------------------
    print(g("Generați un array de 10 numere aleatorii între 0 și 1."))

    arr = np.random.rand(10)
    print(arr)

    # ------------------ Exercițiul 5 ------------------
    print(g("Creați o matrice identitate de dimensiune 5x5."))

    arr = np.eye(5)
    print(arr)

    # ------------------ Exercițiul 6 ------------------
    print(g("Găsiți valoarea maximă și minimă dintr-un array NumPy generat aleator."))

    arr = np.random.rand(10)
    print(f"Valoarea maxima: {arr.max()}, \nValoarea minima: {arr.min()}")

    # ------------------ Exercițiul 7 ------------------
    print(g("Sortați un array NumPy generat aleator."))
    arr = np.random.rand(10)
    arr.sort()
    print(arr)

    # ------------------ Exercițiul 8 ------------------
    print(g("Creați un array bidimensional și transformați-l într-un array unidimensional."))

    arr = np.array([[1, 2, 7],
                    [4, 5, 6]])
    arr_flat = arr.flatten()
    print(arr_flat)

    # ------------------ Exercițiul 9 ------------------
    print(g("Concatenați două array-uri NumPy."))

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr_concat = np.concatenate([arr1, arr2])
    print(arr_concat)


    # ------------------ Exercițiul 10 ------------------
    print("Inversați un array NumPy.")

    arr = np.array([1, 2, 3, 4, 5])
    print(arr[::-1])

    # ------------------ Exercițiul 11 ------------------
    print(g("Creați un array bidimensional unde limita exterioară este 1, iar interiorul este 0."))

    arr = np.ones((5, 5))
    arr[1:-1, 1:-1] = 0
    print(arr)

    # ------------------ Exercițiul 12 ------------------
    print(g("Adunați o valoare la toate elementele dintr-un array NumPy."))
    arr = np.arange(10)
    arr += 5
    print(arr)

    # ------------------ Exercițiul 13 ------------------
    print(g("Multiplicați fiecare element dintr-un array NumPy cu un scalar."))

    arr = np.arange(5)
    arr *= 2
    print(arr)

    # ------------------ Exercițiul 14 ------------------
    print(g("Creați un array NumPy de 4x4 cu valori de la 0 la 15."))

    arr = np.arange(16).reshape(4, 4)
    print(arr)

    # ------------------ Exercițiul 15 ------------------
    print(g("Înlocuiți toate valorile pozitive dintr-un array NumPy cu valoarea -1."))

    arr = np.array([1, -2, 3, -4, 5])
    arr[arr > 0] = -1
    print(arr)

    # ------------------ Exercițiul 16 ------------------
    print(g("Extrageți toate numerele impare dintr-un array NumPy."))

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr_impar = arr[arr % 2 == 1]
    print(arr_impar)

    # ------------------ Exercițiul 17 ------------------
    print(g("Schimbați forma unui array NumPy din 1D în 2D cu 2 rânduri."))

    arr = np.arange(8)
    arr_reshaped = arr.reshape(2, -1)
    print(arr_reshaped)

    # ------------------ Exercițiul 18 ------------------
    print(g("Stivați vertical două array-uri NumPy."))

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr_vstack = np.vstack([arr1, arr2])
    print(arr_vstack)

    # ------------------ Exercițiul 19 ------------------
    print("Calculați media, mediana și deviația standard a unui array NumPy.")

    arr = np.random.rand(10)
    arr_media = np.mean(arr)
    arr_mediana = np.median(arr)
    arr_standard = np.std(arr)
    print(f"Media: {arr_media}, Mediana: {arr_mediana}, Deviația standard: {arr_standard}")

    # ------------------ Exercițiul 20 ------------------
    print(g("Găsiți indexii unde elementele unui array NumPy sunt egale cu un anumit scalar."))

    arr = np.array([1, 2, 3, 4, 5, 2, 3, 4])
    arr_index = np.where(arr == 2)
    print(arr_index)

    # ------------------ Exercițiul 21 ------------------
    """
    Exercițiul: Analiza Nivelurilor de Dioxid de Azot (NO2) într-o Locație Urbană
    Obiectiv: Scopul acestui exercițiu este de a analiza variațiile concentrației de dioxid de azot (NO2) într-o
    locație urbană pe parcursul unui an, folosind date reale obținute din măsurători zilnice. Această analiză va
    contribui la evaluarea calității aerului și la identificarea posibilelor riscuri pentru sănătatea publică.

    Datele: Se presupune că aveți la dispoziție un set de date în format CSV (no2_concentratii.csv), care conține
    înregistrări zilnice ale concentrațiilor de NO2 măsurate într-o anumită locație urbană. Fiecare înregistrare în
    fișierul CSV este formată din două coloane: data (în formatul YYYY-MM-DD) și no2 (concentrația de NO2 exprimată
    în µg/m³).

    Cerințe de Analiză:

    Concentrația Medie Anuală de NO2:

    Calculați și afișați concentrația medie anuală de NO2. Acest lucru va oferi o imagine de ansamblu asupra calității
    aerului pe parcursul întregului an.
    Ziua cu Concentrația Maximă de NO2:

    Identificați și afișați data (ziua) în care a fost înregistrată concentrația maximă de NO2, împreună cu valoarea
    concentrației respective. Aceasta va ajuta la identificarea potențialelor surse acute de poluare.
    Numărul de Zile cu Concentrații Peste Limita Legală:

    Calculați și afișați numărul de zile în care concentrația de NO2 a depășit limita legală (de exemplu, 40 µg/m³,
    conform standardelor UE pentru calitatea aerului). Această informație este crucială pentru evaluarea conformității cu
    reglementările privind calitatea aerului.
    Media Concentrației Lunare de NO2:

    Grupați datele pe luni și calculați media concentrației de NO2 pentru fiecare lună. Afișați aceste medii lunare.
    Aceasta va permite identificarea tendințelor sezoniere și a lunilor cu calitate scăzută a aerului.
    """

    import pandas as pd

    # Încărcați setul de date din fișierul CSV (no2_concentratii.csv)
    # Presupunem că coloanele sunt numite "data" și "no2"

    df = pd.read_csv("/Users/vadimoala/Documents/GitHub/tekwillacademy/no2_concentratii.csv", parse_dates=["data"])

    # Calculați concentrația medie anuală de NO2
    media_anuala_no2 = df["no2"].mean()

    # Găsiți înregistrarea cu cea mai mare valoare de NO2
    max_no2 = df.loc[df["no2"].idxmax()]

    # Numărați zilele cu concentrații peste limita legală (de exemplu, 40 µg/m³)
    zile_peste_limita = (df["no2"] > 40).sum()

    # Calculați media concentrației lunare de NO2
    media_lunara_no2 = df.groupby(df["data"].dt.month)["no2"].mean()

    # Afișați rezultatele
    print(f"Concentrația medie anuală de NO2: {media_anuala_no2:.2f} µg/m³")
    print(f"Ziua cu concentrația maximă de NO2: {max_no2['data'].date()} ({max_no2['no2']:.2f} µg/m³)")
    print(f"Numărul de zile cu concentrații peste limita legală: {zile_peste_limita}")
    print("Media concentrației lunare de NO2:")
    print(media_lunara_no2)



