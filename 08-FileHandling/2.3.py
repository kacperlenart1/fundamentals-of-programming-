import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 2.3.py: Program kopiujący całą zawartość pliku healthy_lifestyle.txt do copy_healthy_lifestyle.txt.
original_file = 'healthy_lifestyle.txt'  # Nazwa pliku źródłowego.
target_file = 'copy_healthy_lifestyle.txt'  # Nazwa pliku docelowego (kopii).

with open(original_file, 'r', encoding='utf-8') as source:  # Otwieramy plik źródłowy do odczytu.
    content = source.read()  # Wczytujemy całą zawartość pliku źródłowego.

with open(target_file, 'w', encoding='utf-8') as target:  # Otwieramy plik docelowy do zapisu.
    target.write(content)  # Zapisujemy wczytaną zawartość do nowego pliku.
