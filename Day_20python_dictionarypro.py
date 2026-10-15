# Dictionary Program 1: Student Result

student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "marks": 75
}

print("Student Details")

for key, value in student.items():
    print(key, ":", value)

if student["marks"] >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")






    # Dictionary Program 2: Employee Salary

employee = {
    "name": "Amit",
    "age": 25,
    "department": "IT",
    "salary": 25000
}

print("Employee Details")

for key, value in employee.items():
    print(key, ":", value)

if employee["salary"] > 20000:
    print("Salary Status: Good")
else:
    print("Salary Status: Low")

employee["bonus"] = 2000

print("Updated Employee Details")

for key, value in employee.items():
    print(key, ":", value)