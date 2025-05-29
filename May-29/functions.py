
# 1. Prime Number Checker

import math

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

for i in range(1,101):
    if isPrime(i):
        print(i,end=" ")


# 2. Temperature Converter
# Write a function convert_temp(value, unit) that converts:
# Celsius to Fahrenheit
# Fahrenheit to Celsius Use conditionals inside the function.

def tempConvert(value,unit):
    unit=unit.upper()
    if unit=='C':
        res= (value * 9/5)+ 32
        return f"{res:.2f} F"
    elif unit=='F':
        res= (value - 32) * 5/9
        return f"{res:.2f} C"
    else:
        return "Invalid unit"

value=int(input("\nEnter value:"))
unit=input("Enter unit:")
print(tempConvert(value,unit))


# 3. Recursive Factorial Function

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

n=int(input("Enter number:"))
print("Factorial:",factorial(n))