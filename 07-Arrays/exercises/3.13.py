### PLIK 3.13.py: Kompletna funkcja bubblesort(array) oraz posortowanie i wypisanie trzech tablic liczb całkowitych.
def bubblesort(array):  # Sortuje tablicę rosnąco algorytmem sortowania bąbelkowego i zwraca nową posortowaną tablicę.
    arr = array.copy()  # Tworzymy kopię wejściowej tablicy.
    n = len(arr)  # Pobieramy długość tablicy.
    for i in range(n):  # Przebiegi pętli zewnętrznej.
        for j in range(0, n - i - 1):  # Porównujemy sąsiednie elementy.
            if arr[j] > arr[j + 1]:  # Jeśli element po lewej jest większy od prawego.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Zamieniamy je miejscami.
    return arr  # Zwracamy posortowaną tablicę.


arrays_to_sort = [  # Trzy przykładowe tablice liczb całkowitych.
    [64, 34, 25, 12, 22, 11, 90],  # Tablica 1.
    [-10, 5, 0, -3, 18, 2],  # Tablica 2.
    [100, 45, 78, 12, 56],  # Tablica 3.
]  # Koniec listy tablic.

for idx, sample in enumerate(arrays_to_sort, start=1):  # Sortujemy i wypisujemy każdą z trzech tablic.
    print(f"Array {idx} before sort:", sample)  # Wypisujemy tablicę przed sortowaniem.
    print(f"Array {idx} after sort: ", bubblesort(sample))  # Wypisujemy tablicę po sortowaniu.
