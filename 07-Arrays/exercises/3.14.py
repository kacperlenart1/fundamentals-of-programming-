### PLIK 3.14.py: Kompletny program wypisujący wszystkie unikalne elementy tablicy (występujące dokładnie raz).
arr = [2, 3, 2, 5, 8, 1, 9, 8]  # Tablica z wartościami z przykładu.
unique_elements = []  # Lista przechowująca elementy unikalne.

for item in arr:  # Sprawdzamy każdy element tablicy.
    if arr.count(item) == 1:  # Element jest unikalny, gdy występuje w tablicy dokładnie jeden raz.
        unique_elements.append(item)  # Dodajemy element do listy unikalnych.

print("Array:", *arr)  # Wypisujemy oryginalną tablicę.
print("Unique elements:", *unique_elements)  # Wypisujemy unikalne elementy.
