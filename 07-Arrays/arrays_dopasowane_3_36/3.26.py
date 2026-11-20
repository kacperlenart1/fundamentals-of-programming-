### PLIK 3.26.py: Kompletny program rysujący wykres funkcji y = sin(x) dla kątów w zakresie 0-360 stopni.
import math  # Importujemy moduł math.
import matplotlib.pyplot as plt  # Importujemy moduł matplotlib.pyplot.

x = list(range(0, 361))  # Kąty w stopniach od 0 do 360.
y = [math.sin(math.radians(angle)) for angle in x]  # Obliczamy wartości sin(x) po zamianie stopni na radiany.

plt.plot(x, y)  # Rysujemy wykres sinusa.
plt.show()  # Wyświetlamy wykres.
