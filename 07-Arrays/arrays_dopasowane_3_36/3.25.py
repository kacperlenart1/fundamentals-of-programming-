### PLIK 3.25.py: Kompletny program rysujący wykres funkcji f(x) = x^2 - 3 dla n w zakresie od -100 do 100.
import matplotlib.pyplot as plt  # Importujemy moduł matplotlib.pyplot.

x = []  # Lista wartości x.
y = []  # Lista wartości y.

for n in range(-100, 101):  # Tworzymy wartości x od -100 do 100.
    x = x + [n]  # Dodajemy n do listy x.

for n in x:  # Obliczamy wartości y = n^2 - 3 dla każdego n z listy x.
    y = y + [n ** 2 - 3]  # Dodajemy wartość funkcji do listy y.

plt.plot(x, y)  # Rysujemy wykres funkcji.
plt.show()  # Wyświetlamy wykres.
