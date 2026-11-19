### PLIK employee5.3.py: Program wczytujący dane pracownika z modułu keyboard i wyświetlający je z opcją ukrycia pensji.
from keyboard import input_string, input_integer, input_real, input_boolean  # Importujemy funkcje wczytujące z modułu keyboard.

first_name = input_string("Enter name: ")  # Pobieramy imię pracownika jako tekst.
last_name = input_string("Enter surname: ")  # Pobieramy nazwisko pracownika jako tekst.
age = input_integer("Enter age: ")  # Pobieramy wiek pracownika jako liczbę całkowitą.
salary = input_real("Enter salary: ")  # Pobieramy wynagrodzenie jako liczbę zmiennoprzecinkową.
is_salary_hidden = input_boolean("Hide salary? (y/n) ")  # Pytamy czy ukryć pensję i zapisujemy wynik bool.

print("DATA RECORD")  # Wypisujemy nagłówek rekordu.
print("===========")  # Wypisujemy linię oddzielającą.
print("Name:", first_name)  # Wypisujemy imię.
print("Surname:", last_name)  # Wypisujemy nazwisko.
print("Age:", age)  # Wypisujemy wiek.
if not is_salary_hidden:  # Wyświetlamy pensję tylko wtedy, gdy nie została ukryta.
    print(f"Salary: {salary}")  # Wypisujemy kwotę wynagrodzenia.
