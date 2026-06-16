-- Day 1 SQL Practice

-- Problem 1: Find all employees in AI department
SELECT name 
FROM employees 
WHERE department = 'AI';

-- Problem 2: Find employees with salary > 45000
SELECT name, salary 
FROM employees 
WHERE salary > 45000;

-- Problem 3: Sort employees by salary highest to lowest
SELECT name, salary 
FROM employees 
ORDER BY salary DESC;

-- Problem 4: Count employees in each department
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department;

-- Problem 5: Average salary per department
SELECT department, AVG(salary) AS average_sal
FROM employees 
GROUP BY department;

-- Problem 6: Departments with average salary > 50000
SELECT department, AVG(salary) AS average_sal
FROM employees 
GROUP BY department
HAVING average_sal > 50000;