### PLIK 3.20.py: Kompletny program rozdzielający liczby parzyste i nieparzyste (najpierw parzyste, potem nieparzyste).
arr = [7, 9, 2, 4, 5, 6]  # Tablica wejściowa.
print("arr =", arr)  # Wypisujemy tablicę przed rozdzieleniem.

evens = []  # Lista liczb parzystych.
odds = []  # Lista liczb nieparzystych.

for num in arr:  # Rozdzielamy elementy na parzyste i nieparzyste.
    if num % 2 == 0:  # Liczba parzysta.
        evens.append(num)  # Dodajemy do listy parzystych.
    else:  # Liczba nieparzysta.
        odds.append(num)  # Dodajemy do listy nieparzystych.

arr = evens + odds  # Najpierw liczby parzyste, następnie nieparzyste.
print("arr =", arr)  # Wypisujemy tablicę po rozdzieleniu.
