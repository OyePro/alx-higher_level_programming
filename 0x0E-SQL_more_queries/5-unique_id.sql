-- creating table `unique_id` with `id` and `name`
-- id is never NULL, it has a default value of 1 and it's unique

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT(1) UNIQUE,
	name VARCHAR(256)
);
