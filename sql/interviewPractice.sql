create database company;

use company;

create table employee(
	emp_id int primary key,
    emp_name varchar(100) not null,
    emp_salary decimal(6,2),
    emp_location varchar(100),
    emp_dob date,
    emp_gender varchar(10),
    emp_contact int,
    emp_designation varchar(50)
    );

describe employee;
alter table employee modify emp_salary decimal(10,2);

alter table employee modify emp_contact bigint not null;

alter table employee modify emp_contact varchar(10);

alter table employee modify emp_id int auto_increment;

alter table employee modify column emp_designation varchar(50) after emp_name;

insert into employee (emp_id, emp_name, emp_salary, emp_location, emp_dob, emp_gender, emp_contact, emp_designation) 
			values(null, 'Arun Kumar', 45000.00, 'Chennai', '1998-05-14', 'Male', 9876543210, 'Software Engineer');
		
        
insert into employee (emp_id, emp_name, emp_salary, emp_location, emp_dob, emp_gender, emp_contact, emp_designation) 
			values(null, 'Priya Sharma', 52000.00, 'Bangalore', '1997-08-22', 'Female', 9123456780, 'Data Analyst'),
				(null, 'Rahul Verma', 60000.00, 'Hyderabad', '1996-12-10', 'Male', 9988776655, 'SQL Developer'),
				(null, 'Sneha Iyer', 48000.00, 'Chennai', '1999-03-18', 'Female', 9871234567, 'HR Executive'),
				(null, 'Karthik Reddy', 70000.00, 'Hyderabad', '1995-07-25', 'Male', 9012345678, 'Database Administrator'),
				(null, 'Anjali Mehta', 55000.00, 'Mumbai', '1998-11-05', 'Female', 9090909090, 'Business Analyst'),
				(null, 'Vikram Singh', 65000.00, 'Delhi', '1996-01-30', 'Male', 8887776665, 'Backend Developer'),
				(null, 'Divya Nair', 47000.00, 'Kochi', '1999-09-12', 'Female', 9797979797, 'Support Engineer'),
				(null, 'Suresh Babu', 53000.00, 'Chennai', '1997-06-08', 'Male', 9898989898, 'System Admin'),
				(null, 'Neha Gupta', 62000.00, 'Pune', '1995-04-27', 'Female', 9111222233, 'Project Coordinator');
                

-- find the nth smallest or largest number
select emp_salary from employee order by emp_salary desc limit 1 offset 1;
select emp_salary from employee order by emp_salary asc limit 1 offset 1;

-- find nth smallest or largest without limit
SELECT emp_salary FROM employee e1 WHERE (SELECT COUNT(DISTINCT e2.emp_salary)FROM employee e2 WHERE e2.emp_salary > e1.emp_salary) = 3;

-- print last 3 rows
select * from employee order by emp_id desc limit 3;
select * from employee where emp_id > (select max(emp_id)-3 from employee);

-- print last 4 rows
select * from employee order by emp_id desc limit 4;
select * from employee where emp_id > (select Max(emp_id)-4 from employee);


create table department(
		dept_id int primary key,
        dept_name varchar(100) unique,
        dept_location varchar(100),
        dept_headname varchar(100),
        foreign key(dept_headname) references employee(emp_name),
        dept_headcontact bigint
        );


alter table department modify dept_headname varchar(100) primary key;
-- insert into department values(101, "Team A","Chennai",);
select * from employee;

select emp_salary from employee e1 where (select count(distinct e2.emp_salary) from employee e2 where e2.emp_salary > e1.emp_salary) = 3;

select emp_salary from employee order by emp_salary desc limit 1 offset 2;

select * from employee where emp_id > (select max(emp_id)-3 from employee);

