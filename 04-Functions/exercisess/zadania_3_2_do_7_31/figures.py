### PLIK figures.py: Moduł zawierający funkcje rysujące kwadrat, trójkąt oraz prostokąt za pomocą modułu turtle.
def draw_square(pen, length):  # Rysuje kwadrat o boku długości length.
    for _ in range(4):  # Kwadrat ma 4 równe boki.
        pen.forward(length)  # Przesuwamy żółwia do przodu o długość boku.
        pen.right(90)  # Skręcamy w prawo o 90 stopni.


def draw_triangle(pen, length):  # Rysuje trójkąt o równych bokach długości length.
    for _ in range(3):  # Trójkąt ma 3 boki.
        pen.forward(length)  # Przesuwamy żółwia do przodu o długość boku.
        pen.left(120)  # Skręcamy w lewo o 120 stopni.


def draw_rectangle(pen, length_a, length_b):  # Rysuje prostokąt o bokach length_a oraz length_b.
    for _ in range(2):  # Powtarzamy parę dwóch boków dwa razy.
        pen.forward(length_a)  # Rysujemy pierwszy bok prostokąta.
        pen.right(90)  # Skręcamy o kąt prosty 90 stopni.
        pen.forward(length_b)  # Rysujemy drugi bok prostokąta.
        pen.right(90)  # Skręcamy ponownie o 90 stopni.
