create database magazu;

use magazu;

select * from produto;

drop table produto;
create table produto(
codproduto int not null auto_increment primary key,
nome varChar(26) not null,
descricao varchar(128),
preco float not null
);

alter table produto add(codfornecedor int not null);

alter table produto add constraint
fkfornecedor foreign key(codfornecedor )
references fornecedor(codfornecedor );

drop table cliente;
create table cliente(
codcliente int not null auto_increment primary key,
nome varchar(30),
telefone varchar(14),
endereco varchar(40)
);

alter table cliente modify telefone varchar(30) not null;

drop table fornecedor;
create table fornecedor(
codfornecedor int not null auto_increment primary key,
razao_social varchar(40) not null,
nome_fantasia varchar(40) not null
);

drop table pedido;
create table pedido(
codpedido int(11) not null primary key auto_increment,
datapedido date not null,
quantidade int(11) not null,
valor float not null,
total float not null,
codcliente int(11) not null,
codproduto int(11) not null
);

alter table pedido add constraint
fkproduto foreign key(codproduto)
references produto(codproduto);



insert into cliente(codcliente, nome,  telefone, endereco)
values
(null, 'Ana', 'Rua abc', '+552190000000');