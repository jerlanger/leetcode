WITH ranking as (
SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
FROM Employee
)

SELECT MAX(salary) as SecondHighestSalary
FROM ranking
WHERE rnk = 2