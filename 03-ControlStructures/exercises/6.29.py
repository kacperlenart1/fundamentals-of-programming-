###
# Program znajdujący pierwsze N liczb pierwszych na podstawie liczby wczytanej z klawiatury.
#

n = int(input("Enter N: "))
primes = []
candidate = 2

# Pętla zbierająca dokładnie N kolejnych liczb pierwszych
while len(primes) < n:
    is_prime = True
    for i in range(2, int(candidate ** 0.5) + 1):
        if candidate % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)
    candidate += 1

# Wyświetlenie znalezionych liczb pierwszych
print("Prime numbers:", end=" ")
for p in primes:
    print(p, end=" ")
print()