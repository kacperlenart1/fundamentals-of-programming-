###
# Program sprawdza poprawność kodu PIN do karty płatniczej, pozwalając na maksymalnie trzy próby przed zablokowaniem.
#

correct_pin = '0805'
attempts_left = 3

# Pętla pozwalająca na podanie kodu maksymalnie 3 razy
for i in range(3):
    entered_pin = input('Enter the PIN code: ')
    
    if entered_pin == correct_pin:
        print('PIN is correct!')
        break
    else:
        print('Incorrect...')
        attempts_left -= 1
else:
    # Wyświetlenie komunikatu o zablokowaniu karty po 3 nieudanych próbach
    print('Sorry, your payment card has been blocked.')