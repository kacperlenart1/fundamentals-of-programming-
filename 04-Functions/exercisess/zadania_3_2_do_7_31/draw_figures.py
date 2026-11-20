### PLIK draw_figures.py: Program konfigurujący okno żółwia i rysujący kwadrat przy pomocy funkcji z modułu figures.
import turtle  # Importujemy moduł graficzny turtle.
from figures import draw_square  # Importujemy funkcję draw_square z modułu figures.

window = turtle.Screen()  # Tworzymy okno programu graficznego.
window.bgcolor("lightgreen")  # Ustawiamy jasnozielony kolor tła okna.

turtle.speed(5)  # Ustawiamy umiarkowaną prędkość domyślnego żółwia.

side_length = 100  # Ustawiamy długość boku kwadratu na 100.
draw_square(side_length)  # Wywołujemy funkcję rysującą kwadrat.

turtle.hideturtle()  # Ukrywamy strzałkę żółwia po zakończeniu rysowania.
window.mainloop()  # Utrzymujemy okno otwarte dopóki użytkownik go nie zamknie.
