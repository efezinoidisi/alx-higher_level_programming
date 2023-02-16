-- lists all cities in the database hbtn_0d_usa
-- it displays the id, name from cities table and name from states table

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;