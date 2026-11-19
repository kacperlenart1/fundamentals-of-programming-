### PLIK draw_all_figures.py: Program rysujący kwadrat, trójkąt i prostokąt dwukrotnie w różnych lokalizacjach na ekranie.
import turtle  # Importujemy moduł graficzny turtle.
from figures import draw_square, draw_triangle, draw_rectangle  # Importujemy funkcje rysujące figury z modułu figures.

window = turtle.Screen()  # Tworzymy okno programu graficznego.
window.bgcolor("lightgreen")  # Ustawiamy jasnozielony kolor tła okna.

pen = turtle.Turtle()  # Tworzymy obiekt żółwia, którym będziemy rysować.
pen.speed(5)  # Ustawiamy umiarkowaną prędkość rysowania.

pen.penup()  # Podnosimy pisak, aby przejść w nowe miejsce bez rysowania śladu.
pen.goto(-250, 150)  # Przenosimy żółwia na współrzędne (-250, 150).
pen.pendown()  # Opuszczamy pisak, aby rozpocząć rysowanie.
draw_square(pen, 80)  # Rysujemy pierwszy kwadrat o boku 80.

pen.penup()  # Podnosimy pisak przed przejściem do kolejnej pozycji.
pen.goto(-250, -50)  # Przenosimy żółwia niżej na współrzędne (-250, -50).
pen.pendown()  # Opuszczamy pisak.
draw_square(pen, 60)  # Rysujemy drugi kwadrat o boku 60.

pen.penup()  # Podnosimy pisak przed narysowaniem pierwszego trójkąta.
pen.goto(-50, 150)  # Ustawiamy pozycję startową dla trójkąta.
pen.pendown()  # Opuszczamy pisak.
draw_triangle(pen, 90)  # Rysujemy pierwszy trójkąt o boku 90.

pen.penup()  # Podnosimy pisak przed narysowaniem drugiego trójkąta.
pen.goto(-50, -50)  # Przenosimy żółwia na współrzędne (-50, -50).
pen.pendown()  # Opuszczamy pisak.
draw_triangle(pen, 70)  # Rysujemy drugi trójkąt o boku 70.

pen.penup()  # Podnosimy pisak przed narysowaniem pierwszego prostokąta.
pen.goto(150, 150)  # Ustawiamy pozycję po prawej stronie ekranu.
pen.pendown()  # Opuszczamy pisak.
draw_rectangle(pen, 110, 60)  # Rysujemy pierwszy prostokąt o bokach 110 i 60.

pen.penup()  # Podnosimy pisak przed narysowaniem drugiego prostokąta.
pen.goto(150, -50)  # Przenosimy żółwia poniżej pierwszego prostokąta.
pen.pendown()  # Opuszczamy pisak.
draw_rectangle(pen, 90, 50)  # Rysujemy drugi prostokąt o bokach 90 i 50.

pen.hideturtle()  # Ukrywamy strzałkę żółwia po zakończeniu rysowania.
window.mainloop()  # Utrzymujemy okno otwarte dopóki użytkownik go nie zamknie.
