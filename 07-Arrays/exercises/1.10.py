### PLIK 1.10.py: Kompletny program obliczający i wypisujący pełne statystyki testu z wartości True/False.
test_results = [  # Wyniki testu: True = poprawna odpowiedź, False = błędna odpowiedź.
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]  # Koniec listy wyników.

question_number = len(test_results)  # Obliczamy łączną liczbę pytań w teście.

correct_answers = 0  # Licznik poprawnych odpowiedzi.
for answer in test_results:  # Przechodzimy przez każdy wynik w liście.
    if answer:  # Sprawdzamy czy odpowiedź ma wartość True.
        correct_answers += 1  # Zwiększamy liczbę poprawnych odpowiedzi.

incorrect_answers = question_number - correct_answers  # Obliczamy liczbę błędnych odpowiedzi.
percentage_correct = (correct_answers / question_number) * 100  # Obliczamy procent poprawnych odpowiedzi.

print("TEST STATISTICS")  # Wypisujemy nagłówek raportu.
print("===============")  # Wypisujemy linię oddzielającą.
print("Number of questions:", question_number)  # Wypisujemy liczbę pytań.
print("Number of correct answers:", correct_answers)  # Wypisujemy liczbę poprawnych odpowiedzi.
print("Number of incorrect answers:", incorrect_answers)  # Wypisujemy liczbę błędnych odpowiedzi.
print(f"Percentage of correct answers: {percentage_correct:.2f}%")  # Wypisujemy procent poprawnych odpowiedzi.
