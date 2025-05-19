create database book_db;

use book_db
create table Book(BookID INT PRIMARY KEY,Title VARCHAR(100),Author VARCHAR(100),Genre VARCHAR(75),Price INT,
PublishedYear INT,Stock INT)

INSERT INTO Book (BookID, Title, Author, Genre, Price, PublishedYear, Stock)VALUES
(1,'The Alchemist', 'Paulo Coelho', 'Fiction', 300, 1988, 50),
(2,'Sapiens', 'Yuval Noah Harari', 'Non-Fiction', 500, 2011, 30),
(3,'Atomic Habits', 'James Clear', 'Self-Help', 400, 2018, 25),
(4,'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Personal Finance', 350, 1997, 20),
(5,'The Lean Startup', 'Eric Ries', 'Business', 450, 2011, 15);

--1. CRUD Operations:
--1.	Add a new book: Insert a book titled "Deep Work" by Cal Newport, Genre Self-Help, Price 420, Published Year 2016, Stock 35.

INSERT INTO Book (BookID, Title, Author, Genre, Price, PublishedYear, Stock)VALUES
(6,'Deep Work','Cal Newport','Self-Help', 420, 2016, 35)

--2.	Update book price:Increase the price of all Self-Help books by 50.

UPDATE Book set Price=Price+50 where Genre='Self-Help'

--3.	Delete a book:

DELETE FROM Book where BookID=4

--4.	Read all books: Display all books sorted by Title in ascending order.

SELECT * from Book order by Title asc

--2. Sorting and Filtering:
--5.	Sort by price: List books sorted by Price in descending order.

SELECT * from Book order by Price desc;

--6.	Filter by genre: Display all books belonging to the Fiction genre.

SELECT * from Book where Genre='Fiction'

--7.	Filter with AND condition: List all Self-Help books priced above 400.

SELECT * from Book where Genre='Self-Help' AND Price>400

--8.	Filter with OR condition: Retrieve all books that are either Fiction or published after 2000.

SELECT * from Book where Genre='Fiction' OR PublishedYear > 2000

--3. Aggregation and Grouping:
--9.	Total stock value: Calculate the total value of all books in stock (Price * Stock).

SELECT SUM(Price * Stock) as Total_Stock_Value from Book

--10.	Average price by genre: Calculate the average price of books grouped by Genre.

SELECT Genre,AVG(Price) as Average_Price from Book group by Genre

--11.	Total books by author: Count the number of books written by Paulo Coelho.

SELECT COUNT(*) as Total_Books_PauloCoelho from Book where Author='Paulo Coelho'

--4. Conditional and Pattern Matching:
--12.	Find books with a keyword in title: List all books whose Title contains the word "The".

SELECT * from Book where Title LIKE '%The%'

--13.	Filter by multiple conditions: Display all books by Yuval Noah Harari priced below 600.

SELECT * from Book where Author='Yuval Noah Harari' AND Price < 600

--14.	Find books within a price range: List books priced between 300 and 500.

SELECT * from Book where Price Between 300 AND 500

--5. Advanced Queries:
--15.	Top 3 most expensive books: Display the top 3 books with the highest price.

SELECT TOP 3 * from Book ORDER BY Price DESC 

--16.	Books published before a specific year: Find all books published before the year 2000.

SELECT * from Book where PublishedYear < 2000

--17.	Group by Genre: Calculate the total number of books in each Genre.

SELECT Genre,COUNT(*) as TotalBooks_Genre from Book group by Genre

--18.	Find duplicate titles: Identify any books having the same title.

SELECT Title,COUNT(*) as BookCount from Book 
group by Title HAVING COUNT(*) > 1

--6. Join and Subqueries (if related tables are present):

--19.	Author with the most books: Find the author who has written the maximum number of books.

SELECT TOP 1 Author,COUNT(*) as Book_Count from Book 
group by Author 
ORDER BY Book_Count DESC


--20.	Oldest book by genre: Find the earliest published book in each genre.

SELECT Genre,MIN(PublishedYear) as OldestBook from Book 
group by Genre


