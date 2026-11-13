###
# Program obliczający podatek VAT od wpisanej kwoty
#

# Pobranie kwoty od użytkownika i konwersja na liczbę zmienneczkową (float)
amount = float(input('Enter amount: '))

# Obliczenie 23% podatku VAT
vat = amount * 0.23

# Wyświetlenie wyników z formatowaniem do 2 miejsc po przecinku
print(f'Amount  : {amount:.2f}')
print(f'VAT 23% : {vat:.2f}')