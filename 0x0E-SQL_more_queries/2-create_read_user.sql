-- creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NO EXISTS hbtn_0d_2;
CREATE USER IF NO EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
