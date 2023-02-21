-- displays the average temperature (in fahrenheit) by city ordered by temperature( descending order)

SELECT DISTINCT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
