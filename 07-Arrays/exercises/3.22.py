### PLIK 3.22.py: Kompletna funkcja rand_elem(array) zwracająca losowy element tablicy oraz kilka wypisań losowych elementów.
import random  # Importujemy moduł random.


def rand_elem(array):  # Zwraca losowo wybrany element z przekazanej tablicy.
    return random.choice(array)  # Losujemy jeden element z tablicy.


sample_arr = [11, 22, 33, 44, 55, 66, 77]  # Przykładowa tablica.
print("Array:", sample_arr)  # Wypisujemy tablicę.
for i in range(5):  # Wypisujemy pięć losowo wybranych elementów.
    print(f"Random element {i + 1}: {rand_elem(sample_arr)}")  # Wywołujemy funkcję rand_elem.
