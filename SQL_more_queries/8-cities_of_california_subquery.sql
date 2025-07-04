-- Write a script that lists all the cities of California from the database hbtn_0d_usa.
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California") GROUP BY id ORDER BY id ASC;