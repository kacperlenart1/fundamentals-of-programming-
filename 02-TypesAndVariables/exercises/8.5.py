###
# Program odczytujący kod SWIFT z klawiatury
# i wyświetlający kod banku oraz kod kraju.
#

swift = input('Enter SWIFT code: ')

# Pobranie kodu banku (pierwsze 4 znaki, od indeksu 0 do 3)
print(f'Bank Code: {swift[:4]}')

# Pobranie kodu kraju (znaki na indeksach 4 i 5)
print(f'Country Code: {swift[4:6]}')