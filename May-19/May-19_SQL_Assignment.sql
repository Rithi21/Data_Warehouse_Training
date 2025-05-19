CREATE TABLE EmployeeAttendance (
    AttendanceID INT PRIMARY KEY,EmployeeName VARCHAR(100),Department VARCHAR(75),Date DATE,
	Status VARCHAR(50),HoursWorked INT)

INSERT INTO EmployeeAttendance VALUES
(1,'John Doe','IT','2025-05-01', 'Present', 8),
(2,'Priya Singh','HR','2025-05-01', 'Absent', 0),
(3,'Ali Khan','IT','2025-05-01', 'Present', 7),
(4,'Riya Patel','Sales','2025-05-01', 'Late', 6),
(5,'David Brown','Marketing','2025-05-01', 'Present', 8);

--1. CRUD Operations:

--1.	Add a new attendance record:

INSERT INTO EmployeeAttendance VALUES (6,'Neha Sharma','Finance','2025-05-01', 'Present', 8)


--2.	Update attendance status: Change Riya Patel's status from Late to Present.

UPDATE EmployeeAttendance set Status = 'Present' 
where EmployeeName = 'Riya Patel' AND Date = '2025-05-01';

--3.	Delete a record:

Delete from EmployeeAttendance where EmployeeName='Priya Singh' AND Date = '2025-05-01';

--4.	Read all records:

SELECT * from EmployeeAttendance ORDER BY EmployeeName ASC;

--2. Sorting and Filtering:

--5.	Sort by Hours Worked:

SELECT * from EmployeeAttendance ORDER BY HoursWorked DESC;

--6.	Filter by Department: Display all attendance records for the IT department.

SELECT * from EmployeeAttendance where Department = 'IT'

--7.	Filter with AND condition: List all Present employees from the IT department.

SELECT * from EmployeeAttendance where Department = 'IT' AND Status='Present'

--8.	Filter with OR condition: Retrieve all employees who are either Absent or Late.

SELECT * from EmployeeAttendance where Status='Absent' OR Status = 'Late';


--3. Aggregation and Grouping:
--9.	Total Hours Worked by Department:

SELECT Department, SUM(HoursWorked) as Total_Hours from EmployeeAttendance
GROUP BY Department

--10.	Average Hours Worked: Find the average hours worked per day across all departments.

SELECT AVG(HoursWorked) as Average_Hours_Worked from EmployeeAttendance;

--11.	Attendance Count by Status: Count how many employees were Present, Absent, or Late

SELECT Status, COUNT(*) as Attendance_Count from EmployeeAttendance
GROUP BY Status;

--4. Conditional and Pattern Matching:

--12.	Find employees by name prefix: List all employees whose EmployeeName starts with 'R'.

SELECT * from EmployeeAttendance where EmployeeName LIKE 'R%';

--13.	Filter by multiple conditions: Display employees who worked more than 6 hours and are marked Present.

SELECT * from EmployeeAttendance where HoursWorked > 6 AND Status = 'Present';

--14.	Filter using BETWEEN operator:

SELECT * from EmployeeAttendance where HoursWorked BETWEEN 6 AND 8;

--5. Advanced Queries:

--15.	Top 2 employees with the most hours: Display the top 2 employees with the highest number of hours worked.

SELECT TOP 2 * from EmployeeAttendance ORDER BY HoursWorked DESC

--16.	Employees who worked less than the average hours:

SELECT * from EmployeeAttendance 
where HoursWorked < (SELECT AVG(HoursWorked) from EmployeeAttendance)

--17.	Group by Status: Calculate the average hours worked for each attendance status (Present, Absent, Late).

SELECT Status,AVG(HoursWorked) as Average_Hours from EmployeeAttendance GROUP BY Status

--18.	Find duplicate entries: Identify any employees who have multiple attendance records on the same date.

SELECT EmployeeName,Date, COUNT(*) as Multiple_Attendance
from EmployeeAttendance 
GROUP BY EmployeeName, Date Having COUNT(*) > 1;

--6. Join and Subqueries (if related tables are present):

--19.	Department with most Present employees: Find the department with the highest number of Present employees.

SELECT TOP 1 Department, Present_count from (
    SELECT Department, COUNT(*) AS Present_count from EmployeeAttendance 
    where Status = 'Present'
    GROUP BY Department
)as Dept_Counts
ORDER BY Present_count DESC;

--20.	Employee with maximum hours per department: Find the employee with the most hours worked in each department.

SELECT ea.* from
EmployeeAttendance ea
JOIN (
    SELECT Department, MAX(HoursWorked) AS Max_Hours
	from EmployeeAttendance
    GROUP BY Department
) as Dept
ON ea.Department = Dept.Department AND ea.HoursWorked = Dept.Max_Hours;




