import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###
# Próbujemy odczytać nieistniejący plik.
# Obsługujemy błąd za pomocą bloku try-except.
#

# Na dysku nie ma pliku o tej nazwie.
file_name = 'xyz.txt'

try:
    with open(file_name) as file:
        content = file.read()
except FileNotFoundError:
    print(f"Hey! The file {file_name} does not exist.")
