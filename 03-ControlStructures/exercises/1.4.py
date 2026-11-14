###
# Program symulujący terminal płatniczy.

account_balance = 500

# Pobranie kwoty płatności od użytkownika i konwersja na liczbę całkowitą
total_payment = int(input('Enter total payment amount: '))

# Sprawdzenie, czy kwota zakupu mieści się w dostępnych środkach na koncie
if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')