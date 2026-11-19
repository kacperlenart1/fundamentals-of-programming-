###
# Program sprawdza, czy wpisane imię kończy się na literę 'a' i wypisuje odpowiedni komunikat.
#

name = input('Enter name: ')

# Sprawdzenie, czy ostatnia litera imienia to 'a' lub 'A'
if name.endswith('a') or name.endswith('A'):
    print(f'{name} -- Polish female name')