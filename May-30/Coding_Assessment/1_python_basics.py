
# Q1. Write a Python program to print all odd numbers between 10 and 50.

for number in range(11, 50):
    if number % 2 !=0:
        print(number,end=" ")

# Q2. Create a function that returns whether a given year is a leap year.

def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False

year=int(input("\nEnter year: "))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Q3. Write a loop that counts how many times the letter a appears in a given string

s=input("Enter string: ")
count=0
for ch in s.lower():
    if ch=='a':
        count+=1
print("Count of 'a':",count)

