cart_amount = float(input("Enter cart amount: "))
premium = input("Are you a premium member? (yes/no): ").lower()

if cart_amount >= 5000:
    if premium == "yes":
        discount = 20
    else:
        discount = 10
else:
    if premium == "yes":
        discount = 5
    else:
        discount = 0

discount_amount = cart_amount * discount / 100
final_amount = cart_amount - discount_amount

print("Cart Amount: ₹", cart_amount)
print("Discount:", discount, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Amount: ₹", final_amount)