WITH ranking AS (
SELECT b.name as Department, a.name as Employee, a.salary as Salary, DENSE_RANK() OVER (partition by departmentId order by salary desc) as rnk
FROM Employee a
JOIN Department b
ON a.departmentId = b.id
)

SELECT Department, Employee, Salary
FROM ranking
WHERE rnk <= 3