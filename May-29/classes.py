# 4. Class: Rectangle
# Attributes: length , width
# Methods:
# area()
# perimeter()
# is_square() → returns True if length == width

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("Area:",(self.length * self.width))
    def perimeter(self):
        print("Perimeter:", (2*(self.length + self.width)))
    def is_square(self):
        return (self.length== self.width)

rec=Rectangle(8,8)
rec.area()
rec.perimeter()
print(rec.is_square())

# 5. Class: BankAccount
# Attributes: name , balance
# Methods:
# deposit(amount)
# withdraw(amount)
# get_balance()
# Prevent withdrawal if balance is insufficient
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount Deposited by {self.name}.")
    def withdraw(self,amount):
        if self.balance < amount:
            print("Balance Insufficient")
        else:
            self.balance-=amount
            print("Amount withdrawn successfully.")
    def get_balance(self):
        print(f"Available balance: {self.balance:.2f}")
# Create account
acc = BankAccount("Priya", 1000)
acc.get_balance()
acc.deposit(500)
acc.get_balance()
acc.withdraw(2000)
acc.withdraw(800)
acc.get_balance()


# 6. Class: Book
# Attributes: title , author , price , in_stock
# Method: sell(quantity)
# Reduces stock
# Throws an error if quantity exceeds stock

class Book:
    def __init__(self,title,author,price,in_stock):
        self.title=title
        self.author=author
        self.price=price
        self.in_stock=in_stock
    def sell(self,qty):
        if qty > self.in_stock:
            print("Quantity exceeds stock")
        else:
            self.in_stock -=qty
            total_price=qty* self.price
            print("Total Price",total_price)
            print("Remaining stock:", self.in_stock)
b=Book("Alchemist","Paul Coelho",20,30)
b.sell(32)
b.sell(5)

# 7. Student Grade System
#
# Create a class Student with:
# Attributes: name , marks (a list)
# Method:
# average()
# grade() — returns A/B/C/F based on average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        total=sum(self.marks)
        avg = total / len(self.marks)
        print(f"Average: {avg:.2f}")
        return avg
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg>=60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'
s1 = Student("John", [80, 92, 78, 92, 75])
print("Student Name:",s1.name)
print("Grade:", s1.grade())