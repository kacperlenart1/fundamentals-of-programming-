### PLIK 7.3.py: Program pobierający numer miesiąca i wypisujący jego nazwę z modułu months.
from months import month  # Importujemy funkcję month z pliku months.py.

n = int(input("Enter month number: "))  # Wczytujemy numer miesiąca jako liczbę całkowitą.
print(f"The name of month {n} is {month(n)}")  # Wypisujemy wynik z użyciem f-stringa.
