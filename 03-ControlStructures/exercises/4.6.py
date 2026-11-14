###
# Program obliczający sumę liczb całkowitych w zakresie od 5 do 10 przy użyciu operatora +=.
#

sum = 0

# Pętla sumująca liczby od 5 do 10 (range(5, 11) obejmuje liczby od 5 do 10 włącznie)
for i in range(5, 11):
    sum += i

# Wyświetlenie ostatecznego wyniku sumowania
print(f'Sum is {sum}')