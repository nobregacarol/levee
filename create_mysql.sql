create database levee;
use levee;

create table category(
	category_id int unique primary key,
    title varchar(50) unique not null
);

create table jobs(
	partner_id int unique primary key,
    job_title varchar(100) not null,
    category_id int,
    foreign key (category_id) references category(category_id),
    expires_at date,
    open_position_amount int not null
);