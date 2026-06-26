-- SQL Day 8 — NULL Handling

-- Table: employees
-- | id | name    | manager_id |
-- |----|---------|------------|
-- | 1  | Sakshi  | NULL       |
-- | 2  | Rahul   | 1          |
-- | 3  | Priya   | 1          |
-- | 4  | Amit    | NULL       |

-- NULL means "no value" - different from 0 or empty string ""
-- CANNOT compare NULL using = or != . Must use IS NULL / IS NOT NULL

-- WRONG:
-- WHERE column = NULL      (never works, returns nothing)

-- CORRECT:
-- WHERE column IS NULL
-- WHERE column IS NOT NULL

-- Problem 1: Find employees who have no manager (top-level employees)
SELECT name, manager_id 
FROM employees 
WHERE manager_id IS NULL;
-- Result: Sakshi, Amit

-- COALESCE(value, default) returns value if not NULL, otherwise returns default
-- Used for DISPLAY purposes, NOT for filtering (can't filter on a COALESCE'd value
-- expecting it to change the underlying NULL)

-- Problem 2: Show each employee with their manager's name
-- Self join + LEFT JOIN + COALESCE
SELECT e1.name AS employee, COALESCE(e2.name, 'No Manager') AS manager_name
FROM employees AS e1
LEFT JOIN employees AS e2 ON e1.manager_id = e2.id;

-- Result:
-- employee | manager_name
-- Sakshi   | No Manager
-- Rahul    | Sakshi
-- Priya    | Sakshi
-- Amit     | No Manager

-- Key concepts learned:
-- NULL never equals anything, not even another NULL - must use IS NULL
-- COALESCE(col, default) - replaces NULL with a fallback value for display
-- LEFT JOIN is essential here - regular JOIN would silently DROP rows with
--   NULL manager_id, since NULL = anything is never true
-- Self join pattern: e1.manager_id = e2.id finds the MANAGER'S row,
--   not e1.manager_id = e2.manager_id (which compares wrong columns)
