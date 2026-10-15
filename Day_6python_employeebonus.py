experience = float(input("Enter experience in years: "))
salary = float(input("Enter salary: "))
performance = int(input("Enter performance score: "))

if experience >= 1:
    if salary >= 50000:
        if performance >= 90:
            bonus = salary * 0.20
        elif performance >= 75:
            bonus = salary * 0.10
        else:
            bonus = salary * 0.05
    else:
        if performance >= 90:
            bonus = salary * 0.15
        else:
            bonus = salary * 0.05
else:
    bonus = 0

print("Bonus Amount: ₹", bonus)
print("Total Salary with Bonus: ₹", salary + bonus)