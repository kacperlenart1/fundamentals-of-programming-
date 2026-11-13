###
# Program symulujący rzut kostką i sprawdzający, czy wylosowano liczbę 1 lub 6.
#

import random

# Rzut kostką (losowanie liczby od 1 do 6)
dice_rolled = random.randint(1, 6)

# Sprawdzenie warunku: czy wylosowano 1 lub 6
is_special = dice_rolled == 1 or dice_rolled == 6

# Wyświetlenie wyników zgodnie z przykładem
print(f'Dice rolled: {dice_rolled}')
print(f'Special number (1 or 6): {is_special}')