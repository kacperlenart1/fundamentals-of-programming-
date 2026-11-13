###
# Program demonstrujący operacje na łańcuchach znaków (stringach)
#

movie = "The Lord of the Rings: The Return of the King"

# 1. Wyświetlenie liczby znaków w tytule
print('Number of characters: ', len(movie))

# 2. Wyświetlenie tytułu wielkimi literami
print('Title in capital letters: ', movie.upper())

# 3. Wyświetlenie tytułu małymi literami
print('Title in small letters: ', movie.lower())

# 4. Sprawdzenie, ile razy litera "e" pojawia się w tytule
print('Number of "e" characters: ', movie.count('e'))

# 5. Sprawdzenie, na której pozycji w tekście znajduje się słowo "Lord"
print('Position of "Lord": ', movie.find('Lord'))

# 6. Sprawdzenie, gdzie znajduje się słowo "dragon" (gdy go nie ma, zwróci -1)
print('Position of "dragon": ', movie.find('dragon'))