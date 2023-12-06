-- facilitadora Simone
-- analise de dados Senac
-- 06/12/2023
-- aluno Henrique Silva

create database escola;
use escola;

create table escola(
id int primary key,
nome varchar(30));

create table aluno(
id int primary key,
nome varchar(50),
email varchar(60),
sexo varchar(1),
id_escola int,
foreign key(id_escola) references escola(id));

create table aluno_audit(
id_aluno int,
data_insert timestamp);

-- cria um gatilho (trigger)

create definer='root'@'localhost' trigger escola2
before insert on aluno_audit 
for each row set new.data_insert = now()

create definer='root'@'localhost' trigger aluno_log_func
before insert on aluno_audit
for each row set new.data_insert = now();
