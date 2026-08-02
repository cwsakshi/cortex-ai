-- Day 24 (SQL Day 14) - Unified Placement Prep Schedule
-- Topic: Multi-table joins + aggregation

-- Department with the highest average salary
SELECT d.dept_name, AVG(e.salary) AS Avg_salary
FROM employees e
JOIN departments d
ON d.id = e.department_id
GROUP BY d.dept_name
ORDER BY Avg_salary DESC
LIMIT 1;
