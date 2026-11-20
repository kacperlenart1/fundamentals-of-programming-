### PLIK 1.15.py: Kompletna funkcja bubble_sort oraz posortowanie spalania samochodów i transakcji bankowych.
def bubble_sort(arr):  # Sortuje tablicę liczb rosnąco algorytmem sortowania bąbelkowego.
    sorted_arr = arr.copy()  # Tworzymy kopię tablicy, aby nie modyfikować oryginału w miejscu.
    n = len(sorted_arr)  # Pobieramy długość tablicy.
    for i in range(n):  # Zewnętrzna pętla przebiegów sortowania.
        for j in range(0, n - i - 1):  # Wewnętrzna pętla porównująca sąsiednie elementy.
            if sorted_arr[j] > sorted_arr[j + 1]:  # Gdy lewy element jest większy od prawego.
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]  # Zamieniamy elementy miejscami.
    return sorted_arr  # Zwracamy posortowaną tablicę.


car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]  # Spalanie paliwa samochodów.
print("Car fuel consumption:", car_fuel_consumption)  # Wypisujemy spalanie przed sortowaniem.
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)  # Sortujemy spalanie paliwa.
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)  # Wypisujemy spalanie po sortowaniu.

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]  # Transakcje bankowe.
print("Bank transactions:", bank_transactions)  # Wypisujemy transakcje przed sortowaniem.
sorted_bank_transactions = bubble_sort(bank_transactions)  # Sortujemy transakcje bankowe.
print("Sorted bank transactions:", sorted_bank_transactions)  # Wypisujemy transakcje po sortowaniu.
