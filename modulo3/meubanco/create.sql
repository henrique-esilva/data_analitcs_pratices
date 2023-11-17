CREATE DATABASE meubanco;
USE meubanco;
CREATE TABLE pessoas(
cod_pessoa INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(80),
tem_smartphone BOOL
);
