create database Pokedex;
create table Pokedex.tb_pokemons (
	id int(10) not null auto_increment primary key,
	nome varchar(50) not null,
	tipo_1 varchar(10) not null,
	tipo_2 varchar(10),
	foto varchar(100) not null,
	defesa int not null,
	hp int not null,
	ataque int not null,
	descrição varchar(500)
);
