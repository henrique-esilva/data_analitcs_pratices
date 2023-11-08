create database magazu;

use magazu;

create table produto(
cod_produto int not null auto_increment primary key,
nome varChar(26) not null,
descricao varchar(128),
preco float not null
);

create table cliente(
cod_cliente int not null auto_increment primary key,
nome varchar(30),
telefone varchar(14),
endereco varchar(40)
);

create table fornecedor(
cod_fornecedor int not null auto_increment primary key,
razao_social varchar(40) not null,
nome_fantasia varchar(40) not null
);
