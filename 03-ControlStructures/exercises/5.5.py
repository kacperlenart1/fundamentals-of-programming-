###
# Program sumujący liczby wprowadzane przez użytkownika do momentu wpisania 0 oraz obliczający ich średnią arytmetyczną.
#

total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break  # Wyjście z pętli po wpisaniu 0
    total_sum += number
    count += 1

# Obliczenie i wyświetlenie wyniku, jeśli wprowadzono jakiekolwiek liczby
if count > 0:
    arithmetic_mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean is: {arithmetic_mean}")
else:
    print("No numbers were entered.")