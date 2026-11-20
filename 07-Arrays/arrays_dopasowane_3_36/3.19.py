### PLIK 3.19.py: Kompletny program zliczający elementy tablicy liczb rzeczywistych większe od wartości z klawiatury.
real_array = [2.5, 7.1, 12.4, 3.8, 9.6, 15.0, 1.2]  # Tablica liczb rzeczywistych.
threshold = float(input("Enter number: "))  # Wczytujemy wartość z klawiatury.

count_greater = 0  # Licznik elementów większych od podanej wartości.
for num in real_array:  # Sprawdzamy każdy element tablicy.
    if num > threshold:  # Gdy element jest większy od wartości wpisanej przez użytkownika.
        count_greater += 1  # Zwiększamy licznik.

print("Array:", real_array)  # Wypisujemy tablicę.
print("Number of elements greater than input:", count_greater)  # Wypisujemy liczbę większych elementów.
