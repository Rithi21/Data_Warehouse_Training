#Digit Sum Calculator
n=int(input("Enter number:"))
s=str(n)
digit_sum=0
for i in s:
    digit_sum+=int(i)
print(f"Sum: {digit_sum}")

#Reverse a 3-digit Number
n=int(input("Enter number:"))
rev=0
while n>0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print(f"Reversed Number: {rev}")

#Unit Converter:
m=int(input("Enter input in meters: "))
print(f"Centimeters: {m * 100} cm")
print(f"Feet: {m * 3.28084:.2f} ft")
print(f"Inches: {m * 39.3701:.2f} inch")

#Percentage Calculator: Input marks of 5 subjects and calculate total, average, and percentage. Display grade based on the percentage.
total=0
for i in range(1,6):
    mark=int(input(f"Enter Marks of subject {i}: "))
    total+=mark
avg=total/5
percentage=(total/500)*100

print(f"Total Marks: {total}")
print(f"Average: {avg}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print(f"Grade: {grade}")