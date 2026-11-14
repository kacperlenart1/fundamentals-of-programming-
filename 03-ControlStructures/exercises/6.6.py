###
# Program obliczający opłatę za parkowanie na podstawie liczby spędzonych godzin.
#

hours = int(input('Enter the number of hours of parking: '))

# Ustalenie opłaty w zależności od liczby godzin parkowania zgodnie z taryfą
if hours <= 2:
    fee = 5
elif hours <= 6:
    fee = 15
else:
    fee = 20

# Wyświetlenie obliczonej opłaty za parkowanie
print(f'Parking fee: {fee} PLN')