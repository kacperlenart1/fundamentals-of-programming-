###
# Program obliczający sumę liczb parzystych w zakresie od 1 do 10.
#

sum = 0

# Pętla przechodząca przez liczby od 1 do 10 włącznie
for i in range(1, 11):
    # Sprawdzenie czy liczba jest parzysta (reszta z dzielenia przez 2 wynosi 0)
    if i % 2 == 0:
        sum += i

# Wyświetlenie ostatecznego wyniku sumowania
print(f'Sum of even numbers in the range <1,10> is {sum}')