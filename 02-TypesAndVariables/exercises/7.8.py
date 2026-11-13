###
# Program symulujący rzut trzema kostkami do gry

import random

# Rzut trzema kostkami (każda losuje liczbę od 1 do 6)
dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

# Obliczenie sumy wszystkich rzutów
total = dice_roll_1 + dice_roll_2 + dice_roll_3

# Wyświetlenie wyników poszczególnych rzutów oraz sumy
print(f'Dice roll 1: {dice_roll_1}')
print(f'Dice roll 2: {dice_roll_2}')
print(f'Dice roll 3: {dice_roll_3}')
print(f'Total sum of dice rolled: {total}')