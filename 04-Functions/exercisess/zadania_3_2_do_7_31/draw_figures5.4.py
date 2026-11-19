### PLIK draw_figures.py: Program konfigurujący okno żółwia i rysujący kwadrat przy pomocy funkcji z modułu figures.
import turtle  # Importujemy moduł graficzny turtle.
from figures import draw_square  # Importujemy funkcję draw_square z modułu figures.

window = turtle.Screen()  # Tworzymy okno programu graficznego.
window.bgcolor("lightgreen")  # Ustawiamy jasnozielony kolor tła okna.

pen = turtle.Turtle()  # Tworzymy obiekt żółwia, którym będziemy rysować.
pen.speed(5)  # Ustawiamy umiarkowaną prędkość rysowania.

side_length = 100  # Ustawiamy długość boku kwadratu na 100.
draw_square(pen, side_length)  # Wywołujemy funkcję rysującą kwadrat.

pen.hideturtle()  # Ukrywamy strzałkę żółwia po zakończeniu rysowania.
window.mainloop()  # Utrzymujemy okno otwarte dopóki użytkownik go nie zamknie.
