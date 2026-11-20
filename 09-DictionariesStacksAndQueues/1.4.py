### PLIK 1.4.py: Program wykonujący operacje odczytu, modyfikacji i dodawania elementów w słowniku person.
person = {  # Słownik z różnymi typami wartości: str, int, list, bool, dict.
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"},
}  # Koniec słownika.

print("Name:", person["name"])  # 1. Wypisujemy imię.
print("Hobby:", person["hobby"])  # 2. Wypisujemy listę zainteresowań.
print("Full dictionary:", person)  # 3. Wypisujemy cały słownik.

person["surname"] = "Nowak"  # 4. Zmieniamy nazwisko na Nowak.
person["married"] = not person["married"]  # 5. Zmieniamy stan cywilny na przeciwny.
person["gender"] = "male"  # 6. Dodajemy nowy klucz gender.
person["hobby"].append("bicycle")  # 7. Dopisujemy nowe hobby do listy.
person["phone"]["work"] = "313131444"  # 8. Dodajemy telefon służbowy do zagnieżdżonego słownika phone.

print("\nUpdated dictionary items:")  # Nagłówek przed wypisaniem zaktualizowanego słownika.
for key, value in person.items():  # 9. Iterujemy po wszystkich parach klucz-wartość.
    print(f"{key}: {value}")  # Wypisujemy klucz i wartość.
