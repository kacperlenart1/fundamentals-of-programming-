###
# Program przeprowadzający ankietę składającą się z trzech pytań i wyświetlający jej wyniki w czytelnej formie.
#

# Zadanie pytań ankietowych i zapisanie odpowiedzi jako wartości logiczne typu bool
computer_science = input("SURVEY Are you interested in computer science? (y/n): ") == 'y'
computer_games = input("Do you like playing computer games? (y/n): ") == 'y'
instagram = input("Do you have an Instagram account? (y/n): ") == 'y'

# Przygotowanie tekstowych odpowiedzi na podstawie wartości logicznych
cs_result = 'Yes' if computer_science else 'No'
games_result = 'Yes' if computer_games else 'No'
insta_result = 'Yes' if instagram else 'No'

# Wyświetlenie nagłówka oraz ostatecznych wyników ankiety
print("\nSURVEY RESULTS")
print(f"Interested in computer science: {cs_result}")
print(f"Playing computer games: {games_result}")
print(f"Has an Instagram account: {insta_result}")