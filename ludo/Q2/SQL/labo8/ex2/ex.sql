--1
--Requête avec jointure :
SELECT DISTINCT c.CompanyName, c.Address
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN Employees e ON o.EmployeeID = e.EmployeeID
WHERE e.LastName = 'Callahan' AND YEAR(o.OrderDate) = 2009
ORDER BY c.CompanyName;
--Requête avec requête imbriquée :
SELECT DISTINCT CompanyName, Address
FROM Customers
WHERE CustomerID IN (
  SELECT DISTINCT o.CustomerID
  FROM Orders o
  INNER JOIN Employees e ON o.EmployeeID = e.EmployeeID
  WHERE e.LastName = 'Callahan' AND YEAR(o.OrderDate) = 2009
)
ORDER BY CompanyName;

--2
--Requête avec jointure :
SELECT DISTINCT c.CompanyName
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN OrderDetails od ON o.OrderID = od.OrderID
INNER JOIN Products p ON od.ProductID = p.ProductID
INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE c.City = 'Paris'
ORDER BY c.CompanyName;
--Requête avec requête imbriquée :
SELECT DISTINCT CompanyName
FROM Suppliers
WHERE SupplierID IN (
  SELECT DISTINCT p.SupplierID
  FROM Products p
  INNER JOIN OrderDetails od ON p.ProductID = od.ProductID
  INNER JOIN Orders o ON od.OrderID = o.OrderID
  INNER JOIN Customers c ON o.CustomerID = c.CustomerID
  WHERE c.City = 'Paris'
)
ORDER BY CompanyName;

--3
--Requête avec jointure :
SELECT e1.FirstName || ' ' || e1.LastName AS EmployeeName, e2.FirstName || ' ' || e2.LastName AS SupervisorName
FROM Employees e1
INNER JOIN Employees e2 ON e1.ReportsTo = e2.EmployeeID
ORDER BY EmployeeName;
--Requête avec requête imbriquée :
SELECT FirstName || ' ' || LastName AS EmployeeName, (
  SELECT FirstName || ' ' || LastName
  FROM Employees
  WHERE EmployeeID = e.ReportsTo
) AS SupervisorName
FROM Employees e
WHERE ReportsTo IS NOT NULL
ORDER BY EmployeeName;
