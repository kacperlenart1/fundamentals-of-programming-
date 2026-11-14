###
# Program obliczający i wyświetlający kwartał roku dla podanego numeru miesiąca (1..12).
#

month = int(input('Enter month number (1..12): '))

# Określenie kwartału za pomocą łańcucha instrukcji warunkowych
if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

# Wyświetlenie wyniku
print(f'Month {month} is in quarter {quarter}')