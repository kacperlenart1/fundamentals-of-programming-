### PLIK 3.2.py: Kompletny program tworzący i wypisujący wszystkie 14 tablic jednowymiarowych i dwuwymiarowych.
import random  # Importujemy moduł random do losowania liczb.

arr1 = [3, 7, 1, 0, 4]  # Tablica z wartościami 3, 7, 1, 0, 4.
arr2 = [[2, 3], [7, 1], [0, 4]]  # Tablica dwuwymiarowa 3x2.
arr3 = [7 for i in range(5)]  # Pięcioelementowa tablica wypełniona 7.
arr4 = [i for i in range(1, 10)]  # Liczby od 1 do 9.
arr5 = [i * 2 for i in range(1, 10)]  # Liczby parzyste od 2 do 18.
arr6 = [random.randint(1, 20) for i in range(10)]  # 10 losowych liczb całkowitych z zakresu 1..20.
arr7 = [[] for i in range(5)]  # Tablica pięciu pustych list.
arr8 = [[1 for i in range(2)] for j in range(4)]  # Tablica 4x2 wypełniona jedynkami.
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]  # Tablica 5x3 losowych liczb 1..20.
arr_403 = [4, 0, 3]  # Tablica z wartościami 4, 0, 3.
arr_zeros_15 = [0 for _ in range(15)]  # Piętnastoelementowa tablica wypełniona zerami.
arr_range_1_30 = [random.randint(1, 30) for _ in range(12)]  # Tablica liczb całkowitych z zakresu <1, 30>.
arr_0_or_1_20 = [random.randint(0, 1) for _ in range(20)]  # Dwudziestoelementowa tablica losowo wypełniona 0 lub 1.
arr_false_5x2 = [[False for _ in range(2)] for _ in range(5)]  # Tablica dwuwymiarowa 5x2 wypełniona False.

all_arrays = [  # Lista wszystkich utworzonych tablic wraz z ich nazwami.
    ("arr1", arr1), ("arr2", arr2), ("arr3", arr3), ("arr4", arr4), ("arr5", arr5),
    ("arr6", arr6), ("arr7", arr7), ("arr8", arr8), ("arr9", arr9),
    ("arr_403", arr_403), ("arr_zeros_15", arr_zeros_15), ("arr_range_1_30", arr_range_1_30),
    ("arr_0_or_1_20", arr_0_or_1_20), ("arr_false_5x2", arr_false_5x2),
]  # Koniec listy tablic.

for name, array in all_arrays:  # Wypisujemy zawartość każdej utworzonej tablicy.
    print(f"{name}: {array}")  # Drukujemy nazwę tablicy oraz jej elementy.
