import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.8.py: Program wypisujący nazwy plików z files.txt, których rozszerzenie ma dokładnie 4 znaki.
with open("files.txt", "r", encoding="utf-8") as file:  # Otwieramy plik files.txt do odczytu.
    for line in file:  # Przechodzimy przez każdą linię w pliku.
        filename = line.strip()  # Usuwamy białe znaki z początku i końca nazwy pliku.
        if "." in filename:  # Sprawdzamy, czy w nazwie pliku jest kropka.
            extension = filename.rsplit(".", 1)[1]  # Pobieramy część po ostatniej kropce (np. "html").
            if len(extension) == 4:  # Sprawdzamy, czy rozszerzenie składa się z dokładnie 4 znaków.
                print(filename)  # Wypisujemy nazwę pliku spełniającego warunek.
