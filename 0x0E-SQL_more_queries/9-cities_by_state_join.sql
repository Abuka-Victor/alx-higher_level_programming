-- list cities in a db
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.states_id 
ORDER BY cities.id ASC;
