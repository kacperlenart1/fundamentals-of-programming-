###
# Prosty kalkulator wykonujący operacje +, -, *, / na podanych liczbach. Użytkownik wprowadza dwie liczby oraz symbol operacji, 
# a program wyświetla wynik obliczeń.
#

# Pobranie liczb oraz symbolu operacji od użytkownika
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter mathematical operation (+, -, *, /): ')

# Sprawdzenie, który operator został wybrany i wykonanie obliczenia
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = 'Error (division by zero)'
else:
    result = 'Invalid operator'

# Wyświetlenie wyniku obliczeń
print(f'{number1} {operator} {number2} = {result}')