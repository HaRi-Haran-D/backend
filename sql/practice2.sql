create database stores;

use stores;

-- alter database read only = 0;


create table employees(
	emp_id int primary key auto_increment,
    emp_name varchar(30),
    salary decimal(6,2),
    join_date date
    );



alter table employees add phone_no bigint;

alter table employees add email varchar(50);

alter table employees rename column phone_no to ph_no;

alter table employees modify column ph_no bigint after salary;

alter table employees drop column email;


describe employees;



insert into employees values(null,'Hari',100.00,1234,current_date());

insert into employees values(null,'JK',200.00,3452,'2025-04-19'),(null,'Yuvi',300.00,2456,'2025-06-09');

insert into employees (emp_name,salary) values('Jagath',400.00);



select * from employees;

select emp_name, salary from employees;

select emp_name as Name, salary as Sal from employees;



update employees set ph_no=5676, join_date='2025-08-09' where emp_id=5;

update employees set ph_no = 6969 where emp_id=5;

delete from employees where emp_id =4;

delete from employees;



set autocommit = 0;
commit;


create table timestamp(
	doj date,
    date_time datetime,
    Times time
    );