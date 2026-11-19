### PLIK 3.2.py: Program losujący liczbę całkowitą z przedziału od 1 do 6 jak przy rzucie kostką.
import random  # Dołączamy wbudowany moduł random, który pozwala losować liczby.

dice_roll = random.randint(1, 6)  # Losujemy jedną liczbę całkowitą od 1 do 6 włącznie.
print("Dice roll:", dice_roll)  # Wyświetlamy wylosowany wynik w terminalu.
