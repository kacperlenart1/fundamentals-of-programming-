###
# Program sprawdzający, czy prędkość pojazdu na autostradzie
#

# Pobranie prędkości od użytkownika i konwersja na liczbę całkowitą
speed = int(input('Enter vehicle speed: '))

# Sprawdzenie, czy prędkość jest w przedziale od 40 do 140 włącznie
speed_is_valid = 40 <= speed <= 140

# Wyświetlenie wyniku (True / False)
print(f'Speed is valid: {speed_is_valid}')