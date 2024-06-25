# Exercițiul: Analiza Nivelurilor de Dioxid de Azot (NO2) într-o Locație Urbană
#     Obiectiv: Scopul acestui exercițiu este de a analiza variațiile concentrației de dioxid de azot (NO2) într-o
#     locație urbană pe parcursul unui an, folosind date reale obținute din măsurători zilnice. Această analiză va
#     contribui la evaluarea calității aerului și la identificarea posibilelor riscuri pentru sănătatea publică.
#
#     Datele: Se presupune că aveți la dispoziție un set de date în format CSV (no2_concentratii.csv), care conține
#     înregistrări zilnice ale concentrațiilor de NO2 măsurate într-o anumită locație urbană. Fiecare înregistrare în
#     fișierul CSV este formată din două coloane: data (în formatul YYYY-MM-DD) și no2 (concentrația de NO2 exprimată
#     în µg/m³).
#
#     Cerințe de Analiză:
#
#     Concentrația Medie Anuală de NO2:
#
#     Calculați și afișați concentrația medie anuală de NO2. Acest lucru va oferi o imagine de ansamblu asupra calității
#     aerului pe parcursul întregului an.
#     Ziua cu Concentrația Maximă de NO2:
#
#     Identificați și afișați data (ziua) în care a fost înregistrată concentrația maximă de NO2, împreună cu valoarea
#     concentrației respective. Aceasta va ajuta la identificarea potențialelor surse acute de poluare.
#     Numărul de Zile cu Concentrații Peste Limita Legală:
#
#     Calculați și afișați numărul de zile în care concentrația de NO2 a depășit limita legală (de exemplu, 40 µg/m³,
#     conform standardelor UE pentru calitatea aerului).
#     Această informație este crucială pentru evaluarea conformității cu
#     reglementările privind calitatea aerului.
#     Media Concentrației Lunare de NO2:
#
#     Grupați datele pe luni și calculați media concentrației de NO2 pentru fiecare lună. Afișați aceste medii lunare.
#     Aceasta va permite identificarea tendințelor sezoniere și a lunilor cu calitate scăzută a aerului.
#



import pandas as pd

# Incarcam fisierul CSV intr-un DataFrame
df = pd.read_csv('no2_concentratii.csv')

# Vizualizam primele cateva inregistrari pentru a intelege structura datelor
print(df.head())

# Calculam concentratia media anuala de NO2
concentratie_medie_anuala = df['no2'].mean()
print(f"Concentratia medie anuala de NO2: {concentratie_medie_anuala:2f} µg/m³")

# Identificam ziua cu concentratia maxima de NO2
max_no2_day = df.loc[df['no2'].idxmax()]
print(f"Ziua cu concentratia maxima de NO2: {max_no2_day['data']} - {max_no2_day['no2']} µg/m³")

# Calculam numarul de zile in care concentratia de NO2 a depasit 20 µg/m³
num_zile_peste_limita = df[df['no2'] > 40]['no2'].count()
print(f"Numarul de zile cu concentratii peste limita legala (40 µg/m³): {num_zile_peste_limita}")

# Adaugam o coloana pentru luna
df['luna'] = pd.to_datetime(df['data']).dt.month

# Calculam media concentratiei lunare de NO2
medii_lunare = df.groupby('luna')['no2'].mean()
print("Mediile lunare ale concentratiei de NO2:")
print(medii_lunare)



