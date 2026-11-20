### PLIK 3.24.py: Kompletny program rysujący w matplotlib linię od pozycji (1, 3) do pozycji (8, 10).
import matplotlib.pyplot as plt  # Importujemy moduł matplotlib.pyplot.

xpoints = [1, 8]  # Współrzędne x punktów końcowych.
ypoints = [3, 10]  # Współrzędne y punktów końcowych.

plt.plot(xpoints, ypoints)  # Rysujemy linię pomiędzy punktami (1, 3) i (8, 10).
plt.show()  # Wyświetlamy wykres.
