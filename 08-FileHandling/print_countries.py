import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###
# Odczytujemy plik linia po linii.
#
with open('countries.txt', 'r') as file:
    counter = 1
    for line in file:
        print(f"{counter}. {line}", end="")
        counter += 1
