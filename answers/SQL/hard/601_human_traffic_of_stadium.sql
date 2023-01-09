-- Init

WITH data AS (
SELECT  (id - LAG(id,2) OVER ()) as p2,
        id - LAG(id,1) OVER () as p1,
        id,
        LEAD(id,1) OVER () -id as n1,
        LEAD(id,2) OVER () -id as n2,
        visit_date,
        people
FROM Stadium
WHERE people >= 100
)

SELECT id, visit_date, people
FROM data
WHERE (p2 = 2 AND p1 = 1) OR (p1=1 AND n1=1) OR (n1=1 AND n2=2)

-- Revision 1

WITH data AS (
SELECT  LAG(id,2) OVER () = id - 2 as p2,
        LAG(id,1) OVER () = id - 1 as p1,
        id,
        LEAD(id,1) OVER () = id + 1 as n1,
        LEAD(id,2) OVER () = id + 2 as n2,
        visit_date,
        people
FROM Stadium
WHERE people >= 100
)

SELECT id, visit_date, people
FROM data
WHERE (p2 AND p1) OR (p1 AND n1) OR (n1 AND n2)