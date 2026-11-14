###
# Program sprawdzający, czy liczba wprowadzona z klawiatury jest parzysta czy nieparzysta
# even parzysta, odd nieparzysta

# Pobranie liczby od użytkownika i konwersja na liczbę całkowitą
number = int(input('Enter number: '))

# Sprawdzenie, czy reszta z dzielenia liczby przez 2 wynosi 0
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')