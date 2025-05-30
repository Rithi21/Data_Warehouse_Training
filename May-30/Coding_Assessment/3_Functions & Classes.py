
# Q7. Write a class Employee with __init__ , display() , and is_high_earner() methods.
# An employee is a high earner if salary > 60000
class Employee:
    def __init__(self, name,dept,salary):
        self.name = name
        self.dept=dept
        self.salary = salary

    def display(self):
        print(f"Name: {self.name},Department:{self.dept}, Salary: {self.salary}")

    def is_high_earner(self):
        return self.salary > 60000

# Q8. Create a class Project that inherits from Employee and adds project_name and
# hours_allocated .
class Project(Employee):
    def __init__(self, name, dept,salary, project_name, hours_allocated):
        super().__init__(name, dept,salary)
        self.project_name = project_name
        self.hours_allocated = hours_allocated

    def display(self):
        super().display()
        print(f"Project: {self.project_name}, Hours Allocated: {self.hours_allocated}")

# Q9. Instantiate 3 employees and print whether they are high earners

emp1 = Employee("Rina", 'IT',45000)
emp2 = Employee("Anjali", 'IT',75000)
emp3 = Employee("Rahul", 'HR',50000)

employees = [emp1, emp2, emp3]

for emp in employees:
    emp.display()
    if emp.is_high_earner():
        print("High Earner\n")
    else:
        print("Not a High Earner\n")

