-- SQL Day 9 — LAG and LEAD Window Functions

-- Table: employees
-- | id | name    | salary |
-- |----|---------|--------|
-- | 1  | Sakshi  | 50000  |
-- | 2  | Rahul   | 45000  |
-- | 3  | Priya   | 55000  |
-- | 4  | Amit    | 40000  |

-- LAG()  -> looks at the PREVIOUS row's value (based on ORDER BY)
-- LEAD() -> looks at the NEXT row's value (based on ORDER BY)

SELECT name, salary,
       LAG(salary) OVER (ORDER BY id) AS prev_salary,
       LEAD(salary) OVER (ORDER BY id) AS next_salary
FROM employees;

-- Result:
-- name   | salary | prev_salary | next_salary
-- Sakshi | 50000  | NULL        | 45000
-- Rahul  | 45000  | 50000       | 55000
-- Priya  | 55000  | 45000       | 40000
-- Amit   | 40000  | 55000       | NULL

-- Key concepts learned:
-- LAG/LEAD let you compare a row to its NEIGHBOR without writing a self-join
-- First row's prev_salary is always NULL (nothing comes before it)
-- Last row's next_salary is always NULL (nothing comes after it)
-- Real-world use: month-over-month sales growth, day-over-day price change,
--   year-over-year comparisons, detecting trends between consecutive records
-- Don't forget the comma between multiple SELECT columns!
