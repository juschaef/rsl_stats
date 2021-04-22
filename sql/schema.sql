CREATE TABLE artifact (
	id integer primary key autoincrement,
	set varchar(255) not null,
	rarity varchar(255) not null,
	star integer not null,
	piece varchar(255) not null,
	main_stat varchar(255) not null,
	main_value integer not null,
	sub_stat_1 varchar(255),
	sub_value_1 integer,
	sub_stat_2 varchar(255),
	sub_value_2 integer,
	sub_stat_3 varchar(255),
	sub_value_3 integer,
	sub_stat_4 varchar(255),
	sub_value_4 integer
);