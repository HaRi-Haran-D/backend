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

select * from employees;





