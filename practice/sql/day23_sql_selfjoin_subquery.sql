-- Day 23 - Week 1 - Unified Placement Prep Schedule
-- Topic: Self-Joins + Subqueries

-- 1. Employees who earn more than their manager (self-join)
SELECT e.name AS employee, m.name AS manager, e.salary AS emp_salary, m.salary AS mgr_salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;

-- 2. Employees who earn more than the company-wide average salary (subquery)
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 3. Departments whose total salary spend is greater than the average
--    department-wise total salary spend (nested subquery)
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > (
    SELECT AVG(dept_total)
    FROM (
        SELECT SUM(salary) AS dept_total
        FROM employees
        GROUP BY department
    ) dept_totals
);
