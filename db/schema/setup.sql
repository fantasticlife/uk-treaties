drop table if exists treaties;
drop table if exists subjects;
drop table if exists treaty_types;

create table subjects (
	id serial,
	subject varchar(255) not null,
	primary key (id)
);

create table treaty_types (
	id serial,
	short_name varchar(5) not null,
	label varchar(12) not null,
	primary key (id)
);
insert into treaty_types (short_name, label) values ( 'BI', 'Bilateral');
insert into treaty_types (short_name, label) values ( 'MULTI', 'Multilateral');

create table treaties (
	id serial,
	uuid char(36) not null,
	record_id int not null,
	treaty_id int not null,
	title varchar(10000) not null,
	description varchar(10000),
	signed_on varchar(255),
	in_force_on varchar(255),
	
	
	
	treaty_type_id int,
	subject_id int,
	
	
	
	
	
	signed_in varchar(255),
	reference_values varchar(10000),
	country_name varchar(10000),
	
	constraint fk_treaty_type foreign key (treaty_type_id) references treaty_types(id),
	constraint fk_subject foreign key (subject_id) references subjects(id),
	primary key (id)
);
