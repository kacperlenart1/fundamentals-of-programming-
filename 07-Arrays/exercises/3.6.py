### PLIK 3.6.py: Kompletny program znajdujący najmniejszą i największą liczbę w tablicy bez użycia funkcji wbudowanych.
arr = [-15, 8, -31, 47, -2, 19]  # Tablica liczb całkowitych.
min_num = arr[0]  # Przyjmujemy pierwszy element jako aktualne minimum.
max_num = arr[0]  # Przyjmujemy pierwszy element jako aktualne maksimum.

for value in arr:  # Sprawdzamy każdy element tablicy.
    if value < min_num:  # Jeśli bieżący element jest mniejszy od minimum.
        min_num = value  # Aktualizujemy wartość minimalną.
    if value > max_num:  # Jeśli bieżący element jest większy od maksimum.
        max_num = value  # Aktualizujemy wartość maksymalną.

print("Array:", *arr)  # Wypisujemy tablicę.
print("Minimum number:", min_num)  # Wypisujemy najmniejszą liczbę.
print("Maximum number:", max_num)  # Wypisujemy największą liczbę.
