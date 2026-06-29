-- SQL Day 10 — CTEs (Common Table Expressions)

-- A CTE is a temporary, named result set you can reference within a query.
-- Breaks complex queries into clean, readable steps instead of nested subqueries.

-- WITH cte_name AS (
--     SELECT ...
-- )
-- SELECT * FROM cte_name;

-- Table: employees
-- | id | name    | department | salary |
-- |----|---------|------------|--------|
-- | 1  | Sakshi  | AI         | 50000  |
-- | 2  | Rahul   | Data       | 45000  |
-- | 3  | Priya   | AI         | 55000  |
-- | 4  | Amit    | Data       | 40000  |
-- | 5  | Neha    | AI         | 60000  |

-- Problem: Find employees who earn more than the AVERAGE SALARY OF THEIR OWN DEPARTMENT
-- (not company-wide average)

WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT e.name, e.department, e.salary
FROM employees e
JOIN dept_avg d ON e.department = d.department
WHERE e.salary > d.avg_salary;

-- dept_avg contains:
-- AI   -> 55000  (avg of 50000+55000+60000)
-- Data -> 42500  (avg of 45000+40000)

-- Final result:
-- Neha  (60000 > 55000) -> included
-- Priya (55000 > 55000) -> EXCLUDED (equal, not greater than)
-- Rahul (45000 > 42500) -> included
-- Sakshi (50000 > 55000) -> excluded
-- Amit (40000 > 42500) -> excluded

-- Result: Neha, Rahul

-- Key concepts learned:
-- WITH ... AS (...) creates a named, reusable temporary result set
-- CTEs make multi-step logic readable - calculate dept averages FIRST,
--   then compare each employee against THEIR OWN department's average
-- Without a CTE, you'd need a correlated subquery (messier, harder to read)
-- > excludes exact matches - watch for >= vs > depending on requirements
