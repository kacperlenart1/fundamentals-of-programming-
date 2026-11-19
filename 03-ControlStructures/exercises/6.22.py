###
# Program wypisujący liczby od 1 do 30 z zastąpieniem wielokrotności odpowiednimi słowami THREE, FIVE lub BINGO.
#

for i in range(1, 31):
    # Sprawdzenie podzielności jednocześnie przez 3 i 5 (musi być pierwsze)
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')
    # Sprawdzenie podzielności przez 3
    elif i % 3 == 0:
        print('THREE', end=' ')
    # Sprawdzenie podzielności przez 5
    elif i % 5 == 0:
        print('FIVE', end=' ')
    # W pozostałych przypadkach wypisanie samej liczby
    else:
        print(i, end=' ')

print()