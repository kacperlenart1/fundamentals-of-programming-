import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.21.py: Program zapisujący słownik opisujący ulubiony film lub książkę do pliku favourite.json.
import json  # Importujemy moduł json.

favourite_movie = {  # Słownik z co najmniej 5 parami klucz-wartość.
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": "Sci-Fi",
    "rating": 8.8,
}  # Koniec słownika.

with open("favourite.json", "w", encoding="utf-8") as file:  # Otwieramy favourite.json do zapisu.
    json.dump(favourite_movie, file, indent=4, ensure_ascii=False)  # Zapisujemy słownik do pliku JSON.

print("Saved data to favourite.json")  # Potwierdzamy zapis.
