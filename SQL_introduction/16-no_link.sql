-- tasak:16
SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
ORDER BY score DESC;