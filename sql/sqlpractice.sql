create database kompany;
use Kompany;

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    dept_id INT,
    location VARCHAR(50),
    dob DATE,
    gender VARCHAR(10),
    contact VARCHAR(15),
    joining_date DATE
);

CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50),
    head_name VARCHAR(50),
    head_contact VARCHAR(15)
);

CREATE TABLE Project (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    dept_id INT
);

INSERT INTO Department (dept_id, dept_name, location, head_name, head_contact) VALUES
			(1, 'HR', 'Chennai', 'Ramesh', '9876543210'),
			(2, 'IT', 'Bangalore', 'Suresh', '9876501234'),
			(3, 'Finance', 'Mumbai', 'Anita', '9123456780'),
			(4, 'Sales', 'Delhi', 'Karthik', '9988776655'),
			(5, 'Marketing', 'Hyderabad', 'Priya', '9090909090');


INSERT INTO Employee (emp_id, name, salary, dept_id, location, dob, gender, contact, joining_date) VALUES
			(101, 'Arun', 50000, 1, 'Chennai', '1998-05-10', 'Male', '9000000001', '2025-03-01'),
			(102, 'Bala', 60000, 2, 'Bangalore', '1997-07-15', 'Male', '9000000002', '2025-02-15'),
			(103, 'Cathy', 55000, 2, 'Bangalore', '1999-01-20', 'Female', '9000000003', '2025-04-01'),
			(104, 'Divya', 70000, 3, 'Mumbai', '1996-11-11', 'Female', '9000000004', '2024-12-20'),
			(105, 'Eshan', 45000, 1, 'Chennai', '2000-03-30', 'Male', '9000000005', '2025-03-10'),
			(106, 'Farah', 80000, 4, 'Delhi', '1995-06-18', 'Female', '9000000006', '2023-10-05'),
			(107, 'Gokul', 75000, 4, 'Delhi', '1994-09-25', 'Male', '9000000007', '2025-01-12'),
			(108, 'Hari', 50000, 2, 'Bangalore', '1998-02-14', 'Male', '9000000008', '2025-03-18'),
			(109, 'Isha', 65000, 5, 'Hyderabad', '1997-08-09', 'Female', '9000000009', '2024-11-01'),
			(110, 'John', 60000, NULL, 'Chennai', '1996-12-12', 'Male', '9000000010', '2025-04-10');

delete from employee where emp_id = 109;

insert into employee values(109, 'Isha', 65000, 5, 'Hyderabad', '1997-08-09', 'Female', '9000000009', '2024-11-01');

INSERT INTO Project (project_id, project_name, dept_id) VALUES
			(201, 'Payroll System', 1),
			(202, 'Website Revamp', 2),
			(203, 'Banking App', 2),
			(204, 'Audit System', 3),
			(205, 'Sales Tracker', 4),
			(206, 'Ad Campaign', 5);
            
            
-- 1. Nth highest / lowest salary (using LIMIT)
-- Lowest
select distinct salary from employee order by salary asc limit 1 offset 1;
-- Highest
select distinct salary from employee order by salary desc limit 1 offset 1;

-- 2. Nth highest / lowest salary Without LIMIT
select salary from employee e1 where (select count(distinct salary) from employee e2 where e1.salary < e2.salary)=2;

-- 3. Subquries
SELECT name FROM Employee WHERE salary > (SELECT AVG(salary) FROM Employee);

-- 4. Avg, Min, Max
SELECT AVG(salary), MIN(salary), MAX(salary) FROM Employee;

-- select distinct salary from employee where salary < (select avg(salary) from employee) order by salary asc;

-- 5. First 3 rows
select * from employee limit 3;

-- 6. Last 3 rows
select * from employee order by emp_id desc limit 3;

-- 7. Count employees per department
select dept_id, count(*) from department group by dept_id;

-- 8. Employees earning more than dept avg
select * from employee e where salary > (select avg(salary) from employee e1 where e.dept_id = e1.dept_id);

-- 9. Duplicate salary in each dept
select dept_id, salary, count(*) from employee group by dept_id, salary having count(*) > 1;

-- 10. Employees based on department
select e.name, d.dept_id, d.dept_name from employee e join department d on e.dept_id = d.dept_id;

-- 1. nth largest/smallest using limit
select salary from employee order by salary desc limit 1 offset 1;
select salary from employee order by salary asc limit 1;

-- 2. without using limit
select salary from employee e1 where (select count(distinct salary) from employee e2 where e1.salary < e2.salary)=3;

select * from employee where salary < (select max(salary) from employee) order by salary desc limit 2;

-- 4. AVG, MAX, MIN
select AVG(salary), MAX(salary), Min(salary) from employee;

-- 5. print last 3 rows
-- select * from employee where emp_id > (select max(emp_id) from employee)-3;
select * from employee order by emp_id desc limit 3;

-- 6. print last 4 rows
select * from employee order by emp_id desc limit 4;
select * from employee where emp_id > (select max(emp_id) from employee)-4;

-- 7. count employee based on department
select e.dept_id, e.name, d.dept_name from employee e join department d on e.dept_id = d.dept_id;

-- 8. highest salary in each department
select e.dept_id, e.name, e.salary from employee e join department d on e.dept_id = d.dept_id;

select dept_id from employee union select dept_id from department;

create view alldata as select * from employee;

select * from alldata order by salary desc;

select e.emp_id, e.name, e.salary, d.dept_name from employee e inner join department d on e.dept_id = d.dept_id order by e.salary desc;

select e.emp_id, e.name, e.salary, d.dept_name from employee e join department d on e.dept_id = d.dept_id; 

delimiter :
create procedure EntireData()
begin
select * from employee;
end:
delimiter ;

drop procedure EntireData;

call EntireData();

delimiter :
create procedure AddData(in id int)
begin
	select * from employee where emp_id = id;
end:
delimiter ;
call AddData(101);

delimiter :
create trigger beforeAdd
before insert on employee
for each row
begin
	set new.salary = IFNULL(new.salary, 35000);
end:
delimiter ;

insert into employee(emp_id, name, dept_id, location, dob, gender, contact, joining_date) values 
		(111, 'Hema', 2, 'Chennai', '2002-12-25', 'Female', '9000000011', '2025-06-18')


delimiter :
create trigger beforeUpdate
before update on employee
for each row
begin
	set new.salary = old.salary * 1.10;
end:
delimiter ;

update employee set salary = 40000 where emp_id = 111;

delimiter :
create trigger beforedelete
before delete on employee
for each row
begin
	insert into project(project_id, project_name) values(404, old.name);
end:
delimiter ;

drop trigger beforedelete;
delete from employee where emp_id= 109;

select * from project;
