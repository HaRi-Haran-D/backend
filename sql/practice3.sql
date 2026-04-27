-- Create a database and a table for storing employee details.
CREATE DATABASE Practice;
USE Practice;

CREATE TABLE employee(
	emp_id int primary key,
    emp_name varchar(100),
    emp_designation varchar(75),
    emp_salary int,
    emp_location varchar(50),
    emp_contact varchar(10)
    );

CREATE TABLE department(
	dept_id int primary key auto_increment,
    dept_name varchar(50) unique,
    dept_code int,
    foreign key(dept_code) references employee(emp_id)
    );
alter table employee modify emp_id int auto_increment;

alter table employee modify emp_contact varchar(10) after emp_salary;

alter table employee add column emp_email varchar(25);

alter table employee drop column emp_email;

describe employee;


select emp_salary from employee where emp_salary < (select max(emp_salary) from employee);