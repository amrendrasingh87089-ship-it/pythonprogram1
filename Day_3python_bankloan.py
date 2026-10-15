age = int(input("Enter your age: "))

if age >= 21:
    salary = float(input("Enter your monthly salary: "))

    if salary >= 25000:
        credit_score = int(input("Enter your credit score: "))

        if credit_score >= 750:
            print("Loan Approved")
        elif credit_score >= 650:
            print("Loan Approved with Higher Interest")
        else:
            print("Loan Rejected")
    else:
        print("Loan Rejected: Salary must be at least 25000")
else:
    print("Loan Rejected: Age must be at least 21")