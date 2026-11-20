### PLIK 3.7.py: Kompletny program obliczający średnią arytmetyczną elementów tablicy [15, 8, 31, 47, 2, 19] w pętli for.
arr = [15, 8, 31, 47, 2, 19]  # Tablica wartości.
total = 0  # Suma elementów tablicy.

for value in arr:  # Sumujemy wszystkie elementy w pętli for.
    total += value  # Dodajemy element do sumy.

mean = total / len(arr)  # Obliczamy średnią arytmetyczną.
print("Array:", *arr)  # Wypisujemy elementy tablicy.
print("Arithmetic mean:", mean)  # Wypisujemy średnią arytmetyczną.
