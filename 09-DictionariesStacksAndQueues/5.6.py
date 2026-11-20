### PLIK 5.6.py: Program łączący dwa słowniki w jeden słownik person (5 par klucz-wartość).
basic_data = {  # Podstawowe dane.
    "name": "Barbara",
    "age": 21,
}  # Koniec basic_data.

advanced_data = {  # Dodatkowe dane.
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"],
}  # Koniec advanced_data.

person = {}  # Tworzymy nowy słownik person.
person.update(basic_data)  # Kopiujemy pary z basic_data.
person.update(advanced_data)  # Kopiujemy pary z advanced_data.

print(person)  # Wypisujemy połączony słownik person.
