import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 1.7.py: Program obliczający łączną liczbę zaparkowanych samochodów na podstawie pliku car_park.txt.
def read_from_file(name):  # Wczytuje i zwraca zawartość wskazanego pliku.
    with open(name, 'r', encoding='utf-8') as file:  # Otwieramy plik do odczytu.
        content = file.read()  # Pobieramy całą zawartość pliku.
    return content  # Zwracamy wczytany napis.


file_content = read_from_file('car_park.txt')  # Odczytujemy dane z pliku car_park.txt.
file_lines = file_content.splitlines()  # Dzielimy zawartość na listę linii.

total = 0  # Zmienna akumulująca łączną liczbę zaparkowanych aut.
for line in file_lines:  # Przechodzimy przez każdą linię z listy.
    total += int(line)  # Zamieniamy tekst z linii na liczbę całkowitą i dodajemy do sumy.

print('Total cars parked:', total)  # Wypisujemy łączną liczbę zaparkowanych samochodów.
