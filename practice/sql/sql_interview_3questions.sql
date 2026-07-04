-- SQL Interview Practice — 3 Questions

-- Table: employees
-- | id | name    | department | salary | join_date  | manager_id |
-- |----|---------|------------|--------|------------|------------|
-- | 1  | Sakshi  | AI         | 50000  | 2026-01-10 | NULL       |
-- | 2  | Rahul   | Data       | 45000  | 2025-11-15 | 1          |
-- | 3  | Priya   | AI         | 55000  | 2026-05-01 | 1          |
-- | 4  | Amit    | Data       | 40000  | 2025-08-20 | NULL       |
-- | 5  | Neha    | AI         | 60000  | 2025-10-05 | 1          |

-- Question 1: Second highest salary (without LIMIT/OFFSET)
SELECT MAX(salary) AS second_highest_sal
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
-- Result: 55000 (Priya's salary)

-- Question 2: Employees with more than 180 days at company
SELECT name, DATEDIFF('2026-07-01', join_date) AS days_employed
FROM employees
WHERE DATEDIFF('2026-07-01', join_date) > 180;
-- Key fix: can't use alias in WHERE, must repeat the DATEDIFF expression
-- Key fix: date must be in quotes '2026-07-01', full 4-digit year required

-- Question 3: Salary rank within each department (highest = rank 1)
SELECT name, department, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept
FROM employees;

-- Common mistakes to avoid:
-- 1. Using alias in WHERE clause (alias is created in SELECT, runs after WHERE)
-- 2. Forgetting quotes around date strings
-- 3. Using short year format '26-07-01' instead of '2026-07-01'
