drop database if exists example;
create database example;
use example;
drop table if exists user;
create table user( id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255));
insert into user values(1,'nikita');

drop database if exists sample;
create database sample;
use sample;
drop table if exists user;
create table user( id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255));
INSERT INTO sample.user SELECT * FROM example.user;
/*commit 'mysqldump -u root -p nikita2005 example > C:/Users/igor/OneDrive/Работы MySQL/dump.sql';
mysqldump -u root -p nikita2005 sample < C:/Users/igor/OneDrive/Работы MySQL/dump.sql;/*