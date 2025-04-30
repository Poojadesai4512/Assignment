-- a) Total amount spent by each customer
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id;

-- b) Orders placed after '2023-01-03'
SELECT * 
FROM orders
WHERE order_date > '2023-01-03';

-- c) Customers with more than one order
SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1;
