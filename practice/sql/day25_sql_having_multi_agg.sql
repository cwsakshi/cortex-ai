-- Day 25 - Unified Placement Prep Schedule
-- Topic: HAVING + multiple aggregations

-- Departments with more than 5 employees AND average salary > 50000
SELECT department_id, COUNT(id) AS employees_indept, AVG(salary) AS Avg_salary
FROM employees
GROUP BY department_id
HAVING COUNT(id) > 5 AND AVG(salary) > 50000;
