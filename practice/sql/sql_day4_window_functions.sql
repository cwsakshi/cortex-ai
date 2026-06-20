-- SQL Day 4 — Window Functions + Self Join

-- Table: employees
-- | id | name    | department | salary |
-- |----|---------|------------|--------|
-- | 1  | Sakshi  | AI         | 50000  |
-- | 2  | Rahul   | Data       | 45000  |
-- | 3  | Priya   | AI         | 55000  |
-- | 4  | Amit    | Data       | 40000  |
-- | 5  | Neha    | AI         | 60000  |

-- ============ WINDOW FUNCTIONS ============

-- Rank employees by salary within their department
SELECT name, department, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept
FROM employees;

-- Total salary per department, shown next to every employee (no collapsing rows)
SELECT name, department, salary,
       SUM(salary) OVER (PARTITION BY department) AS dept_total
FROM employees;

-- Running total of salaries ordered by employee id
SELECT id, name, salary,
       SUM(salary) OVER (ORDER BY id) AS running_total
FROM employees;

-- ============ INTERVIEW PROBLEMS ============

-- Problem 1: Second highest salary (without LIMIT/OFFSET)
SELECT MAX(salary) AS second_highest_sal
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Problem 2: Departments with more than 2 employees
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- Problem 3: Self Join — pairs of employees in same department
SELECT e1.name AS employee1, e2.name AS employee2, e1.department
FROM employees e1
JOIN employees e2
  ON e1.department = e2.department
  AND e1.id < e2.id;

-- Problem 5: CASE statement — categorize by salary
SELECT name, salary,
  CASE
    WHEN salary > 50000 THEN 'High'
    WHEN salary >= 30000 THEN 'Medium'
    ELSE 'Low'
  END AS salary_category
FROM employees;

-- Key concepts learned:
-- PARTITION BY = mini groups, but rows are NOT collapsed (unlike GROUP BY)
-- RANK() OVER = ranking within a partition
-- SUM() OVER (ORDER BY id) = running/cumulative total
-- Self Join = joining a table to itself using two aliases (e1, e2)
-- e1.id < e2.id = avoids duplicate pairs and self-pairing
-- CASE WHEN = if-else logic inside SQL queries
