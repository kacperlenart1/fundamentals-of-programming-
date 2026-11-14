###
# Program obliczający i wyświetlający liczbę dni w danym miesiącu przy założeniu, że luty ma zawsze 28 dni.
#

month = int(input('Enter month number (1..12): '))

# Sprawdzenie czy miesiąc ma 31 dni
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
# Sprawdzenie czy miesiąc ma 30 dni
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 28  # luty ma zawsze 28 dni

# Wyświetlenie ostatecznego wyniku
print(f'Month {month} has {days} days')