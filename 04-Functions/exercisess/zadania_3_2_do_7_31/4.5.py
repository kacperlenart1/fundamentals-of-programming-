### PLIK 4.5.py: Funkcja przeliczająca liczbę punktów na ocenę końcową według podanych progów.
def pts_to_grade(points):  # Definiujemy funkcję sprawdzającą próg punktowy dla parametru points.
    grade = ""  # Tworzymy pusty napis na ocenę końcową.
    if points >= 18:  # Najpierw sprawdzamy najwyższy próg punktowy, czyli co najmniej 18 punktów.
        grade = "Excellent"  # Przypisujemy ocenę Excellent.
    elif points >= 14:  # Jeśli punktów jest mniej niż 18, sprawdzamy próg od 14 punktów.
        grade = "Good"  # Przypisujemy ocenę Good.
    elif points >= 10:  # Jeśli punktów jest mniej niż 14, sprawdzamy próg od 10 punktów.
        grade = "Satisfactory"  # Przypisujemy ocenę Satisfactory.
    else:  # W każdym innym przypadku, czyli poniżej 10 punktów.
        grade = "Fail"  # Przypisujemy ocenę Fail.
    return grade  # Zwracamy wyznaczoną ocenę.


test_result = 15  # Ustawiamy przykładowy wynik testu równy 15 punktom.
final_grade = pts_to_grade(test_result)  # Przeliczamy punkty na ocenę wywołując funkcję pts_to_grade.
print(f"You scored {test_result} points on the test. Your final grade is {final_grade}")  # Wypisujemy wynik testu i ocenę.
