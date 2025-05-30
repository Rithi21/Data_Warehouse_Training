#  Section 4: File Handling
# Q10. Write to a file the names of employees who belong to the 'IT' department.
employees = [
    {"name": "Rina", "dept": "HR"},
    {"name": "Anjali", "dept": "IT"},
    {"name": "Rahul", "dept": "IT"},
    {"name": "Meena", "dept": "Finance"}
]

with open("employees_dept_it.txt", "w") as file:
    for emp in employees:
        if emp["dept"] == "IT":
            file.write(emp["name"] + "\n")

# Q11. Read from a text file and count the number of words.
with open("output.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Number of words:", len(words))

#  Section 5: Exception Handling
# Q12. Write a program that accepts a number from the user and prints the square. Handle
# the case when input is not a number.
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Invalid input... Enter a valid number.")

# Q13. Handle a potential ZeroDivisionError in a division function.

def divide(a, b):
    try:
        result = a // b
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

divide(5, 0)
