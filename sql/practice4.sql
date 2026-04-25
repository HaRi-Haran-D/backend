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

-- Find all the movies directed by John Lasseter
select title, director from movies where director = "John Lasseter";
select * from movies where director like "John Lasseter";

-- Find all the movies (and director) not directed by John Lasseter
select title, director from movies where director!= "John Lasseter";
select * from movies where director not like "John Lasseter";

-- Find all the WALL-* movies
select * from movies where title like "WALL-%";
-- OR
select * from movies where title like "WALL-_";


-- Exercise 4 
-- List all directors of Pixar movies (alphabetically), without duplicates
select distinct director from movies order by director;

-- List the last four Pixar movies released (ordered from most recent to least) 
select * from movies order by year desc limit 4;

-- List the first five Pixar movies sorted alphabetically
select title from movies order by title asc limit 5;

-- List the next five Pixar movies sorted alphabetically 
select title from movies order by title asc limit 5 offset 5;

create table north_american_cities(
	city varchar(50) primary key,
    country varchar(50),
    population int,
    latitude decimal(10,6),
    longitude decimal(10,6)
    );

insert into north_american_cities values("Guadalajara","Mexico",1500800,20.659699,-103.349609);
insert into north_american_cities values
					("Toronto","Canada",2795060,43.653226,-79.383184),
                    ("Houston","United States",2195914,29.760427,-95.369803),
                    ("New York","United States",8405837,40.712784,-74.005941),
                    ("Philadelphia","United States",1553165,39.952584,-75.165222),
                    ("Havana","Cuba",2106146,23.05407,-82.345189),
                    ("Mexico City","Mexico",8555500,19.432608,-99.133208),
                    ("Phoenix","United States",1513367,33.448377,-112.074037),
                    ("Los Angeles","United States",3884307,34.052234,-118.243685),
                    ("Ecatepec de Morelos","Mexico",1742000,19.601841,-99.050674),
                    ("Montreal","Canada",1717767,45.501689,-73.567256),
                    ("Chicago","United States",2718782,41.878114,-87.629798);

delete from north_american_cities where id=1;

-- Exercise 5
-- List all the Canadian cities and their populations
SELECT city, population FROM north_american_cities where country = "Canada";

-- Order all the cities in the United States by their latitude from north to south
select * from north_american_cities where country = "United States" order by latitude desc;

-- List all the cities west of Chicago, ordered from west to east 
select * from north_american_cities where longitude < -87.629798 order by longitude desc;

-- List the two largest cities in Mexico (by population)
select * from north_american_cities where country = "Mexico" order by population desc limit 2;

-- List the third and fourth largest cities (by population) in the United States and their population
select * from north_american_cities where country = "United States" order by population desc limit 2 offset 2;


-- Excercise 6
-- Find the domestic and international sales for each movie
SELECT * FROM movies inner join boxoffice on movies.id = boxoffice.movie_id;
-- OR
SELECT title, domestic_sales, international_sales FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id;

-- Show the sales numbers for each movie that did better internationally rather than domestically
select * from boxoffice inner join movies on boxoffice.movie_id = movies.id where domestic_sales < international_sales order by international_sales desc;
-- OR
SELECT title, domestic_sales, international_sales FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id WHERE international_sales > domestic_sales;

-- List all the movies by their ratings in descending order
select * from boxoffice inner join movies on boxoffice.movie_id = movies.id order by rating desc;
-- OR
SELECT title, rating FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id ORDER BY rating DESC;




-- find the nth smallest or largest number
select salary from employee order by salary desc limit 1 offset 1;

select salary from employee order by salary asc limit 1 offset 1;

