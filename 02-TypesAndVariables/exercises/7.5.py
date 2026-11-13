###
# Program sprawdzający, czy numer rejestracyjny pojazdu pochodzi z Krakowa
# (numery z Krakowa zaczynają się od liter "KR" lub "KK").
#

car_number = input('Enter car registration number: ')

# Sprawdzenie, czy pierwsze dwa znaki to "KR" lub "KK"
is_krakow = car_number[0:2] == 'KR' or car_number[0:2] == 'KK'

# Wyświetlenie wyniku (True / False)
print(f'Car is from Krakow: {is_krakow}')