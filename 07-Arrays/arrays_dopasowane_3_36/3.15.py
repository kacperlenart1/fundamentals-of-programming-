### PLIK 3.15.py: Kompletny program wypisujący krotkę (10,20,30,40,50) w kolejności oryginalnej oraz odwrotnej.
my_tuple = (10, 20, 30, 40, 50)  # Tworzymy krotkę z wartościami 10, 20, 30, 40, 50.
reversed_tuple = my_tuple[::-1]  # Odwracamy krotkę wycinkiem z krokiem -1.

print("Tuple:", ",".join(str(x) for x in my_tuple))  # Wypisujemy krotkę w oryginalnej kolejności.
print("Reverse order:", ",".join(str(x) for x in reversed_tuple))  # Wypisujemy krotkę w odwrotnej kolejności.
