correct_pin = 1234
balance = 25000
account_active = True

pin = int(input("Enter ATM PIN: "))

if pin == correct_pin:
    if account_active:
        amount = int(input("Enter withdrawal amount: "))

        if amount > 0:
            if amount % 100 == 0:
                if balance - amount >= 500:
                    if amount > 20000:
                        print("Extra verification required")
                    else:
                        balance -= amount
                        print("Withdrawal Successful")
                        print("Remaining Balance: ₹", balance)
                else:
                    print("Minimum ₹500 balance required")
            else:
                print("Amount must be a multiple of ₹100")
        else:
            print("Amount must be positive")
    else:
        print("Account is inactive")
else:
    print("Invalid PIN")