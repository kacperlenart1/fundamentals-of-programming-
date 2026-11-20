import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 2.4.py: Program zapisujący dane pracowników ze stanowiska Software Engineer do pliku software_engineer.txt.
employees_file = 'it_company.csv'  # Plik wejściowy z listą pracowników.
position_file = 'software_engineer.txt'  # Plik wyjściowy dla wybranego stanowiska.
job_title = 'Software Engineer'  # Nazwa stanowiska do przefiltrowania.

with open(employees_file, 'r', encoding='utf-8') as src:  # Otwieramy plik z pracownikami do odczytu.
    with open(position_file, 'w', encoding='utf-8') as dst:  # Otwieramy plik wynikowy do zapisu.
        for line in src:  # Przechodzimy linia po linii przez dane pracowników.
            if job_title in line:  # Jeśli linia dotyczy szukanego stanowiska.
                dst.write(line)  # Zapisujemy tę linię do pliku software_engineer.txt.
