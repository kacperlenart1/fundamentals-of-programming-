import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###
# Próbujemy odczytać nieistniejący plik.
#

# Na dysku nie ma pliku o tej nazwie.
file_name = 'xyz.txt'

with open(file_name) as file:
    content = file.read()
