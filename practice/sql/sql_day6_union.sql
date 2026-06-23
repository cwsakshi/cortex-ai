-- SQL Day 6 — UNION

-- Table: employees
-- | id | name    | department | salary |
-- |----|---------|------------|--------|
-- | 1  | Sakshi  | AI         | 50000  |
-- | 2  | Rahul   | Data       | 45000  |
-- | 3  | Priya   | AI         | 55000  |
-- | 4  | Amit    | Data       | 40000  |
-- | 5  | Neha    | AI         | 60000  |

-- UNION combines results from two queries into one result set
-- Automatically removes duplicates

-- Example: Find names who are in AI department OR earn more than 55000
SELECT name FROM employees WHERE department = 'AI'
UNION
SELECT name FROM employees WHERE salary > 55000;
-- Result: Sakshi, Priya, Neha (Neha appears once even though she matches both)

-- Problem: Find names who are in Data department OR earn less than 45000
SELECT name FROM employees WHERE department = 'Data'
UNION
SELECT name FROM employees WHERE salary < 45000;
-- Result: Rahul, Amit

-- Key concepts learned:
-- UNION = combines two queries, removes duplicate rows automatically
-- UNION ALL = same thing but KEEPS duplicates
-- Both queries in a UNION must have the same number of columns
