###
# Program sprawdza, czy przynajmniej jedna z dwóch wprowadzonych liczb nie jest ujemna.
#

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

# Sprawdzenie za pomocą 'not' oraz 'or', czy chociaż jedna liczba nie jest ujemna
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print(f'Both numbers {x} and {y} are negative')