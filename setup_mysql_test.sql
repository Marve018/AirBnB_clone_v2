-- a script that prepares a MySQL server
-- a database hbnb_test_db
-- new user hbnb_test (in localhost)
-- the password of hbnb_test should be set to hbnb_test_pwd
-- hbnb_test should have all privileges on the database hbnb_test_db
-- hbnb_test should have SELECT privilege on the database performance_schema
-- If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
