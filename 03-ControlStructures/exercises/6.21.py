###
# Program wydający podaną kwotę w monetach o nominale 5, 2 i 1 PLN przy użyciu jak najmniejszej liczby monet.
#

amount = int(input("Enter the amount in PLN: "))
original_amount = amount

# Obliczenie liczby monet o nominale 5 PLN oraz aktualizacja pozostałej kwoty
coins_5 = amount // 5
amount %= 5

# Obliczenie liczby monet o nominale 2 PLN oraz aktualizacja pozostałej kwoty
coins_2 = amount // 2
amount %= 2

# Pozostała kwota to bezpośrednio liczba monet o nominale 1 PLN
coins_1 = amount

# Wyświetlenie podsumowania podziału kwoty na poszczególne nominały
print(f"The amount of PLN {original_amount} in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")