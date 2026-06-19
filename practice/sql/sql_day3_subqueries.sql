-- SQL Day 3 — Subqueries

-- A subquery is a query inside another query
-- Inner query runs first → returns a value → outer query uses it

-- Table: employees
-- | id | name    | department | salary |
-- |----|---------|------------|--------|
-- | 1  | Sakshi  | AI         | 50000  |
-- | 2  | Rahul   | Data       | 45000  |
-- | 3  | Priya   | AI         | 55000  |
-- | 4  | Amit    | Data       | 40000  |
-- | 5  | Neha    | AI         | 60000  |

-- Problem 1: Find employees who earn more than average salary
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
-- Subquery returns: 50000
-- Result: Priya (55000), Neha (60000)

-- Problem 2: Find employee with highest salary
SELECT name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
-- Result: Neha (60000)

-- Problem 3: Find all employees in same department as Sakshi
SELECT name, department
FROM employees
WHERE department = (SELECT department FROM employees WHERE name = 'Sakshi');
-- Subquery returns: 'AI'
-- Result: Sakshi, Priya, Neha

-- Problem 4: Find employees NOT in the highest paying department
SELECT name, department
FROM employees
WHERE department NOT IN (
    SELECT department
    FROM employees
    GROUP BY department
    ORDER BY AVG(salary) DESC
    LIMIT 1
);
-- Subquery returns: 'AI' (highest avg salary dept)
-- Result: Rahul (Data), Amit (Data)

-- Key concepts:
-- Subquery runs BEFORE the outer query
-- Can't use AVG() directly in WHERE — use subquery instead
-- NOT IN excludes rows matching subquery result
-- LIMIT 1 returns only the top result
-- Always use single quotes for text values: 'Sakshi' not "Sakshi"
