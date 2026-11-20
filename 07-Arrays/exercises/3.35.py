### PLIK 3.35.py: Kompletna funkcja transpose_matrix(m) oraz wypisanie transponowanych macierzy dla 3 przykładów.
def transpose_matrix(m):  # Zwraca transponowaną macierz m (zamienia wiersze z kolumnami).
    num_rows = len(m)  # Liczba wierszy macierzy m.
    num_cols = len(m[0])  # Liczba kolumn macierzy m.
    return [[m[r][c] for r in range(num_rows)] for c in range(num_cols)]  # Tworzymy macierz transponowaną.


def print_2d_array(matrix):  # Wypisuje macierz w wierszach i kolumnach.
    for row in matrix:  # Przechodzimy przez każdy wiersz macierzy.
        print(*row)  # Wypisujemy wartości wiersza.


example_matrices = [  # Trzy macierze podane w zadaniu.
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Macierz 1.
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],  # Macierz 2.
    [[5, 6, 7, 8]],  # Macierz 3.
]  # Koniec listy macierzy.

for idx, mat in enumerate(example_matrices, start=1):  # Transponujemy i wypisujemy każdą macierz.
    print(f"Transposed matrix {idx}:")  # Nagłówek wyniku.
    print_2d_array(transpose_matrix(mat))  # Wypisujemy transponowaną macierz.
    print()  # Pusta linia oddzielająca.
