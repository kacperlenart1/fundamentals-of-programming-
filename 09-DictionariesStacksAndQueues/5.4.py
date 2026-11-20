### PLIK 5.4.py: Program obliczający łączną liczbę godzin przedmiotów w semestrze zimowym.
winter_semester = {  # Słownik przedmiot -> liczba godzin.
    "math": 60,
    "programming": 30,
    "history": 15,
}  # Koniec słownika.

total_hours = sum(winter_semester.values())  # Sumujemy liczby godzin ze wszystkich przedmiotów.
print(f"The total number of hours in the winter semester is {total_hours}")  # Wypisujemy wynik.
