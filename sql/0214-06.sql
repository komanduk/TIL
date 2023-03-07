-- SHOW COLUMNS FROM users
-- 문제 1
-- CREATE TABLE users (
-- 	userid INT AUTO_INCREMENT ,
--     fist_name VARCHAR(20) NOT NULL,
--     last_name VARCHAR(20) NOT NULL,
--     birthday DATE NOT NULL,
--     city VARCHAR(100) DEFAULT NULL,
--     country VARCHAR(100) DEFAULT NULL,
--     email VARCHAR(100) DEFAULT NULL,
--     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
--     PRIMARY KEY (userid)
-- );

-- 문제 2
-- INSERT INTO users (fist_name, last_name, birthday, city, country, email)
-- VALUES
-- ('Beemo', 'Jeong', '1000-01-01', '', '', 'beemo@hphk.kr'),
-- ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', ''),
-- ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', ''),
-- ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', '');

-- 문제 3
-- INSERT INTO users (fist_name, last_name, city, birthday)
-- VALUES
-- ('Tee', 'Mo', 'Seoul', '1000-01-01'),
-- ('Twisted', 'Fate', 'Jeju', '1000-01-01'),
-- ('Kog', 'Maw', 'Busan', '1000-01-01'),
-- ('Kha', 'Zix', 'Seoul', '1000-01-01'),
-- ('Xin', 'Zhao', 'Seoul', '1000-01-01');

-- 문제 4
-- UPDATE users SET fist_name = '영진', last_name = '고', birthday = '1994-01-18' WHERE userid = 2; 

-- 문제 5
-- UPDATE users SET country = 'Korea' WHERE (country IS NULL);

-- 문제 6
-- DELETE FROM users WHERE fist_name = 'Beemo';

-- 문제 7
-- DELETE FROM users WHERE fist_name = 'Kwangsoo' AND last_name = 'Lee' ;

-- 문제 8
-- DELETE FROM users ORDER BY created_at DESC LIMIT  1;