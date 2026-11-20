### PLIK 1.5.py: Program przechowujący 5 państw w liście słowników i wypisujący je w tabeli.
countries = [  # Lista słowników z nazwą państwa i liczbą mieszkańców.
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 68000000},
    {"name": "Spain", "population": 48000000},
    {"name": "Italy", "population": 59000000},
]  # Koniec listy państw.

print(f"{'COUNTRY':<10} {'POPULATION'}")  # Wypisujemy nagłówki kolumn.
for country in countries:  # Przechodzimy przez każdy słownik w liście.
    print(f"{country['name']:<10} {country['population']}")  # Wypisujemy nazwę i populację.
