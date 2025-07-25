-- Create user_0d_1 with root-like ALL privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Create database user_2_db if not exists (needed for user_0d_2 privileges)
CREATE DATABASE IF NOT EXISTS user_2_db;

-- Create user_0d_2 with SELECT and INSERT privileges on user_2_db
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Apply privilege changes immediately
FLUSH PRIVILEGES;

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
