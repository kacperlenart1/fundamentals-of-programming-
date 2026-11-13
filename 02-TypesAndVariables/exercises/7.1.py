###
# Program sprawdzający, czy osoba kwalifikuje się do zwolnienia z podatku
# (dla osób do 26 roku życia włącznie).
#

# Pobranie wieku od użytkownika i konwersja na liczbe całkowita
age = int(input('Enter age: '))

# Sprawdzenie warunku (czy wiek jest <= 26)
no_tax = age <= 26

# Wyświetlenie wyniku (True / False)
print(f'Exemption from paying taxes: {no_tax}')