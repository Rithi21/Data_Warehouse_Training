# 13. Frequency Counter: Count the frequency of each character in a string using a dictionary.
s=input()
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("Frequency count:",freq)

# 14. Student Grade Book Ask for names and marks of 3 students. Then ask for a name and display their grade ( >=90: A , >=75: B , else C).
students = {}

for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks for {name}: "))
    students[name] = marks


name_for_grade = input("Enter name to check grade: ")

if name_for_grade in students:
    marks = students[name_for_grade]
    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    else:
        grade = 'C'
    print(f"{name_for_grade} has grade {grade}")
else:
    print("Student not found.")

# 15. Merge Two Dictionaries. If the same key exists, sum the values.

dict1 = {"a": 3, "b": 2}
dict2 = {"b": 5, "c": 8}

merge = dict1.copy()
for key, value in dict2.items():
    if key in merge:
        merge[key] += value
    else:
        merge[key] = value

print("Merged Dictionary:", merge)

# 16. Invert a dictionary’s keys and values. Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"}

d = {"a": 1, "b": 2}
invert={}
for key, value in d.items():
    invert[value]=key
print("New inverted Dictionary:", invert)

# 17. Group Words by Length Input a list of words. Create a dictionary where the key is word length and the value is a list of words of that length

words = input("Enter words: ").split()

res= {}
for word in words:
    l = len(word)
    if l in res:
        res[l].append(word)
    else:
        res[l] = [word]

print("Grouped by word length:", res)
