### PLIK 3.5.py: Kompletny program obliczający drugą potęgę każdego elementu tablicy [8, 2, 5, 1, 9] i wypisujący wyniki.
arr = [8, 2, 5, 1, 9]  # Tablica początkowa.
powers = []  # Lista przechowująca kwadraty elementów.

for value in arr:  # Obliczamy kwadrat każdego elementu w pętli.
    powers.append(value ** 2)  # Dopisujemy drugą potęgę do listy wynikowej.

print("Array:", *arr)  # Wypisujemy oryginalną tablicę.
print("2nd power:", *powers)  # Wypisujemy drugie potęgi elementów.
