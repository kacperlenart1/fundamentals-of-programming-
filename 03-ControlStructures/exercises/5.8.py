###
# Program symulujący działanie bankomatu z obsługą salda, wpłat, wypłat oraz weryfikacji i zmiany kodu PIN.
#

balance = 1000  # Initial balance
pin = '1111'  # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ")
    print()
    
    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        # Sprawdzenie poprawności 4-cyfrowego kodu PIN
        entered_pin = input("Enter your PIN: ")
        if len(entered_pin) == 4 and entered_pin.isdigit():
            if entered_pin == pin:
                print("PIN is correct.")
            else:
                print("Incorrect PIN.")
        else:
            print("Invalid PIN format. PIN must consist of exactly 4 digits.")
    elif choice == '5':
        # Zmiana obecnego kodu PIN na nowy
        current_pin = input("Enter current PIN: ")
        if current_pin == pin:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN has been successfully changed.")
            else:
                print("Invalid new PIN format. PIN must consist of exactly 4 digits.")
        else:
            print("Incorrect current PIN.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")