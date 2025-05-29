#
# 8. Person → Employee
# Class Person : name , age
# Class Employee inherits Person , adds emp_id , salary
# Method display_info() shows all details
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.salary=salary
    def display_info(self):
        print(f"Employee Id:{self.emp_id}")
        print(f"Employee Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Salary:{self.salary}")
e1=Employee("Rohini",25,101,30000)
e1.display_info()

# 9. Vehicle → Car , Bike
# Base Class: Vehicle(name, wheels)
# Subclasses:
# Car : additional attribute fuel_type
# Bike : additional attribute is_geared
# Override a method description() in both
class Vehicle:
    def __init__(self,name,wheels):
        self.name = name
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, name, wheels, fuel_type):
        super().__init__(name, wheels)
        self.fuel_type = fuel_type

    def description(self):
        print(f"Car Name: {self.name}")
        print(f"Wheels: {self.wheels}")
        print(f"Fuel Type: {self.fuel_type}")

class Bike(Vehicle):
    def __init__(self, name, wheels, is_geared):
        super().__init__(name, wheels)
        self.is_geared = is_geared

    def description(self):
        print(f"Car Name: {self.name}")
        print(f"Wheels: {self.wheels}")
        print(f"Geared: {'Yes' if self.is_geared else 'No'}")

car1 = Car("BMW", 4, "Petrol")
bike1 = Bike("Hero Splendor", 2, True)

print("Car Details:")
car1.description()

print("\nBike Details:")
bike1.description()

# 10. Polymorphism with Animals
# Base class Animal with method speak()
# Subclasses Dog , Cat , Cow override speak() with unique sounds
# Call speak() on each object in a loop

class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

class Cow(Animal):
    def speak(self):
        print("Cow moos.")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()
