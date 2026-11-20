### PLIK 3.21.py: Kompletny program sprawdzający czy pierwsza tablica jest podzbiorem drugiej tablicy.
array1 = [3, 7, 15]  # Pierwsza tablica.
array2 = [1, 3, 5, 7, 9, 15, 20]  # Druga tablica.

is_subset = True  # Zakładamy na start, że array1 jest podzbiorem array2.
for item in array1:  # Sprawdzamy każdy element pierwszej tablicy.
    if item not in array2:  # Jeśli elementu nie ma w drugiej tablicy.
        is_subset = False  # Ustawiamy False.
        break  # Kończymy pętlę.

print("First array:", array1)  # Wypisujemy pierwszą tablicę.
print("Second array:", array2)  # Wypisujemy drugą tablicę.
print("Is first array a subset of the second:", is_subset)  # Wypisujemy wynik sprawdzenia.
