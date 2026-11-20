### PLIK 2.6.py: Kompletny program ustawiający 1 na głównej przekątnej macierzy 3x3 w pętli i wypisujący macierz.
matrix = [  # Macierz kwadratowa 3x3 wypełniona zerami.
    [0, 0, 0],  # Wiersz 1.
    [0, 0, 0],  # Wiersz 2.
    [0, 0, 0]   # Wiersz 3.
]  # Koniec macierzy.

for i in range(len(matrix)):  # Przechodzimy po indeksach głównej przekątnej (0, 1, 2).
    matrix[i][i] = 1  # Ustawiamy wartość 1 na głównej przekątnej.

for row in matrix:  # Wypisujemy zmodyfikowaną macierz wiersz po wierszu.
    for val in row:  # Wypisujemy wartości w bieżącym wierszu.
        print(val, end=" ")  # Drukujemy wartość i spację.
    print()  # Przechodzimy do nowej linii po wierszu.
