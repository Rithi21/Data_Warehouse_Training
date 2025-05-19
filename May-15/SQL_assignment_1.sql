create database product_db
use product_db

create table Product(ProductId INT PRIMARY KEY,ProductName VARCHAR(150) NOT NULL,Category VARCHAR(150) NOT NULL,Price INT NOT NULL,
StockQuantity INT,Supplier VARCHAR(100))

INSERT INTO Product(ProductId,ProductName,Category,Price,StockQuantity,Supplier) values 
(1,'Laptop','Electronics',70000,50,'TechMart'),
(2, 'Office Chair', 'Furniture', 5000, 100, 'HomeComfort'),
(3, 'Smartwatch', 'Electronics', 15000, 200, 'GadgetHub'),
(4, 'Desk Lamp', 'Lighting', 1200, 300, 'BrightLife'),
(5, 'Wireless Mouse', 'Electronics', 1500, 250, 'GadgetHub');

SELECT * from Product

--1. CRUD Operations:
--1.	Add a new product:
--Insert a product named "Gaming Keyboard" under the "Electronics" category, priced at 3500, with 150 units in stock, supplied by "TechMart".

INSERT INTO Product(ProductId,ProductName,Category,Price,StockQuantity,Supplier) values 
(6,'Gaming Keyboard','Electronics',3500,150,'TechMart')

--2.	Update product price:
--Increase the price of all Electronics products by 10%.
UPDATE Product set Price=Price*1.10 where Category='Electronics'

--3.Delete a product:
--Remove the product with the ProductID = 4 (Desk Lamp).
DELETE FROM Product where ProductId=4

--4.Read all products:
--Display all products sorted by Price in descending order.
SELECT * from Product order by Price DESC

--2. Sorting and Filtering:
--5.	Sort products by stock quantity:
--Display the list of products sorted by StockQuantity in ascending order.
SELECT * from Product order by StockQuantity ASC

--6.	Filter products by category:
--List all products belonging to the Electronics category.
SELECT * from Product where Category='Electronics'

--7.	Filter products with AND condition:
--Retrieve all Electronics products priced above 5000.
SELECT * from Product where Category = 'Electronics' and Price > 5000

--8.	Filter products with OR condition:
--List all products that are either Electronics or priced below 2000
SELECT * from Product where Category='Electronics' or Price < 2000

--3. Aggregation and Grouping:

--9.	Calculate total stock value: Find the total stock value (Price * StockQuantity) for all products.
SELECT SUM(Price * StockQuantity) as 'Total Stock Value' from PRODUCT

--10.	Average price of each category: Calculate the average price of products grouped by Category.
SELECT Category,ROUND(AVG(Price),2) as Average_Price from Product group by Category

--11.	Total number of products by supplier: Count the total number of products supplied by GadgetHub.
SELECT COUNT(ProductId) as Total_Product_GadgetHub  from Product where supplier='GadgetHub' 

--4. Conditional and Pattern Matching:

--12.	Find products with a specific keyword: Display all products whose ProductName contains the word "Wireless".
SELECT * from Product where ProductName LIKE '%Wireless%'

--13.	Search for products from multiple suppliers: Retrieve all products supplied by either TechMart or GadgetHub. 
SELECT * from Product where Supplier IN ('TechMart','GadgetHub')

--14.	Filter using BETWEEN operator: List all products with a price between 1000 and 20000.
SELECT * from Product where Price between 1000 and 20000

--5. Advanced Queries:
--15.	Products with high stock:Find products where StockQuantity is greater than the average stock quantity.
SELECT * from Product where  StockQuantity > (Select AVG(StockQuantity) from Product)


--16.	Get top 3 expensive products: Display the top 3 most expensive products in the table.
SELECT TOP 3 * from Product order by Price desc

--17.	Find duplicate supplier names: Identify any duplicate supplier names in the table.
SELECT Supplier, COUNT(*) AS ProductCount from Product group by Supplier
HAVING COUNT(*) > 1;

--18.	Product summary:
--Generate a summary that shows each Category with the number of products and the total stock value.
SELECT Category,COUNT(*) as Number_of_Products,SUM(Price*StockQuantity) as Total_Stock_Value 
from Product group by Category


--6. Join and Subqueries (if related tables are present):
--19.	Supplier with most products:

SELECT TOP 1 Supplier, COUNT(*) AS MAX_ProductCount FROM Product
group by Supplier order by Max_ProductCount DESC;

--20.	Most expensive product per category:

SELECT p.* FROM Product p
where Price = (SELECT MAX(Price) from Product where Category = p.Category);






