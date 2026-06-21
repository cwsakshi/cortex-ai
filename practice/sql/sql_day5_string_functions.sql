-- SQL Day 5 — String Functions

-- Table: users
-- | id | name      | email                  |
-- |----|-----------|------------------------|
-- | 1  | Sakshi    | sakshi@gmail.com       |
-- | 2  | rahul     | RAHUL@GMAIL.COM        |
-- | 3  | Priya     | priya@gmail.com        |

-- Common string functions:
-- UPPER(name)            -> converts to uppercase
-- LOWER(name)            -> converts to lowercase
-- LENGTH(name)           -> returns length of string
-- CONCAT(a, b)           -> joins two strings together
-- SUBSTRING(name, 1, 3)  -> extracts part of string
-- TRIM(name)             -> removes extra spaces

-- Problem 1: Find all names in uppercase
SELECT UPPER(name) FROM users;

-- Problem 2: Find the length of each email address
SELECT name, LENGTH(email) AS length_of_email FROM users;

-- Problem 3: Combine name and email into one column
SELECT CONCAT(name, ' (', email, ')') AS full_info FROM users;
-- Result: "Sakshi (sakshi@gmail.com)"

-- Problem 4: Find users whose email is NOT already lowercase
SELECT name, email FROM users WHERE email != LOWER(email);
-- Result: rahul - RAHUL@GMAIL.COM

-- Key concepts learned:
-- UPPER()/LOWER() change case of strings
-- LENGTH() returns character count
-- CONCAT() joins multiple strings together
-- Comparing a column with LOWER(column) or UPPER(column) finds case mismatches
