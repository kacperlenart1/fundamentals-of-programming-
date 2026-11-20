### PLIK 1.14.py: Kompletna implementacja sortowania bąbelkowego (Bubble Sort) zgodnie z pseudokodem.
def bubble_sort(arr):  # Sortuje tablicę rosnąco algorytmem sortowania bąbelkowego.
    n = len(arr)  # Pobieramy długość tablicy.
    for i in range(n):  # Zewnętrzna pętla od 0 do n - 1.
        for j in range(0, n - i - 1):  # Wewnętrzna pętla porównująca sąsiednie elementy.
            if arr[j] > arr[j + 1]:  # Jeśli element lewy jest większy od prawego.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Zamieniamy elementy miejscami.
    return arr  # Zwracamy posortowaną tablicę.


sample_array = [29, 10, 14, 37, 13]  # Przykładowa tablica liczb.
print("Original array:", sample_array)  # Wypisujemy tablicę przed sortowaniem.
print("Sorted array:  ", bubble_sort(sample_array.copy()))  # Wypisujemy tablicę po sortowaniu.
