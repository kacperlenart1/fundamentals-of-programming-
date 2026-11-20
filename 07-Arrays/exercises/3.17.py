### PLIK 3.17.py: Kompletny program zliczający liczbę wystąpień podanej wartości w krotce.
my_tuple = (50, 20, 40, 50, 30, 50)  # Krotka z przykładowego wyniku.
value = 50  # Wartość, której wystąpienia zliczamy.
count_value = my_tuple.count(value)  # Obliczamy liczbę wystąpień wartości w krotce.

print("Tuple:", ",".join(str(x) for x in my_tuple))  # Wypisujemy krotkę.
print("Value:", value)  # Wypisujemy sprawdzaną wartość.
print("Number of occurrences:", count_value)  # Wypisujemy liczbę wystąpień.
