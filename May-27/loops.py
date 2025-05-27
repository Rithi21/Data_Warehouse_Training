# 9. Find All Prime Numbers Between 1 and 100 Use a nested loop to check
# divisibility.
print("Prime numbers between 1 and 100:")

for i in range(2, 101):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")

# 10. Palindrome Checker Ask for a string and check whether it reads the same backward.

def isPalindrome(str):
  l=0
  r=len(str)-1
  while(l<r):
    if(str[l]!=str[r]):
      return False
    l+=1
    r-=1
  return True
s=input("Enter String: ")
if(isPalindrome(s)):
  print(f'{s} is palindrome')
else:
  print(f'{s} is not palindrome')

# 11. Fibonacci Series (First N Terms) Input n , and print first n terms of the
# Fibonacci sequence.
n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Fibonacci Series:")
if n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for _ in range(2, n):
        res = a + b
        print(res, end=" ")
        a = b
        b = res

#12. Multiplication Table (User Input) Take a number and print its table up to 10:

num = int(input("Enter a number: "))

print(f"Multiplication Table for {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

