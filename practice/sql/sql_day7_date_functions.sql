-- SQL Day 7 — Date Functions

-- Table: employees
-- | id | name    | join_date  |
-- |----|---------|------------|
-- | 1  | Sakshi  | 2026-05-01 |
-- | 2  | Rahul   | 2025-11-15 |
-- | 3  | Priya   | 2026-01-10 |

-- Common date functions:
-- CURRENT_DATE                    -> today's date
-- DATEDIFF(date1, date2)          -> difference between two dates (in days)
-- DATE_ADD(date, INTERVAL n DAY)  -> add n days to a date
-- EXTRACT(YEAR FROM date)         -> pull out year/month/day from a date

-- Problem 1: Days each employee has been with the company (assume today = 2026-06-23)
SELECT name, DATEDIFF('2026-06-23', join_date) AS days_employed 
FROM employees;

-- Problem 2: Employees who joined in the year 2026
SELECT name, join_date 
FROM employees 
WHERE EXTRACT(YEAR FROM join_date) = 2026;
-- Result: Sakshi, Priya

-- Problem 3: Employees whose 90-day probation has already ended
SELECT name, join_date 
FROM employees 
WHERE DATE_ADD(join_date, INTERVAL 90 DAY) < '2026-06-23';

-- Key concepts learned:
-- DATEDIFF gives a number (days between dates) - useful for tenure/age calculations
-- EXTRACT() pulls a specific part (year/month/day) out of a date column
-- DATE_ADD() calculates a future date by adding an interval
-- Just calculating a date isn't enough - use WHERE to filter based on that calculation
