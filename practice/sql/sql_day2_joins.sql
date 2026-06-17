-- SQL Day 2 — JOINs

-- Tables used:
-- customers: id, name
-- orders: id, customer_id, amount

-- INNER JOIN — only matching rows
SELECT c.name, o.amount
FROM customers AS c
INNER JOIN orders AS o ON c.id = o.customer_id;

-- LEFT JOIN — all customers even without orders
SELECT c.name, o.amount
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id;

-- Problem 1: Find all customers and their order amounts
-- Include customers who have never ordered
SELECT c.name, o.amount
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id;

-- Problem 2: Find customers who have NEVER placed an order
SELECT c.name
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id
WHERE o.customer_id IS NULL;

-- Problem 3: Total amount spent by each customer
SELECT c.name, SUM(o.amount) AS total_amount_spent
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id
GROUP BY c.name;

-- Problem 4: Customers who spent more than 500 in total
SELECT c.name, SUM(o.amount) AS total_spent
FROM customers AS c
LEFT JOIN orders AS o ON c.id = o.customer_id
GROUP BY c.name
HAVING total_spent > 500;

-- Key concepts:
-- INNER JOIN = only matching rows from both tables
-- LEFT JOIN  = all rows from left table + matches from right
-- RIGHT JOIN = all rows from right table + matches from left
-- IS NULL    = check for missing values (not = NULL)
-- Aliases    = AS c, AS o for shorter table names
