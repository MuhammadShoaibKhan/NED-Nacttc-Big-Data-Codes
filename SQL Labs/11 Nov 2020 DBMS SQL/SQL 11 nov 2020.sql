show databases;
create database hpcc;
show databases;
use hpcc;
show tables;
create table teacher(
t_id int(11),
t_name varchar(255),
t_sal int(5)

);

show tables;
rename table teacher to teachers;
desc teachers;
select * from teachers;
insert into teachers(t_id, t_name, t_sal) values(1,'hamza shabbir',6000);
select t_id from teachers;
select * from teachers;
alter table teachers add NoOfCourse int(1);
select * from teachers;
insert into teachers(NoOfCourse) values(3);
select * from teachers;
insert into teachers(t_id, t_name, t_sal,NoOfCourse) values(1,'hamza shabbir',6000,6);
select * from teachers;
alter table teachers change NoOfCourse courses int(1);
select * from teachers;
alter table teachers modify courses varchar(255);
select * from teachers;
alter table teachers modify courses int(1);
select * from teachers;
alter table teachers drop courses;
select * from teachers;


truncate table teachers;
show tables;
drop tables teachers;
select * from teachers;




