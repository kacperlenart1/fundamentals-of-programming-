import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.4.py: Program wyświetlający kolejne linie pliku po 5 na raz i czekający na naciśnięcie Enter.
file_name = "it_company.csv"  # Nazwa pliku wejściowego.

with open(file_name, "r", encoding="utf-8") as file:  # Otwieramy plik do odczytu w UTF-8.
    line_counter = 0  # Licznik linii wypisanych w bieżącej paczce.
    for line in file:  # Czytamy plik linia po linii.
        print(line.rstrip())  # Wypisujemy linię bez końcowego znaku nowej linii.
        line_counter += 1  # Zwiększamy licznik wypisanych linii.
        if line_counter == 5:  # Po każdych 5 liniach prosimy o naciśnięcie Enter.
            input("Press Enter key...")  # Czekamy na wciśnięcie klawisza Enter przez użytkownika.
            line_counter = 0  # Zerujemy licznik dla kolejnej paczki 5 linii.
