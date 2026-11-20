### PLIK 1.5.py: Kompletny program modyfikujący listę [1, 2, 3, 4, 5] i wypisujący jej zawartość po każdej zmianie.
arr = [1, 2, 3, 4, 5]  # Tworzymy tablicę z wartościami 1, 2, 3, 4, 5.
print(f"Array: {arr}")  # Wypisujemy początkową zawartość tablicy.

arr[0] -= 1  # Odejmujemy 1 od pierwszego elementu tablicy.
print(f"Array: {arr}")  # Wypisujemy tablicę po odjęciu 1 od pierwszego elementu.

arr[-1] += 4  # Zwiększamy ostatni element tablicy o 4.
print(f"Array: {arr}")  # Wypisujemy tablicę po zwiększeniu ostatniego elementu o 4.

arr[len(arr) // 2] *= 2  # Mnożymy środkowy element tablicy przez 2.
print(f"Array: {arr}")  # Wypisujemy tablicę po pomnożeniu środkowego elementu przez 2.
