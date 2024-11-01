--
SELECT c.id, c.name
FROM cities c, states s
WHERE s.name = 'California' AND c.state_id = s.id
ORDER BY c.id ASC;