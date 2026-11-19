### PLIK 7.5.py: Program testujący przynależność liczby do przedziału domkniętego.
from range_checker import in_range  # Importujemy funkcję sprawdzającą przedział.

number = 7  # Testowana liczba.
x = 2  # Dolna granica przedziału.
y = 15  # Górna granica przedziału.
answer = "yes" if in_range(number, x, y) else "no"  # Zamieniamy wartość logiczną na napis yes lub no.
print(f"A number: {number}")  # Wypisujemy testowaną liczbę.
print(f"Number {number} in the range <{x},{y}>: {answer}")  # Wypisujemy wynik sprawdzenia przedziału.
