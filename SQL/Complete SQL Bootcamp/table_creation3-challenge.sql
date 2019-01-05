--Create a table to organize our potential leads! We will have the following information:
--A customer's first name, last name,email,sign-up date, and number of minutes spent on the dvd rental site. You should also have some sort of id tracker for them.

CREATE TABLE leads(
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email  VARCHAR(355) UNIQUE NOT NULL,
	join_date TIMESTAMP NOT NULL,
	time_spent INTEGER NOT NULL,

	CONSTRAINT customer_account_email_fkey FOREIGN KEY (email)
		REFERENCES account (email) MATCH SIMPLE
		ON UPDATE NO ACTION ON DELETE NO ACTION);