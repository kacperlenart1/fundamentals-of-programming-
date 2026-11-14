###
# Prosta gra polegająca na odgadywaniu wylosowanej liczby z zakresu od 1 do 100 przy użyciu pętli while.
#

import random

# Losowanie liczby do odgadnięcia z zakresu od 1 do 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

# Pętla działa dopóki użytkownik nie odgadnie poprawnej liczby
while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")