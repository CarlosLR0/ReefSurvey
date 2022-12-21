-- this is just a draft to start with
-- create the new user
CREATE USER new_user WITH PASSWORD 'password';

-- create the new database
CREATE DATABASE new_database;

-- grant the user permissions to the new database
GRANT ALL PRIVILEGES ON DATABASE new_database TO new_user;

-- connect to the new database
\c new_database

-- create a new table
CREATE TABLE table_name (
  column_1 datatype,
  column_2 datatype,
  ...
);

-- grant the user permissions to the new table
GRANT SELECT, INSERT, UPDATE, DELETE ON table_name TO new_user;

