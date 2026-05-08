create database cena;
use cena;

create table dep(
depid int primary key,
depname varchar(50),
deploc varchar(50),
depheadcontactname varchar(50),
depheadcontactno varchar(50));

create table emp(
empid int primary key,
empname varchar(50),
empsal int,
emploc varchar(50),
empdob date,
empgender varchar(50),
empContact varchar(50),
depid int,
foreign key (depid) references dep(depid));


INSERT INTO dep VALUES 
(1, 'Sales', 'Chennai', 'Ramesh Kumar', '9876543210'),
(2, 'HR', 'Bangalore', 'Anita Sharma', '9123456780'),
(3, 'Finance', 'Mumbai', 'Suresh Iyer', '9988776655'),
(4, 'IT', 'Hyderabad', 'Karthik Reddy', '9090909090'),
(5, 'Marketing', 'Delhi', 'Priya Singh', '9871234567'),
(6, 'Operations', 'Pune', 'Vikram Joshi', '9765432109'),
(7, 'Logistics', 'Kolkata', 'Arjun Das', '9345678901'),
(8, 'Customer Support', 'Chennai', 'Meena Lakshmi', '9012345678'),
(9, 'R&D', 'Bangalore', 'Rahul Verma', '8899776655'),
(10, 'Admin', 'Coimbatore', 'Deepa Nair', '9786543210');

INSERT INTO emp VALUES
(101, 'Arun Kumar', 45000, 'Chennai', '1998-05-12', 'Male', '9876501234', 1),
(102, 'Sneha Reddy', 52000, 'Bangalore', '1997-08-22', 'Female', '9123409876', 2),
(103, 'Vikash Singh', 60000, 'Mumbai', '1995-11-10', 'Male', '9988001122', 3),
(104, 'Priya Nair', 48000, 'Hyderabad', '1999-02-18', 'Female', '9090912345', 4),
(105, 'Karthik Raj', 55000, 'Delhi', '1996-07-30', 'Male', '9871230001', 5),
(106, 'Meena Iyer', 47000, 'Pune', '1998-09-14', 'Female', '9765402222', 6),
(107, 'Rahul Das', 53000, 'Kolkata', '1997-12-05', 'Male', '9345603333', 7),
(108, 'Anjali Sharma', 49000, 'Chennai', '2000-03-25', 'Female', '9012304444', 8),
(109, 'Suresh Babu', 65000, 'Bangalore', '1994-06-19', 'Male', '8899705555', 9),
(110, 'Deepa Menon', 46000, 'Coimbatore', '1998-01-08', 'Female', '9786506666', 10);


		/* Nth largest sal
limit = how many rows to skip
offset = how many rows to skip */

select * from emp;

select distinct empsal
from emp
order by empsal desc
limit 1,1;

		/* Nth smallest sal*/
select distinct empsal
from emp
order by empsal asc
limit 1 , 1;

	/* print last 3 rows */
select *from emp order by empid desc limit 3;

	/* print first 3 rows */
select *from emp order by empid limit 3;

		/* Avg,min,max*/
select avg(empsal) as avg  from emp;

		/* highest sal in each dep*/
select depid,max(empsal) as max_sal from emp group by depid;

		/* count emp based on dep*/
select  depid , count(*) as count_emp from emp group by depid;

		/*emp earning more than avg in each dep*/
 select empname,empsal,depid
 from emp e
 where empsal>
 (select avg(empsal) from emp where depid=e.depid);
 
		/*duplicate emp*/
select empname,count(*) 
from emp group by empname
having count(*)>1;

		/* emp with same sal*/
select empsal,count(*)
from emp 
group by empsal
having count(*)>1;

		/*highest paid emp in each dep*/
select * from emp e
where empsal=
(select max(empsal) from emp where depid=e.depid);

alter table emp add manager_id int;

alter table emp add constraint fk_manager foreign key (manager_id) references emp(empid);

update emp set manager_id = 1 where empid=2;

-- inner join
select e.empid, e.empname, d.depname from emp e inner join dep d on e.depid = d.depid;

-- left join  (all employee from department even if there is no department) 
select e.empid, e.empname, d.depname from emp e left join dep d on e.depid = d.depid;

-- right join (all department even if it has no employee)
select e.empid, e.empname, d.depname from emp e right join dep d on e.depid = d.depid;

-- full join
select e.empid, e.empname, d.depname from emp e left join dep d on e.depid = d.depid
union
select e.empid, e.empname, d.depname from emp e right join dep d on e.depid = d.depid;

/* why sql does not spport full outer join?
a full outer join returns all matching rows from both tables,
along with that unmatched rows from both side filled with nulls so mysql focused on both left and right joins along with union,
that is left join gives all rows from table 1.
right join gives all row from table 2.
union merges both tables and remove duplicates
*/

-- employee earning more than the manager
select e.empname from emp e join emp d on e.manager_id = d.empid where e.empsal > m.empsal;

-- count employees in each department
select d.deptname from emp d;

-- highest salary in each department
select e.empname, max(e.empsal)as max_salary from emp e join dep d on e.depid = d.depid group by d.depname;

-- employee table with same salary
select e.empname, e1.empname, e.empsal from emp;