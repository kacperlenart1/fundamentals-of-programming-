### PLIK 3.1.py: Program wykonujący zadane operacje odkładania i sumowania elementów na stosie LIFO.
import queue  # Importujemy moduł queue zawierający LifoQueue.

stack = queue.LifoQueue()  # Tworzymy pusty stos (LIFO).

for number in [2, 3, 7, 4, 1, 9, 8]:  # Odkładamy kolejno podane liczby na stos.
    stack.put(number)  # Wrzucamy liczbę na wierzch stosu.

last_two_sum = stack.get() + stack.get()  # Zdejmujemy dwie ostatnie liczby i je sumujemy.
print("Sum of last two numbers:", last_two_sum)  # Wypisujemy sumę dwóch ostatnich elementów (8 + 9 = 17).

remaining_sum = 0  # Akumulator dla pozostałych na stosie elementów.
while not stack.empty():  # Dopóki stos nie jest pusty.
    remaining_sum += stack.get()  # Zdejmujemy kolejny element i dodajemy do sumy.

print("Sum of remaining stack elements:", remaining_sum)  # Wypisujemy sumę pozostałych liczb.
