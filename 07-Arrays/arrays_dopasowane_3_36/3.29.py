### PLIK 3.29.py: Kompletna funkcja create_2d_arr(x, y) tworząca tablicę zer oraz utworzenie i wypisanie tablicy 3 na 5.
def create_2d_arr(x, y):  # Tworzy i zwraca tablicę dwuwymiarową x na y wypełnioną zerami.
    return [[0 for _ in range(y)] for _ in range(x)]  # Tworzymy x wierszy po y zer w każdym.


arr_3x5 = create_2d_arr(3, 5)  # Tworzymy tablicę dwuwymiarową o wymiarach 3 na 5.
print("Created 3x5 array:", arr_3x5)  # Wypisujemy utworzoną tablicę.
