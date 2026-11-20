### PLIK 3.3.py: Program sprawdzający poprawność zagnieżdżenia i kolejności nawiasów (), {}, [] za pomocą stosu.
import queue  # Importujemy moduł queue.

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # Poprawne nawiasy.
expression2 = "[(2+3]/4)"  # Niepoprawne nawiasy.
expression3 = "(2-3*4+(5/6)"  # Niepoprawny nawias (brak zamknięcia).


def brackets_ok(expression):  # Zwraca True, jeśli nawiasy w wyrażeniu są użyte poprawnie.
    stack = queue.LifoQueue()  # Stos przechowujący otwierające nawiasy.
    pairs = {")": "(", "}": "{", "]": "["}  # Mapa: nawias zamykający -> odpowiadający otwierający.

    for char in expression:  # Przechodzimy przez kolejne znaki wyrażenia.
        if char in "({[":  # Jeśli znak jest nawiasem otwierającym.
            stack.put(char)  # Odkładamy go na stos.
        elif char in ")}]":  # Jeśli znak jest nawiasem zamykającym.
            if stack.empty():  # Brak otwierającego nawiasu na stosie oznacza błąd.
                return False  # Zwracamy False.
            opening = stack.get()  # Zdejmujemy ostatni otwierający nawias ze stosu.
            if opening != pairs[char]:  # Sprawdzamy, czy typy nawiasów pasują do siebie.
                return False  # Zwracamy False przy niezgodności.

    return stack.empty()  # Poprawnie zamknięte wyrażenie zostawia pusty stos.


for idx, expr in enumerate([expression1, expression2, expression3], start=1):  # Testujemy wszystkie wyrażenia.
    if brackets_ok(expr):  # Sprawdzamy wynik funkcji brackets_ok.
        print(f"Expression {idx}: brackets OK")  # Komunikat o poprawnych nawiasach.
    else:  # Gdy nawiasy są błędne.
        print(f"Expression {idx}: brackets NOT correct")  # Komunikat o błędnych nawiasach.
