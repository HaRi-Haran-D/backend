-- Create a database and a table for storing employee details.
create database company;
use company;

create table employee(
	emp_id int primary key auto_increment,
    emp_name varchar(50),
    emp_salary int,
    emp_position varchar(30),
    emp_join_date date
	);
    
describe employee;

-- Insert multiple records into a table.
insert into employee values(null,'Hari',20000,'PFS','2025-08-20');

insert into employee values(null,'JK',50000,'Devops','2023-06-12'),(null,'Jagath',20000,'MERN','2025-06-10'),
							(null,'Yuvi',40000,'Data','2024-04-10'),(null,'DS',20000,'JFS','2022-09-13');

-- Write a query to select all records from a table.
select * from employee;

-- Write a query to select specific columns from a table.
select emp_name from employee;

-- Write a query to filter data using WHERE clause.
select * from employee where emp_salary=20000;
select * from employee where emp_salary>20000;
