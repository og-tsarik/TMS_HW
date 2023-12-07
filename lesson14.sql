create database if not exists lesson14;

use lesson14;

show tables;

create table seller (
	id int unsigned primary key auto_increment,
	company varchar(64) unique not null,
    phone varchar(15) null
);

create table users (
	id int unsigned primary key auto_increment,
	username varchar(64) unique not null,
    password varchar(64) not null,
    email varchar(50) unique not null
);

create table products (
	id int unsigned primary key auto_increment,
	name varchar(64) not null,
	cost int unsigned not null,
	count int unsigned not null,
    seller_id int unsigned not null,
    foreign key (seller_id) references seller (id)
);

create table orders (
	id int unsigned primary key auto_increment,
    user_id int unsigned not null,
    product_id int unsigned not null,
	count int unsigned not null,
    foreign key (user_id) references users (id),
    foreign key (product_id) references products (id)
);

select * from seller;
select * from users;
select * from products;
select * from orders;
show tables;

insert users(username, password, email) values('igor', 'password', 'igor@mail.com');
insert users(username, password, email) values('max', 'password', 'max@mail.com');

insert seller(company, phone) values('Balt', '+375449684257');
insert seller(company, phone) values('Tempo', '+3752933214578');
insert seller(company, phone) values('XP', '+375296358745');

insert products(name, cost, count, seller_id) values('cat', 15, 10, 1);
insert products(name, cost, count, seller_id) values('dog', 50, 3, 1);
insert products(name, cost, count, seller_id) values('cd', 5, 1000, 2);
insert products(name, cost, count, seller_id) values('book', 20, 132, 2);
insert products(name, cost, count, seller_id) values('game', 50, 34, 3);

insert orders(user_id, product_id, count) values(1, 1, 1);
insert orders(user_id, product_id, count) values(2, 3, 5);
insert orders(user_id, product_id, count) values(2, 4, 3);
insert orders(user_id, product_id, count) values(1, 2, 1);