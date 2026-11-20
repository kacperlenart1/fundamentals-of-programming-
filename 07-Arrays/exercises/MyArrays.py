### PLIK MyArrays.py: Kompletny moduł ze wszystkimi 5 funkcjami operującymi na tablicy liczb zgodnie z zadaniem 3.18.
def second_largest(arr):  # Funkcja 1: zwraca drugi największy element w tablicy liczb.
    unique_values = []  # Lista przechowująca unikalne liczby z tablicy.
    for item in arr:  # Przechodzimy przez wszystkie elementy tablicy wejściowej.
        if item not in unique_values:  # Dodajemy liczbę tylko wtedy, gdy jeszcze nie wystąpiła.
            unique_values.append(item)  # Dopisujemy unikalną wartość do listy.
    for i in range(len(unique_values)):  # Sortujemy unikalne wartości rosnąco prostą pętlą porównującą.
        for j in range(i + 1, len(unique_values)):  # Porównujemy bieżący element z kolejnymi.
            if unique_values[j] < unique_values[i]:  # Gdy kolejny element jest mniejszy od wcześniejszego.
                unique_values[i], unique_values[j] = unique_values[j], unique_values[i]  # Zamieniamy je miejscami.
    return unique_values[-2]  # Zwracamy drugą największą wartość.


def diff_min_max(arr):  # Funkcja 2: zwraca różnicę między największą a najmniejszą wartością w tablicy.
    smallest = arr[0]  # Przyjmujemy pierwszy element jako aktualne minimum.
    largest = arr[0]  # Przyjmujemy pierwszy element jako aktualne maksimum.
    for item in arr[1:]:  # Przeglądamy pozostałe elementy tablicy.
        if item < smallest:  # Jeśli znajdziemy mniejszą wartość.
            smallest = item  # Aktualizujemy najmniejszą wartość.
        if item > largest:  # Jeśli znajdziemy większą wartość.
            largest = item  # Aktualizujemy największą wartość.
    return largest - smallest  # Zwracamy różnicę pomiędzy największą a najmniejszą wartością.


def median(arr):  # Funkcja 3: zwraca medianę liczb w tablicy bez używania gotowych funkcji statystycznych.
    ordered = arr.copy()  # Tworzymy kopię tablicy, aby nie modyfikować oryginału.
    n = len(ordered)  # Pobieramy liczbę elementów w tablicy.
    for i in range(n):  # Sortujemy elementy rosnąco w pętlach.
        for j in range(0, n - i - 1):  # Porównujemy sąsiednie elementy.
            if ordered[j] > ordered[j + 1]:  # Gdy element po lewej jest większy od elementu po prawej.
                ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]  # Zamieniamy sąsiednie elementy miejscami.
    mid = n // 2  # Wyznaczamy środkowy indeks posortowanej sekwencji.
    if n % 2 == 1:  # Gdy liczba elementów jest nieparzysta, mediana to środkowy element.
        return ordered[mid]  # Zwracamy wartość środkową.
    return (ordered[mid - 1] + ordered[mid]) / 2  # Gdy liczba elementów jest parzysta, zwracamy średnią dwóch środkowych.


def min_max(arr):  # Funkcja 4: zwraca dwuelementową tablicę zawierającą najmniejszą i największą wartość.
    smallest = arr[0]  # Przyjmujemy pierwszy element jako aktualne minimum.
    largest = arr[0]  # Przyjmujemy pierwszy element jako aktualne maksimum.
    for item in arr[1:]:  # Sprawdzamy kolejne elementy tablicy.
        if item < smallest:  # Jeśli element jest mniejszy od dotychczasowego minimum.
            smallest = item  # Aktualizujemy wartość minimalną.
        if item > largest:  # Jeśli element jest większy od dotychczasowego maksimum.
            largest = item  # Aktualizujemy wartość maksymalną.
    return [smallest, largest]  # Zwracamy dwuelementową listę [najmniejsza, największa].


def to_minus_string(arr):  # Funkcja 5: zwraca elementy tablicy jako napis rozdzielony znakiem minusa.
    result = ""  # Zmienna budująca napis wynikowy.
    for i in range(len(arr)):  # Przechodzimy po wszystkich indeksach tablicy.
        if i > 0:  # Przed każdym kolejnym elementem dodajemy znak minusa.
            result += "-"  # Dopisujemy pojedynczy znak minusa.
        result += str(arr[i])  # Dopisujemy wartość elementu zamienioną na napis.
    return result  # Zwracamy gotowy napis.
