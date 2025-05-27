# TUPLES
# 6. Swap Values Write a function that accepts two tuples and swaps their contents.
def swap(t1, t2):
    return t2, t1

tuple1 = (3,5,6)
tuple2 = (7,8,9)

tuple1, tuple2 = swap(tuple1, tuple2)

print("Tuple 1 after swap:", tuple1)
print("Tuple 2 after swap:", tuple2)

# 7. Unpack Tuples Unpack a tuple with student details: (name, age, branch, grade) and print them in a sentence.
student=("Rahul",20,"CSE","A")
name,age,branch,grade=student

print(f"{name} is {age} years old, studying {branch} with grade {grade}.")

# 8. Tuple to Dictionary Convert a tuple of key-value pairs into a dictionary.
# Example: (("a", 1), ("b", 2)) → {"a": 1, "b": 2}

tuple1 = (("a", 1), ("b", 2), ("c", 3))

res = dict(tuple1)
print("Converted dictionary:", res)
