create database flori;

use flori;

-- tabela produto

create table produto(
cod_produto int(10) not null primary key auto_increment,
nome varchar(15) not null,
descricao varchar(40) not null,
tipo varchar(15) not null,
quantidade int(6) not null,
valor float(6) not null
);

-- tabela cliente

create table cliente(
cod_cliente int(4) not null primary key auto_increment,
nome varchar(40) not null,
cpf int(11) not null,
rg int(9) not null,
telefone varchar(17) not null,
endereco varchar(40) not null,
email varchar(25) not null
);

select * from cliente;

-- tabela compras

create table compra(
cod_compra int(6) not null primary key auto_increment,
data date not null,
cod_cliente int,
cod_produto int
);

alter table compra
add constraint fk_cliente foreign key (cod_cliente) references cliente(cod_cliente),
add constraint fk_produto foreign key (cod_produto) references produto(cod_produto);
