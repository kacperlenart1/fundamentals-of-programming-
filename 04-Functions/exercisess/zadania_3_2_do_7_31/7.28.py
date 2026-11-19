### PLIK 7.28.py: Funkcja zwracająca cyfrę która wystąpiła najwięcej razy z rzędu w podanym ciągu rzutów.
def f(dice):  # Przyjmujemy ciąg wyników rzutów kostką.
    if not dice:  # Jeśli ciąg jest pusty, nie ma żadnego rzutu.
        return None  # Zwracamy None.
    best_digit = dice[0]  # Najlepsza cyfra na start to pierwszy znak.
    best_streak = 1  # Najdłuższa seria na start wynosi 1.
    current_digit = dice[0]  # Aktualnie badana cyfra.
    current_streak = 1  # Długość bieżącej serii powtórzeń pod rząd.

    for ch in dice[1:]:  # Przeglądamy kolejne rzuty począwszy od drugiego znaku.
        if ch == current_digit:  # Jeśli trafiliśmy na tę samą cyfrę co poprzednio.
            current_streak += 1  # Wydłużamy bieżącą serię o 1.
        else:  # Gdy pojawiła się inna cyfra.
            current_digit = ch  # Zmieniamy aktualnie badaną cyfrę.
            current_streak = 1  # Zaczynamy nową serię od długości 1.
        if current_streak > best_streak:  # Jeśli obecna seria jest dłuższa niż dotychczasowy rekord.
            best_streak = current_streak  # Aktualizujemy rekord długości serii.
            best_digit = current_digit  # Zapisujemy cyfrę, która ustanowiła ten rekord.

    return int(best_digit)  # Zwracamy cyfrę o najdłuższej serii jako liczbę całkowitą.


print(f("5233165554211"))  # Cyfra 5 wystąpiła trzy razy z rzędu, wynik to 5.
print(f("2133"))  # Cyfra 3 wystąpiła dwa razy z rzędu, wynik to 3.
