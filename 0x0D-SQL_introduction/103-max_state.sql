-- displays the max temperature of each state
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY MAX(value) DESC
LIMIT 3;
