### PLIK 4.2.py: Program zarządzający kolejką plików do drukowania (FIFO).
import queue  # Importujemy moduł queue.

files_to_print = queue.Queue()  # Tworzymy kolejkę FIFO dla plików do wydruku.

while True:  # Pętla menu programu.
    print("1. Add file to print")  # Opcja dodania pliku do kolejki.
    print("2. Print file")  # Opcja pobrania pierwszego pliku z kolejki do druku.
    print("0. Quit")  # Opcja wyjścia z programu.
    menu = input("Select an option: ")  # Wczytujemy wybór użytkownika.

    if menu == "1":  # Dodawanie pliku na koniec kolejki.
        file_name = input("Enter file name to print: ")  # Pobieramy nazwę pliku.
        files_to_print.put(file_name)  # Wrzucamy plik na koniec kolejki.
        print(f"File '{file_name}' added to the print queue.")  # Potwierdzamy dodanie.
    elif menu == "2":  # Drukowanie najstarszego pliku w kolejce.
        if not files_to_print.empty():  # Sprawdzamy, czy kolejka nie jest pusta.
            file_to_print = files_to_print.get()  # Pobieramy pierwszy plik z początku kolejki.
            print(f"File {file_to_print} is currently being printed. Please wait!")  # Komunikat o drukowaniu.
        else:  # Gdy kolejka jest pusta.
            print("Print queue is empty. No files to print.")  # Informujemy o braku plików.
    elif menu == "0":  # Zakończenie programu.
        break  # Przerywamy pętlę while.
    else:  # Niepoprawny numer opcji.
        print("Invalid option. Try again.")  # Komunikat o złym wyborze.
    print()  # Pusta linia oddzielająca tury menu.
