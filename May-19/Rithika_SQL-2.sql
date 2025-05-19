CREATE TABLE ProductInventory (
    ProductID INT PRIMARY KEY,ProductName VARCHAR(100) NOT NULL,Category VARCHAR(50),
    Quantity INT,UnitPrice INT,Supplier VARCHAR(100),LastRestocked DATE
);

INSERT INTO ProductInventory (ProductId,ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)VALUES 
(1,'Laptop', 'Electronics',20, 70000, 'TechMart', '2025-04-20'),
(2,'Office Chair', 'Furniture',50, 5000, 'HomeComfort', '2025-04-18'),
(3,'Smartwatch', 'Electronics',30, 15000, 'GadgetHub', '2025-04-22'),
(4,'Desk Lamp', 'Lighting',80, 1200, 'BrightLife', '2025-04-25'),
(5,'Wireless Mouse', 'Electronics',100, 1500, 'GadgetHub', '2025-04-30');

--1. CRUD Operations:
-- 1.1 Add a new product

INSERT INTO ProductInventory (ProductID,ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)
VALUES (6,'Gaming Keyboard', 'Electronics', 40, 3500, 'TechMart', '2025-05-01');

-- 1.2 Update stock quantity

UPDATE ProductInventory set Quantity = Quantity + 20
where ProductName = 'Desk Lamp';

-- 1.3 Delete a discontinued product
DELETE from ProductInventory where ProductID = 2;

-- 1.4 Read all products sorted by ProductName
SELECT * from ProductInventory ORDER BY ProductName ASC;

-- 2.1 Sort by Quantity in descending order

Select * from ProductInventory ORDER BY Quantity DESC

-- 2.2 Filter by Category = 'Electronics'

SELECT * from ProductInventory where Category = 'Electronics'

-- 2.3 Filter with AND condition: Electronics with Quantity > 20

SELECT * from ProductInventory where Category = 'Electronics' AND Quantity > 20

-- 2.4 Filter with OR condition: Electronics OR UnitPrice < 2000

SELECT * from ProductInventory  where Category = 'Electronics' OR UnitPrice < 2000

--3. Aggregation and Grouping:
--9.	Total stock value calculation:

SELECT SUM(Quantity * UnitPrice) as TotalStockValue from ProductInventory

--10.	Average price by category:

SELECT Category,AVG(UnitPrice) as Average_Price from ProductInventory GROUP BY Category

--11.	Count products by supplier: Display the number of products supplied by GadgetHub.

SELECT Supplier,COUNT(*) as No_of_Products from ProductInventory where Supplier='GadgetHub' GROUP BY Supplier 

--4. Conditional and Pattern Matching:

--12.	Find products by name prefix: List all products whose ProductName starts with 'W'.
SELECT * from ProductInventory where ProductName LIKE 'W%'

--13.	Filter by supplier and price: Display all products supplied by GadgetHub with a UnitPrice above 10000.

SELECT * from ProductInventory where Supplier = 'GadgetHub' AND UnitPrice > 10000;

--14.	Filter using BETWEEN operator: List all products with UnitPrice between 1000 and 20000.

SELECT * from ProductInventory where UnitPrice BETWEEN 1000 AND 20000;

--5. Advanced Queries:

--15.	Top 3 most expensive products: Display the top 3 products with the highest UnitPrice.

SELECT TOP 3 * from ProductInventory ORDER BY UnitPrice DESC

--16.	Products restocked recently: Find all products restocked in the last 10 days.

SELECT * from ProductInventory where LastRestocked >= DATEADD(DAY, -10, GETDATE());

--17.	Group by Supplier: Calculate the total quantity of products from each Supplier.

SELECT Supplier,SUM(Quantity) as Total_Qty from ProductInventory GROUP BY Supplier

--18.	Check for low stock: List all products with Quantity less than 30.

SELECT * from ProductInventory where Quantity<30

--6. Join and Subqueries (if related tables are present):

--19.	Supplier with most products: Find the supplier who provides the maximum number of products.

SELECT TOP 1 Supplier,COUNT(*) as No_of_Products from ProductInventory 
GROUP BY Supplier ORDER BY No_of_Products DESC

--20.	Product with highest stock value:

SELECT  TOP 1 *,(Quantity * UnitPrice) as Stock_Value from ProductInventory 
ORDER BY Stock_Value DESC;

