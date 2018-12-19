-- How many payment transactions were greater than $5?
SELECT COUNT(amount) FROM payment WHERE amount > 5;

-- How many actors have a first name that starts with P?
SELECT COUNT(first_name) FROM actor WHERE first_name LIKE 'P%';

-- How many unique districts are our customers from?
SELECT COUNT(DISTINCT(district)) FROM address;

-- Retrieve the list of names for the distinct districts
SELECT DISTINCT(district) FROM address;

-- How many films have a rating of R and a replacement cost between $5 and $15?
SELECT COUNT(*) FROM film WHERE rating = 'R' AND replacement_cost BETWEEN 5 and 15;

-- How many films contain the word Truman in their title?
SELECT COUNT(title) FROM film WHERE title LIKE '%Truman%'