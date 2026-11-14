###
# Program obliczający sumę liczb parzystych od 1 do podanej liczby N przy użyciu pętli while.
#

N = 10
sum_even = 0
i = 1

# Obliczenie sumy liczb parzystych za pomocą pętli while
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

# Wyświetlenie ostatecznego wyniku sumowania
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")