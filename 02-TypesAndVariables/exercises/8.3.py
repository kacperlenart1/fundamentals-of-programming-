###
# Program konwertujący temperaturę z stopni Celsjusza na Kelwiny i Fahrenheity.
#
# 1. Odczytaj temperaturę w stopniach Celsjusza z klawiatury.
# 2. Oblicz temperaturę w Kelwinach (dodaj 273.15).
# 3. Obliczenie temperatury w Fahrenheitach (pomnoż przez 1.8 i dodaj 32).
# 4. Wyświetl wyniki obliczeń.
#

# Krok 1: Pobranie temperatury od użytkownika (konwersja na float dla ułamków)
celsius = float(input('Enter temperature in Celsius: '))

# Krok 2: Przeliczenie na Kelwiny
kelvin = celsius + 273.15

# Krok 3: Przeliczenie na Fahrenheity
fahrenheit = (celsius * 1.8) + 32

# Krok 4: Wyświetlenie wyników
print(f'Temperature in Kelvin: {kelvin}')
print(f'Temperature in Fahrenheit: {fahrenheit}')