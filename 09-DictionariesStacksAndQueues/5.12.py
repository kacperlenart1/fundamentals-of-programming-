### PLIK 5.12.py: Program odwracający podany tekst z użyciem stosu LIFO.
import queue  # Importujemy moduł queue.


def reverse_text(text):  # Zwraca odwrócony napis z wykorzystaniem stosu.
    stack = queue.LifoQueue()  # Tworzymy stos znaków.
    for char in text:  # Odkładamy każdy znak napisu na stos.
        stack.put(char)  # Wrzucamy znak na wierzch stosu.

    reversed_chars = []  # Lista na znaki zdejmowane ze stosu.
    while not stack.empty():  # Zdejmujemy znaki od końca.
        reversed_chars.append(stack.get())  # Dodajemy znak do listy wynikowej.

    return "".join(reversed_chars)  # Łączymy znaki w odwrócony napis.


user_text = input("Enter text to reverse: ")  # Wczytujemy tekst od użytkownika.
print("Reversed text:", reverse_text(user_text))  # Wypisujemy odwrócony napis.
