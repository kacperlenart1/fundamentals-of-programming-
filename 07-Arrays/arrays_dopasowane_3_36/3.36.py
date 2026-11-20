### PLIK 3.36.py: Kompletna funkcja zamieniająca tablicę 2D na 1D oraz wypisanie wyników dla 3 przykładów.
def array_2d_to_1d(matrix):  # Zamienia tablicę dwuwymiarową na jednowymiarową.
    result = []  # Lista wynikowa jednowymiarowa.
    for row in matrix:  # Przechodzimy przez każdy wiersz tablicy 2D.
        for item in row:  # Przechodzimy przez każdy element w wierszu.
            result.append(item)  # Dopisujemy element do listy 1D.
    return result  # Zwracamy tablicę jednowymiarową.


example_2d_arrays = [  # Trzy tablice dwuwymiarowe podane w zadaniu.
    [[2, 3], [1, 5]],  # Tablica 1.
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],  # Tablica 2.
    [[2, 1], [3, 5], [7, 4], [2, 6]],  # Tablica 3.
]  # Koniec listy tablic.

for idx, arr_2d in enumerate(example_2d_arrays, start=1):  # Konwertujemy i wypisujemy każdą tablicę.
    print(f"1D array {idx}: {array_2d_to_1d(arr_2d)}")  # Wypisujemy wynikową tablicę 1D.
