### PLIK 4.3.py: Program obliczający pole trójkąta na podstawie długości jego boków ze wzoru Herona.
import math  # Importujemy moduł math, aby skorzystać z funkcji pierwiastka math.sqrt.


def triangle_area(a, b, c):  # Definiujemy funkcję przyjmującą trzy boki trójkąta: a, b oraz c.
    s = (a + b + c) / 2  # Obliczamy połowę obwodu trójkąta potrzebną we wzorze Herona.
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Wyliczamy pole trójkąta i zapisujemy je w zmiennej area.
    return area  # Zwracamy obliczone pole w miejsce wywołania funkcji.


a = float(input("Enter side a: "))  # Wczytujemy długość boku a i zamieniamy tekst na liczbę zmiennoprzecinkową.
b = float(input("Enter side b: "))  # Wczytujemy długość boku b i zamieniamy tekst na liczbę zmiennoprzecinkową.
c = float(input("Enter side c: "))  # Wczytujemy długość boku c i zamieniamy tekst na liczbę zmiennoprzecinkową.
print(f"The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c)}")  # Wypisujemy wynik z użyciem f-stringa.

print("The area of a triangle with sides 3, 4, 5 is", triangle_area(3, 4, 5))  # Testujemy funkcję dla boków 3, 4, 5.
print("The area of a triangle with sides 5, 12, 13 is", triangle_area(5, 12, 13))  # Testujemy funkcję dla boków 5, 12, 13.
print("The area of a triangle with sides 7, 24, 25 is", triangle_area(7, 24, 25))  # Testujemy funkcję dla boków 7, 24, 25.
