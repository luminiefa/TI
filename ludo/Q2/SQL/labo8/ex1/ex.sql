--1
--Avec une jointure :
SELECT Orders.OrderID, Orders.OrderDate
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Customers.City = 'London';
--Avec une requête imbriquée :
SELECT OrderID, OrderDate
FROM Orders
WHERE CustomerID IN (
    SELECT CustomerID
    FROM Customers
    WHERE City = 'London'
);

--2
--Avec une jointure :
SELECT Products.ProductName, Products.Price
FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
WHERE Categories.CategoryName = 'Desserts'
ORDER BY Products.ProductName ASC;
--Avec une requête imbriquée :
SELECT ProductName, Price
FROM Products
WHERE CategoryID = (
    SELECT CategoryID
    FROM Categories
    WHERE CategoryName = 'Desserts'
)
ORDER BY ProductName ASC;

--3
--Avec une jointure :
SELECT Employees.FirstName, Employees.LastName, Employees.Title, Employees.Salary
FROM Employees
JOIN Employees AS Managers ON Employees.ReportsTo = Managers.EmployeeID
WHERE Managers.LastName = 'Fuller';
--Avec une requête imbriquée :
SELECT FirstName, LastName, Title, Salary
FROM Employees
WHERE ReportsTo = (
    SELECT EmployeeID
    FROM Employees
    WHERE LastName = 'Fuller'
);
