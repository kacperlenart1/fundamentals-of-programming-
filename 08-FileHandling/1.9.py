import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 1.9.py: Program wyświetlający ponumerowaną listę pracowników na stanowisku Software Engineer z it_company.csv.
file_name = 'it_company.csv'  # Nazwa pliku z listą pracowników.
job_title = 'Software Engineer'  # Szukane stanowisko pracy.

counter = 1  # Licznik porządkowy dla znalezionych pracowników.
with open(file_name, 'r', encoding='utf-8') as file:  # Otwieramy plik CSV do odczytu.
    for line in file:  # Przechodzimy przez każdą linię w pliku.
        if job_title in line:  # Sprawdzamy, czy nazwa stanowiska występuje w bieżącej linii.
            print(f"{counter}. {line.strip()}")  # Wypisujemy numer i oczyszczoną linię pracownika.
            counter += 1  # Zwiększamy numer porządkowy o 1.
