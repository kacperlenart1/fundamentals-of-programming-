import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

### PLIK 4.12.py: Program dzielący książki z books.csv na osobne pliki według gatunku z podziałem na funkcje.
import csv  # Importujemy moduł csv.

GENRE_TO_FILE = {  # Słownik przypisujący nazwę gatunku do nazwy pliku wyjściowego.
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt",
}  # Koniec słownika.


def load_books(file_path):  # Wczytuje wszystkie rekordy książek z pliku CSV.
    with open(file_path, "r", encoding="utf-8", newline="") as file:  # Otwieramy plik books.csv.
        return list(csv.DictReader(file))  # Zwracamy listę słowników z danymi książek.


def get_books_by_genre(books, genre):  # Zwraca podlistę książek należących do wskazanego gatunku.
    return [book for book in books if book.get("Genre", "").strip() == genre]  # Filtrujemy po kolumnie Genre.


def write_books_file(books, output_path):  # Zapisuje wybrane książki do docelowego pliku tekstowego.
    with open(output_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for book in books:
            writer.writerow(str(value).strip() for value in book.values())

def main():  # Główna funkcja programu koordynująca wczytanie, filtrowanie i zapis.
    books = load_books("books.csv")  # Wczytujemy książki z books.csv.
    for genre, filename in GENRE_TO_FILE.items():  # Przechodzimy przez wszystkie zdefiniowane gatunki.
        filtered = get_books_by_genre(books, genre)  # Pobieramy książki danego gatunku.
        write_books_file(filtered, filename)  # Zapisujemy je do odpowiedniego pliku.


if __name__ == "__main__":  # Uruchamiamy main() tylko przy bezpośrednim uruchomieniu skryptu.
    main()  # Wywołujemy funkcję główną.
