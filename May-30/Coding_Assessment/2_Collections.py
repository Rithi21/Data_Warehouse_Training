
# Q4. Create a dictionary:

keys = ['a', 'b', 'c']
values = [100, 200, 300]

dict1 = dict(zip(keys, values))
print(dict1)

# Q5. From a list of employee salaries, extract:
# The maximum salary
# All salaries above average
# A sorted version in descending order

l = list(map(int, input("Enter a list of employee salaries: ").split()))

max_salary = max(l)
print("Maximum salary:", max_salary)

avg_salary = sum(l) / len(l)

above_avg = [salary for salary in l if salary > avg_salary]
print("Salaries above average:", above_avg)


sorted_desc = sorted(l, reverse=True)
print("Salaries sorted desc:", sorted_desc)
print(l)

# Q6. Create a set from a list and remove duplicates. Show the difference between two sets:

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

set1 = set(a)
set2 = set(b)

print("Set A:", set1)
print("Set B:", set2)

diff = set1 - set2
print("Difference:", diff)
