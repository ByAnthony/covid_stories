DROP TABLE memories;
DROP TABLE contributors;
DROP TABLE charities;

CREATE TABLE contributors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    profession VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE charities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    website VARCHAR(255)
);

CREATE TABLE memories (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    contributor_id INT REFERENCES contributors(id) ON DELETE CASCADE,
    account VARCHAR(255),
    date DATE,
    charity_id INT REFERENCES charities(id) ON DELETE CASCADE
);