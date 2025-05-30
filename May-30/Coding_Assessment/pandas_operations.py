
# Q14. Load both employees.csv and projects.csv using Pandas.

import pandas as pd

employees = pd.read_csv("employees.csv")
projects=pd.read_csv("projects.csv")

print(employees.head())
print(projects.head())

# Q15. Display:
# First 2 rows of employees

print(employees.head(2))

# Unique values in the Department column

print("Unique departments:", employees['Department'].unique())

# Average salary by department

avg_salary_dept = employees.groupby("Department")["Salary"].mean()
print(avg_salary_dept)

# Q16. Add a column TenureInYears = current year - joining year.

from datetime import datetime

employees["JoiningDate"] = pd.to_datetime(employees["JoiningDate"])

curr_year = datetime.now().year
employees["TenureInYears"] = curr_year - employees["JoiningDate"].dt.year

print(employees)

#  Section 7: Data Filtering, Aggregation, and Sorting
# Q17. From employees.csv , filter all IT department employees with salary > 60000.

res = employees[(employees['Department'] == 'IT') & (employees['Salary'] > 60000)]
print("IT dept with salary > 60000:\n", res)

# Q18. Group by Department and get:
# Count of employees
# Total Salary
# Average Salary

grouped = employees.groupby('Department').agg(
    EmpCount=('EmployeeID', 'count'),
    TotalSalary=('Salary', 'sum'),
    AverageSalary=('Salary', 'mean')
)

print(grouped)

# Q19. Sort all employees by salary in descending order.

sort = employees.sort_values(by='Salary', ascending=False)
print("Employees sorted",sort)

#  Section 8: Joins & Merging

# Q20. Merge employees.csv and projects.csv on EmployeeID to show project
# allocations.

merged = pd.merge(employees, projects, on='EmployeeID')
print(merged)

# Q21. List all employees who are not working on any project (left join logic).

join= pd.merge(employees, projects, on='EmployeeID', how='left')

no_proj = join[join['ProjectID'].isna()]
print("Employees without projects:\n", no_proj[['EmployeeID', 'Name', 'Department', 'Salary']])

# Q22. Add a derived column TotalCost = HoursAllocated * (Salary / 160) in the merged
# dataset

merged = merged.dropna(subset=['HoursAllocated'])

merged['TotalCost'] = merged['HoursAllocated'] * (merged['Salary'] / 160)

print("Dataset with TotalCost:\n", merged[['EmployeeID', 'Name', 'ProjectName', 'HoursAllocated', 'TotalCost']])
