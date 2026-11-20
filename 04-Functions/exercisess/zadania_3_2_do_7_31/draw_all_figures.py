### PLIK draw_all_figures.py: Program rysujący kwadrat, trójkąt i prostokąt dwukrotnie w różnych lokalizacjach na ekranie.
import turtle  # Importujemy moduł graficzny turtle.
from figures import draw_square, draw_triangle, draw_rectangle  # Importujemy funkcje rysujące figury z modułu figures.

window = turtle.Screen()  # Tworzymy okno programu graficznego.
window.bgcolor("lightgreen")  # Ustawiamy jasnozielony kolor tła okna.

turtle.speed(5)  # Ustawiamy umiarkowaną prędkość domyślnego żółwia.

turtle.penup()  # Podnosimy pisak, aby przejść w nowe miejsce bez rysowania śladu.
turtle.goto(-250, 150)  # Przenosimy żółwia na współrzędne (-250, 150).
turtle.pendown()  # Opuszczamy pisak, aby rozpocząć rysowanie.
draw_square(80)  # Rysujemy pierwszy kwadrat o boku 80.

turtle.penup()  # Podnosimy pisak przed przejściem do kolejnej pozycji.
turtle.goto(-250, -50)  # Przenosimy żółwia niżej na współrzędne (-250, -50).
turtle.pendown()  # Opuszczamy pisak.
draw_square(60)  # Rysujemy drugi kwadrat o boku 60.

turtle.penup()  # Podnosimy pisak przed narysowaniem pierwszego trójkąta.
turtle.goto(-50, 150)  # Ustawiamy pozycję startową dla trójkąta.
turtle.pendown()  # Opuszczamy pisak.
draw_triangle(90)  # Rysujemy pierwszy trójkąt o boku 90.

turtle.penup()  # Podnosimy pisak przed narysowaniem drugiego trójkąta.
turtle.goto(-50, -50)  # Przenosimy żółwia na współrzędne (-50, -50).
turtle.pendown()  # Opuszczamy pisak.
draw_triangle(70)  # Rysujemy drugi trójkąt o boku 70.

turtle.penup()  # Podnosimy pisak przed narysowaniem pierwszego prostokąta.
turtle.goto(150, 150)  # Ustawiamy pozycję po prawej stronie ekranu.
turtle.pendown()  # Opuszczamy pisak.
draw_rectangle(110, 60)  # Rysujemy pierwszy prostokąt o bokach 110 i 60.

turtle.penup()  # Podnosimy pisak przed narysowaniem drugiego prostokąta.
turtle.goto(150, -50)  # Przenosimy żółwia poniżej pierwszego prostokąta.
turtle.pendown()  # Opuszczamy pisak.
draw_rectangle(90, 50)  # Rysujemy drugi prostokąt o bokach 90 i 50.

turtle.hideturtle()  # Ukrywamy strzałkę żółwia po zakończeniu rysowania.
window.mainloop()  # Utrzymujemy okno otwarte dopóki użytkownik go nie zamknie.
