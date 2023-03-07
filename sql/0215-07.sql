-- 문제 1

-- SELECT employeeNumber, lastName, firstName, city FROM employees INNER JOIN offices ON employees.officeCode = offices.officeCode ORDER BY employeeNumber;

-- 문제 2
-- SELECT customerNumber , officeCode, customers.city, offices.city FROM customers LEFT JOIN offices ON customers.city = offices.city ORDER BY customerNumber DESC;

-- 문제 3
-- SELECT customerNumber , officeCode, customers.city, offices.city FROM customers RIGHT JOIN offices ON customers.city = offices.city ORDER BY customerNumber DESC;

-- 문제 4
-- SELECT customerNumber , officeCode, customers.city, offices.city FROM customers INNER JOIN offices ON customers.city = offices.city ORDER BY customerNumber DESC;

-- 문제 5
-- 2번 쿼리문은 customers 와 offices 테이블의 서로 겹치는 값만 출력하지만 3번은 서로겹치면서 customers 의 값도 출력한다. 단 offices 에 없는값들은 NULL 로 표시된다. 4번은 3번의 반대

-- 문제 6
-- SELECT customerNumber , officeCode, customers.city, offices.city FROM customers LEFT JOIN offices ON customers.city = offices.city
-- UNION
-- SELECT customerNumber , officeCode, customers.city, offices.city FROM customers RIGHT JOIN offices ON customers.city = offices.city
-- ORDER BY customerNumber DESC;

-- 문제 7

-- SELECT orderdetails.orderNumber, orderDate FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber ORDER BY orderNumber;

-- 문제 8
-- SELECT orderNumber , orderdetails.productCode , productName FROM orderdetails INNER JOIN products ON orderdetails.productCode = products.productCode ORDER BY orderNumber ;

-- 문제 9
-- SELECT orderdetails.orderNumber , orderdetails.productCode , orderDate, productName FROM orderdetails LEFT JOIN orders ON orderdetails.orderNumber = orders.orderNumber JOIN products ON orderdetails.productCode = products.productCode ORDER BY orderNumber;
