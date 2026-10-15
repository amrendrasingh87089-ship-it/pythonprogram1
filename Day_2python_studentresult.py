m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    total = m1 + m2 + m3
    percentage = total / 3

    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

    if percentage >= 75:
        print("Result: Distinction")
    elif percentage >= 60:
        print("Result: First Division")
    elif percentage >= 50:
        print("Result: Second Division")
    else:
        print("Result: Pass")
else:
    print("Result: Fail")