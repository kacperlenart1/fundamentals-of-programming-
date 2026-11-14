###
# Program sprawdzający, czy wprowadzona liczba jest dodatnia, ujemna czy równa zero.
#

# Pobranie liczby od użytkownika i konwersja na liczbę całkowitą
number = int(input('Enter number: '))

# Sprawdzenie wartości liczby za pomocą instrukcji warunkowych
if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')