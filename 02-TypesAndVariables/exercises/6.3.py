###
# A program that prints a university abbreviation
#

university = "Krakow University of Economics"

# Pobranie pierwszych liter każdego słowa za pomocą indeksów i ich połączenie
abbreviation = university[0] + university[7] + university[21]

# Wyświetlenie skrótu
print(f"{university[0]}{university[7]}{university[21]}")