--
SELECT COUNT(*) AS number, score
FROM second_table
GROUP BY score
OREDER BY number DESC;