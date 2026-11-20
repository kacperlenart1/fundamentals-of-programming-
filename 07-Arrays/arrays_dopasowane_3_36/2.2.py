### PLIK 2.2.py: Kompletny program wypisujący planszę gry kółko i krzyżyk 3x3 w wierszach i kolumnach.
tic_tac_toe_board = [  # Tablica dwuwymiarowa 3x3 reprezentująca planszę.
    ['X', 'O', 'X'],  # Pierwszy wiersz.
    [' ', 'X', 'O'],  # Drugi wiersz.
    ['O', ' ', 'X']   # Trzeci wiersz.
]  # Koniec planszy.

for row in tic_tac_toe_board:  # Przechodzimy przez każdy wiersz planszy.
    for item in row:  # Przechodzimy przez każde pole w wierszu.
        print(item, end=" ")  # Wypisujemy zawartość pola i spację.
    print()  # Przechodzimy do nowej linii po wypisaniu wiersza.
