pin = 1234
balance = 5000

user_pin = int(input("Enter your ATM PIN: "))

if user_pin == pin:
    amount = int(input("Enter withdrawal amount: "))

    if amount % 100 == 0:
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Amount must be a multiple of 100")
else:
    print("Invalid PIN")