-- 문제1 
-- SELECT productCode,productName, MSRP FROM products WHERE MSRP > (SELECT AVG(MSRP) FROM products) ORDER BY MSRP ;

-- 문제2
-- SELECT orderDate FROM orders WHERE orderDate >= '2003-01-06' AND orderDate <= '2003-03-26'; 기간 조회
-- SELECT customerNumber, customerName
-- FROM customers
--  FROM (
-- 	SELECT t1.customerNumber, customerName, orderDate
--     FROM customers AS t1
--     INNER JOIN orders AS t2
--     on t1.customerNumber = t2.customerNumber) AS findNumber
-- WHERE orderDate IN (SELECT orderDate FROM orders WHERE orderDate >= '2003-01-06' AND orderDate <= '2003-03-26') ORDER BY customerNumber;

-- 문제 3
-- SELECT productCode , productName , productLine , MSRP FROM products WHERE productLine = 'Classic Cars' ORDER BY MSRP DESC LIMIT 1

-- 문제 4
-- SELECT customerNumber , customerName , country FROM customers WHERE country = (SELECT MAX(country) FROM customers);

-- 문제 5
-- SELECT customers.customerNumber, customers.customerName, count(orderNumber) AS order_count
-- FROM customers
-- INNER JOIN orders ON customers.customerNumber = orders.customerNumber
-- GROUP BY customers.customerNumber
-- ORDER BY count(orderNumber) DESC LIMIT 1

-- 문제 6
-- SELECT productCode , productName
-- FROM products
-- NATURAL JOIN orders
-- NATURAL JOIN orderdetails
-- WHERE orderDate >= '2004-01-01' AND orderDate <= '2004-12-31'
-- GROUP BY productCode
-- ORDER BY productCode DESC;
