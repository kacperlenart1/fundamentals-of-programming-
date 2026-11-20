import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.9.py: Program zliczający pojazdy z vehicle.txt według wyróżnika z province.csv.
import csv  # Importujemy moduł csv do odczytu pliku województw.

letter_to_province = {}  # Słownik: litera wyróżnika -> nazwa województwa.
with open("province.csv", "r", encoding="utf-8", newline="") as csv_file:  # Otwieramy plik province.csv.
    reader = csv.DictReader(csv_file)  # Wczytujemy wiersze na podstawie nagłówków Letter i Name.
    for row in reader:  # Przechodzimy przez kolejne województwa.
        letter = row["Letter"].strip().upper()  # Pobieramy literę wyróżnika.
        province = row["Name"].strip()  # Pobieramy nazwę województwa.
        letter_to_province[letter] = province  # Zapisujemy mapowanie litera -> województwo.

counts = {province: 0 for province in letter_to_province.values()}  # Inicjujemy liczniki dla każdego województwa.

with open("vehicle.txt", "r", encoding="utf-8") as veh_file:  # Otwieramy plik z numerami rejestracyjnymi.
    for line in veh_file:  # Czytamy kolejne tablice rejestracyjne.
        plate = line.strip().upper()  # Czyścimy białe znaki i ujednolicamy wielkość liter.
        if plate:  # Pomijamy puste linie.
            first_letter = plate[0]  # Bierzemy pierwszą literę rejestracji.
            if first_letter in letter_to_province:  # Sprawdzamy, czy wyróżnik jest w słowniku.
                province = letter_to_province[first_letter]  # Pobieramy nazwę województwa.
                counts[province] += 1  # Zwiększamy licznik pojazdów dla tego województwa.

for province, count in counts.items():  # Przechodzimy przez województwa i ich liczby pojazdów.
    print(f"{province}: {count}")  # Wypisujemy nazwę województwa oraz liczbę aut.
