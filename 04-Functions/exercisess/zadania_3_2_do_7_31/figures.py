### PLIK figures.py: Moduł zawierający funkcje rysujące figury za pomocą modułu turtle.
import turtle  # Korzystamy z domyślnego żółwia modułu turtle.


def draw_square(length):  # Rysuje kwadrat o boku długości length.
    for _ in range(4):  # Kwadrat ma 4 równe boki.
        turtle.forward(length)  # Przesuwamy żółwia do przodu o długość boku.
        turtle.right(90)  # Skręcamy w prawo o 90 stopni.


def draw_triangle(length):  # Rysuje trójkąt równoboczny, a więc także równoramienny.
    for _ in range(3):  # Trójkąt ma 3 boki.
        turtle.forward(length)  # Przesuwamy żółwia do przodu o długość boku.
        turtle.left(120)  # Skręcamy w lewo o 120 stopni.


def draw_rectangle(length_a, length_b):  # Rysuje prostokąt o bokach length_a oraz length_b.
    for _ in range(2):  # Powtarzamy parę dwóch boków dwa razy.
        turtle.forward(length_a)  # Rysujemy pierwszy bok prostokąta.
        turtle.right(90)  # Skręcamy o kąt prosty 90 stopni.
        turtle.forward(length_b)  # Rysujemy drugi bok prostokąta.
        turtle.right(90)  # Skręcamy ponownie o 90 stopni.
