SELECT request_at as Day,
CAST(SUM(CASE WHEN status <> 'completed' THEN 1 ELSE 0 END)/COUNT(*) AS DECIMAL(3,2)) as 'Cancellation Rate'
FROM Trips a
JOIN Users b
ON a.client_id = b.users_id
JOIN Users c
ON a.driver_id = c.users_id
WHERE b.banned = 'No' AND c.banned = 'No'
AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 1