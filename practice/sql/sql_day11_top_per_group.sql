-- SQL Day 11 — Find Top Performer Per Group (CTE pattern)

-- Table: employees
-- | id | name    | department | salary | manager_id |
-- |----|---------|------------|--------|------------|
-- | 1  | Sakshi  | AI         | 50000  | NULL       |
-- | 2  | Rahul   | Data       | 45000  | 1          |
-- | 3  | Priya   | AI         | 55000  | 1          |
-- | 4  | Amit    | Data       | 40000  | NULL       |
-- | 5  | Neha    | AI         | 60000  | 1          |

-- Problem: Find each department's HIGHEST-PAID employee using a CTE

WITH dept_max AS (
    SELECT department, MAX(salary) AS max_salary
    FROM employees
    GROUP BY department
)
SELECT e.name, e.department, e.salary
FROM employees e
JOIN dept_max d ON e.department = d.department
WHERE e.salary = d.max_salary;

-- Result:
-- Neha  | AI   | 60000  (highest in AI)
-- Rahul | Data | 45000  (highest in Data)

-- Key concepts learned:
-- IS / IS NOT is ONLY for NULL comparisons (IS NULL, IS NOT NULL)
-- For comparing two regular values, always use = (equality), not IS
-- WHERE salary = max_salary -> the highest-paid person's salary EQUALS the
--   group's max (they ARE the max), not greater than it
-- This "find top performer per group" pattern is a very common interview
--   question - same CTE structure works for: highest score per class,
--   best-selling product per category, most recent order per customer
