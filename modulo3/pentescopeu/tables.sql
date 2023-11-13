create database consultorio;
use consultorio;

create table paciente(
id_paciente int not null primary key,
nome varchar(100) not null
);

create table medico(
id_medico int not null primary key,
nome varchar(100) not null,
crm char(9) not null,
especializacao varchar(40) not null
);

create table consulta(
id_consulta int not null primary key,
data_consulta date not null,
id_medico int, 
id_paciente int,
observacao varchar(300) not null
);
alter table consulta 
add constraint fk_paciente 
foreign key(id_paciente)
references paciente(id_paciente);

alter table consulta 
add constraint fk_medico
foreign key(id_medico)
references medico(id_medico);
