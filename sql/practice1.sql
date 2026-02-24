-- to create database
create database girafee;


-- to use database
use girafee;


-- to create table
create table students(
	Std_Id int primary key auto_increment,
    Std_Name varchar(30) not null,
    Subjects varchar(30)
    );


-- to delete table
drop table students;


-- to alter table
alter table students add gpa decimal(2,2);

alter table students drop gpa;


-- to view table details
describe students;


-- to insert values into the table
insert into students (std_name,subjects) values('Hari', 'Maths');
insert into students (std_name,subjects) values('JK', 'Science'),('Yuvi','Social'),('Jagath', 'Tamil'),('Suriya','Biology');
insert into students (std_name,subjects) values('Suriya','Biology');
insert into students (std_id,std_name,subjects) values(null,'Andrew','Maths');


-- to view table with column data
select * from students;


-- to view table with a specific column name
select std_name from students;


-- to view table with a specific data value
select * from students where std_name='Hari';


-- to change the table data if exist
update students set subjects = 'Sci' where subjects = 'Science' limit 1;
update students set subjects = 'Soc' where subjects = 'Social' limit 2;


-- to modify the datatype of the mentioned column
alter table students modify column subjects varchar(40);

alter table students add column percentage decimal(2,2);


-- to delete a column or data from the table
delete from students where std_id=5;

-- to select all the data from the table
select * from students;

-- to display specific column
select std_name from students;

-- to display specific column in order
select * from students order by std_name;
