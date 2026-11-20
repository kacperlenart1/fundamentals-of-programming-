### PLIK 5.14.py: Program obsługujący kolejkę klientów z automatyczną numeracją biletów (FIFO).
import queue  # Importujemy moduł queue.

customer_queue = queue.Queue()  # Kolejka oczekujących klientów.
next_ticket = 1  # Licznik kolejnych numerów biletów.

while True:  # Pętla obsługi stanowiska.
    print("1. New customer (take ticket)")  # Dodanie nowego klienta na koniec kolejki.
    print("2. Serve next customer")  # Obsłużenie klienta z początku kolejki.
    print("0. Quit")  # Zakończenie pracy programu.
    choice = input("Select an option: ")  # Wczytujemy wybór.

    if choice == "1":  # Nowy klient pobiera bilet.
        ticket = next_ticket  # Przypisujemy bieżący numer biletu.
        next_ticket += 1  # Zwiększamy licznik na kolejny bilet.
        customer_queue.put(ticket)  # Dodajemy bilet na koniec kolejki.
        print(f"Customer assigned ticket #{ticket}.")  # Informujemy o wydaniu biletu.
    elif choice == "2":  # Obsługa następnego klienta.
        if not customer_queue.empty():  # Sprawdzamy, czy ktoś czeka w kolejce.
            served_ticket = customer_queue.get()  # Pobieramy klienta z początku kolejki.
            print(f"Serving customer with ticket #{served_ticket}.")  # Wypisujemy numer obsługiwanego klienta.
        else:  # Gdy nikt nie czeka.
            print("No customers waiting in the queue.")  # Informujemy o pustej kolejce.
    elif choice == "0":  # Wyjście z programu.
        break  # Kończymy pętlę.
    else:  # Nieprawidłowa opcja.
        print("Invalid option.")  # Komunikat o błędzie wyboru.
    print()  # Pusta linia.
