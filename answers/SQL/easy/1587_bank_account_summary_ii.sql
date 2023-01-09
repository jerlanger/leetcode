# Write your MySQL query statement below

SELECT b.name, SUM(a.amount) balance
FROM Transactions a
LEFT JOIN Users b
ON a.account = b.account
GROUP BY 1
HAVING balance > 10000