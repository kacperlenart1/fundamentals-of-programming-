import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 5.18.py: Program wypisujący informacje o psach młodszych niż 5 lat z pliku dogs.json.
import json  # Importujemy moduł json.

with open("dogs.json", "r", encoding="utf-8") as file:  # Otwieramy dogs.json do odczytu.
    dogs = json.load(file)  # Wczytujemy listę psów.

for dog in dogs:  # Przechodzimy przez każdy rekord psa.
    if dog.get("age", 0) < 5:  # Sprawdzamy warunek wieku poniżej 5 lat.
        print(dog)  # Wypisujemy dane psa spełniającego warunek.
