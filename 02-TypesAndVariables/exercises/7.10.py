###
# Gra w zgadywanie rzutu kością: komputer rzuca, gracz zgaduje.

import random

# TURA KOMPUTERA: losowanie liczby od 1 do 6
computer = random.randint(1, 6)

# TURA GRACZA: wprowadzenie liczby z klawiatury i konwersja na liczbę całkowitą (int)
you = int(input('Enter your guess (1-6): '))

# Sprawdzenie, czy gracz odgadł wylosowaną przez komputer liczbę
you_won = computer == you

# Wyświetlenie wyniku (True / False)
print(f'You won: {you_won}')