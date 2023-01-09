SELECT a.id, CASE WHEN a.p_id IS NULL THEN 'Root'
                  WHEN b.p_id IS NOT NULL THEN 'Inner'
                  WHEN b.p_id IS NULL THEN 'Leaf'
                  END as type
FROM Tree a
LEFT JOIN Tree b
ON a.id = b.p_id
GROUP BY 1,2