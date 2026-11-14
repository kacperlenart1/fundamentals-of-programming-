###
# Program wypisujący pierwsze dwadzieścia wyrazów ciągu Fibonacciego.
#

# Definicja pierwszego i drugiego wyrazu ciągu
a = 0
b = 1

# Pętla generująca i wypisująca kolejne wyrazy ciągu Fibonacciego
for i in range(20):
    print(a, end=' ')
    next_value = a + b
    a = b
    b = next_value

print()