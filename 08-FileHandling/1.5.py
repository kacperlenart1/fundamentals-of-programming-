import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 1.5.py: Program odczytujący plik countries.txt linia po linii i wypisujący ponumerowaną listę krajów.
with open('countries.txt', 'r', encoding='utf-8') as file:  # Otwieramy plik countries.txt do odczytu.
    counter = 1  # Licznik numerujący kolejne linie od 1.
    for line in file:  # Przechodzimy przez każdą linię w pliku.
        print(f"{counter}. {line}", end="")  # Wypisujemy numer i linię (bez podwójnego entera dzięki end="").
        counter += 1  # Zwiększamy licznik o 1.
