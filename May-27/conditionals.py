#5. Leap Year Checker A year is a leap year if it’s divisible by 4 and (not divisible by 100 or
# divisible by 400).
year=int(input("Enter year: "))
if (year % 4 == 0) and ((year % 400 ==0) or (year % 100 !=0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#6. Simple Calculator Input two numbers and an operator ( + - * / ) and perform the
#operation using if...elif...else .

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
op=input("Enter operator: ")
if op=='+':
    print(f"Add:{num1 + num2}")
elif op == '-':
    print(f"Sub:{num1 - num2}")
elif op=='*':
    print(f"Multiply:{num1 * num2}")
elif op=='/':
    if num2 != 0:
        print(f"Divide: {num1 / num2}")
    else:
        print("Error: Divide by zero")
else:
    print("Invalid operator")

#7. Triangle Validator Given 3 side lengths, check whether they can form a valid
#triangle.
a=int(input("Enter side length:"))
b=int(input("Enter side length:"))
c=int(input("Enter side length:"))
if (a+b > c) and (b+c>a) and (c+a>b):
    print("Valid")
else:
    print("Invalid")

#8. Bill Splitter with Tip Ask total bill amount, number of people, and tip
#percentage. Show final amount per person.

bill_amt=float(input("Enter bill amount:"))

people=int(input("Enter number of people:"))

tip=int(input("Enter tip percentage:"))

tip_amt=(tip/100)* bill_amt
total_amt = bill_amt + tip_amt
final_amt=total_amt/people

print(f"Total Amount: {total_amt:.2f}")
print(f"Final amount per person {final_amt:.2f}")
