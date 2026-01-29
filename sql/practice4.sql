create database film;
use film;

create table movies(
	id int primary key auto_increment,
    title varchar(50) not null,
    director varchar(50) not null,
    year int not null,
    length_minutes int
    );
describe movies;

insert into movies values(null,'Toy Story','John Lasseter',1995,81);

insert into movies values(null,'A Bugs Life','John Lasseter',1998,95),
	(null,'Toy Story 2','John Lasseter',1999,93),
	(null,'Monsters, Inc.','Pete Docter',2001,92),
    (null,'Finding Nemo','Andrew Stanton',2003,107),
    (null,'The Incredibles','Brad Bird',2004,116),
    (null,'Cars','John Lasseter',2006,117),
    (null,'Ratatouille','Brad Bird',2007,115),
    (null,'WALL-E','Andrew Stanton',2008,104),
    (null,'Up','Pete Docter',2009,101),
    (null,'Toy Story 3','Lee Unkrich',2010,103),
    (null,'Cars 2','John Lasseter',2011,120),
    (null,'Brave','Brenda Chapman',2012,102),
    (null,'Monsters University','Dan Scanlon',2013,110);

insert into movies values(87,'WALL-G','Brenda Chapman',2042,97);


-- Exercise 1
-- Find all the information about each film
select * from movies;

-- Find the title of each film
select title from movies;

-- Find the director of each film
select director from movies;

-- Find the title and director of each film
select title, director from movies;

-- Find the title and year of each film
select title, year from movies;


-- Exercise 2
-- Find the movie with a row id of 6
select * from movies where id=6;

-- Find the movies released in the years between 2000 and 2010
select * from movies where year between 2000 and 2010;
-- OR
select * from movies where year>=2000 and year<=2010;

-- Find the movies not released in the years between 2000 and 2010
select * from movies where year not between 2000 and 2010;
-- OR
select * from movies where year<=2000 or year>=2010;

-- Find the first 5 Pixar movies and their release year
select * from movies where id<=5;
-- OR
select title, year from movies where year<=2003;

-- Excersice 3
-- Find all the Toy Story movies
select * from movies where title like 'Toy Story%';