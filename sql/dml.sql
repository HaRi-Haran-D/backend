create database student;
use student;
create table Student(
	Std_Id int primary key auto_increment,
    Name varchar(40),
    Gpa decimal(3,2));

alter table Student add department varchar(10);
alter table Student drop department;
describe Student;