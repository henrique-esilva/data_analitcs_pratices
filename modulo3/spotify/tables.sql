-- banco spotify

-- usuario(idusuario,nome,email, senha)

-- musicas(idmusica, nome, duracao, categoria,
-- idartista)
-- artista(idartista, nome)
-- playlist(idplaylist, idmusica, data)
-- 

create database spotfy;

use spotfy;

create table artista(
id_artista int not null primary key auto_increment,
nome varchar(20)
);

create table musica(
	id_musica int(12) not null primary key auto_increment,
	nome varchar(30) not null,
	categoria varchar(10),
	duracao time not null,
	id_artista int
);
alter table musica
add constraint fk_artista foreign key(id_artista) references artista(id_artista);

create table usuario(
	id_usuario int(11) not null primary key auto_increment,
	nome varchar(20),
	email varchar(50),
	senha varchar(50)
);

create table playlist(
	id_playlist int(12) not null primary key auto_increment,
	id_musica int(12)
);
alter table playlist
add constraint foreign key(id_musica) references musica(id_musica);

alter table playlist add(id_usuario int not null);

alter table playlist
add constraint fk_usuario foreign key(id_usuario) references usuario(id_usuario);

create table reproducao(
	id_reproducao int(13) not null primary key auto_increment,
	data datetime not null,
	id_musica int(12),
	id_usuario int(11)
);
alter table reproducao
add constraint fk_repr_musica foreign key(id_musica) references musica(id_musica),
add constraint fk_repr_usuario foreign key(id_usuario) references usuario(id_usuario);
