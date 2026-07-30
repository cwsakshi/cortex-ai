-- Day 22 - Week 1 - Unified Placement Prep Schedule
-- Topic: SQL Window Functions (RANK, PARTITION BY)
-- Task: Top 3 employees by total sales, per region

SELECT * FROM (
    SELECT employee, region, SUM(amount) AS total_sales,
           RANK() OVER (PARTITION BY region ORDER BY SUM(amount) DESC) AS rnk
    FROM sales
    GROUP BY employee, region
) ranked
WHERE rnk <= 3;
