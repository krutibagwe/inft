create database hotelmanagementsystem; 
show databases;
use hotelmanagementsystem;
create table login(username varchar(25), password varchar(25));
insert into login values('admin' , '12345');
select * from login;
use hotelmanagementsystem;
create table employee(name varchar(25), age varchar(10), gender varchar(15), job varchar(30), salary varchar(15), phone varchar(15), email varchar(40), aadhar varchar (20));
describe employee;
select * from employee;
use hotelmanagementsystem;
create table room(roomnumber varchar(10), availability varchar(20), cleaning_status varchar(20), price varchar(20), bed_type varchar(20));
select * from room;
update room set availability = 'Available' where roomnumber = '101';
use hotelmanagementsystem;
create table customer(document varchar(20), number varchar(30), name varchar(30), gender varchar(15), country varchar(20), room varchar(10), checkintime varchar(80), deposit varchar(20));
select * from customer;
use hotelmanagementsystem;
delete from employee;
delete from room;
delete from customer;
insert into login values('admin2' , 'hello12');
show databases;
use hotelmanagementsystem;
show tables;
select * from login;
select * from employee;
select * from room;
select * from customer;
delete from employee;
delete from room;
delete from customer;
