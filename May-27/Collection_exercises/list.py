# LISTS
# 1. Create a list of squares of numbers from 1 to 20.

squares=list(map(lambda x:x**2,range(1,21)))
print(squares)

# 2. Find the second largest number in a list without using sort().

l=list(map(int,input("Enter list of numbers: ").split()))

first=-1
second=-1
for i in l:
    if i>first:
        second=first
        first=i
    elif first>i>second:
        second=i
print(second)

# 3. Write a program to remove all duplicate values from a list while preserving order.
l=list(map(int,input("Enter list of numbers: ").split()))
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print(unique)


# 4. Rotate List Rotate a list to the right by k steps. Example: [1, 2, 3, 4, 5] rotated by 2 → [4, 5, 1, 2, 3]

l=list(map(int,input("Enter list of numbers: ").split()))
k=int(input("Enter steps to rotate:"))
k = k % len(l)

rotated = l[-k:] + l[:-k]
print(rotated)

# 5. List Compression From a list of numbers, create a new list with only the even numbers doubled.
l=list(map(int,input("Enter list of numbers: ").split()))
result=[]
for i in l:
    if i % 2==0:
        result.append(i*2)
    else:
        result.append(i)
print(result)