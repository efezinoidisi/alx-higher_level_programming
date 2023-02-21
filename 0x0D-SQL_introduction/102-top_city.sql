-- displays the top 3 cities temperature during july and august ordered by temperature( descending order)

SELECT DISTINCT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
