# SETS
# 9. Common Items: Find the common elements in two user-defined lists using sets.
l1 = list(map(int, input("Enter elements: ").split()))
l2 = list(map(int, input("Enter elements: ").split()))

common = set(l1) & set(l2)
print("Common elements:", list(common))

# 10. Unique Words in Sentence : Take a sentence from the user and print all unique words.

s=input()
word=s.split(" ")
unique=set(word)
print(list(unique))
# 11. Symmetric Difference : Given two sets of integers, print elements that are in one set or the other, but not both.
set1 = set(map(int, input("Enter elements: ").split()))
set2 = set(map(int, input("Enter elements: ").split()))

diff = set1 ^ set2
print("Symmetric difference:", diff)


# 12. Subset Checker:
set1 = set(map(int, input("Enter elements: ").split()))
set2 = set(map(int, input("Enter elements: ").split()))

if set1.issubset(set2):
    print("set 1 is subset of set 2")
else:
    print("set 1 is not subset of set 2")
