### PLIK 5.13.py: Kalkulator wyrażeń w odwrotnej notacji polskiej (RPN) oparty na stosie.
import queue  # Importujemy moduł queue.


def evaluate_rpn(tokens):  # Oblicza wartość wyrażenia RPN podanego jako lista tokenów.
    stack = queue.LifoQueue()  # Stos liczb pośrednich.

    for token in tokens:  # Przetwarzamy kolejne elementy wyrażenia.
        if token == "=":  # Znak równości kończy wyrażenie i zwraca wynik.
            return stack.get() if not stack.empty() else None  # Zdejmujemy wynik końcowy.
        elif token in {"+", "-", "*", "/"}:  # Jeśli token jest operatorem arytmetycznym.
            b = stack.get()  # Zdejmujemy prawy operand.
            a = stack.get()  # Zdejmujemy lewy operand.
            if token == "+":  # Dodawanie.
                stack.put(a + b)  # Odkładamy wynik na stos.
            elif token == "-":  # Odejmowanie.
                stack.put(a - b)  # Odkładamy wynik na stos.
            elif token == "*":  # Mnożenie.
                stack.put(a * b)  # Odkładamy wynik na stos.
            elif token == "/":  # Dzielenie.
                stack.put(a / b)  # Odkładamy wynik na stos.
        else:  # W przeciwnym razie traktujemy token jako liczbę.
            stack.put(float(token))  # Odkładamy liczbę na stos.

    return stack.get() if not stack.empty() else None  # Zwracamy wynik, jeśli nie podano '='.


expr_input = input("Enter RPN expression (e.g. 2 3 + =): ").replace("–", "-").strip()  # Czytamy wyrażenie i ujednolicamy minus.
tokens = expr_input.split()  # Dzielimy wejście na pojedyncze tokeny.
result = evaluate_rpn(tokens)  # Obliczamy wynik RPN.
print("Result:", result)  # Wypisujemy wynik obliczeń.
