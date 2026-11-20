### PLIK 3.34.py: Kompletna funkcja identity_matrix(n), wypisywanie macierzy 2D oraz macierze jednostkowe 3, 5 i 8.
def identity_matrix(n):  # Zwraca macierz jednostkową (tablicę 2D) o wymiarze n x n.
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # Jedynki na przekątnej, zera poza przekątną.


def print_2d_array(matrix):  # Wypisuje tablicę dwuwymiarową w wierszach i kolumnach.
    for row in matrix:  # Przechodzimy przez każdy wiersz macierzy.
        print(*row)  # Wypisujemy elementy wiersza oddzielone spacją.


for size in [3, 5, 8]:  # Tworzymy i wypisujemy macierze jednostkowe o wymiarach 3, 5 oraz 8.
    print(f"Identity matrix {size}x{size}:")  # Nagłówek dla macierzy danego rozmiaru.
    print_2d_array(identity_matrix(size))  # Wypisujemy macierz w wierszach i kolumnach.
    print()  # Wypisujemy pustą linię pomiędzy macierzami.
