import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.11.py: Program rejestrujący głosy na wskazaną osobę i zapisujący wyniki do voting.json.
import json  # Importujemy moduł json.
from pathlib import Path  # Importujemy Path do sprawdzania istnienia pliku.

voting_file = Path("voting.json")  # Ścieżka do pliku voting.json.

if voting_file.exists():  # Jeśli plik już istnieje, wczytujemy dotychczasowe głosy.
    with open(voting_file, "r", encoding="utf-8") as file:  # Otwieramy voting.json do odczytu.
        votes = json.load(file)  # Wczytujemy słownik głosów.
else:  # Jeśli plik jeszcze nie istnieje.
    votes = {}  # Tworzymy pusty słownik na wyniki głosowania.

person_name = input("Name of the person you are voting for: ").strip()  # Pobieramy imię/nazwisko kandydata.
if person_name:  # Jeśli wpisano niepustą nazwę.
    votes[person_name] = votes.get(person_name, 0) + 1  # Zwiększamy liczbę głosów o 1 (lub ustawiamy 1).

with open(voting_file, "w", encoding="utf-8") as file:  # Otwieramy plik do zapisu.
    json.dump(votes, file, indent=4, ensure_ascii=False)  # Zapisujemy zaktualizowane głosy do JSON.

print("Current voting results:", votes)  # Wypisujemy aktualny stan głosów.
