###
# Program wypisujący nazwę uniwersytetu z dodatkową spacją pomiędzy każdym znakiem.
#

university = 'Krakow University of Economics'
university_expanded = ''

# Iteracja po każdym znaku w napisie i dodawanie spacji
for char in university:
    university_expanded = university_expanded + char + ' '

# Wyświetlenie nazwy oryginalnej oraz rozszerzonej
print(university)
print(university_expanded)