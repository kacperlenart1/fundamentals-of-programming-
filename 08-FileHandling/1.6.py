import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 1.6.py: Program wczytujący zawartość pliku countries.txt i wypisujący kraje posortowane alfabetycznie.
def read_from_file(name):  # Wczytuje i zwraca całą zawartość pliku jako napis.
    with open(name, 'r', encoding='utf-8') as file:  # Otwieramy plik do odczytu.
        content = file.read()  # Czytamy cały tekst z pliku.
    return content  # Zwracamy odczytaną treść.


file_content = read_from_file('countries.txt')  # Odczytujemy całą zawartość pliku countries.txt.
file_lines = file_content.splitlines()  # Dzielimy tekst na listę pojedynczych linii.
sorted_lines = sorted(file_lines)  # Sortujemy listę linii alfabetycznie za pomocą sorted().

for line in sorted_lines:  # Przechodzimy przez posortowane linie.
    print(line)  # Wypisujemy każdą linię na ekranie.
