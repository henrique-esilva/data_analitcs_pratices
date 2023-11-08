use magazu;

insert into cliente (codcliente, nome, telefone, endereco) values
(null, 'Ana', '445545', 'Rua asas'),
(null, 'Pedro', '7988998', 'Rua BCV');

insert into `fornecedor` (`codfornecedor`, `nome_fantasia`, `razao_social`, `cnpj`, `email`, `endereco`) values
(null, 'Empresa CWE', 'CWE Equipamentos', '676767767676', 'b@gmail.com', '44332'),
(null, 'Empresa jtr', 'qwe Equipamentos', '88767767676', 'b@gmail.com', '44332');

insert into `produto` (`codproduto`, `nome`, `descricao`, `preco`, `codfornecedor`) values
(null, 'Notebook', 'Info', 3000, 1),
(null, 'Mouse', 'Info', 3000, 1),
(null, 'Monitor', 'Info', 3000, 2);

insert into `pedido` (`codpedido`, `datapedido`, `quantidade`, `valor`, `total`, `codcliente`, `codproduto`) values
(null, '2023-10-11', 10, 250, 2500, 1, 3),
(null, '2023-11-06', 10, 250, 2500, 2, 3),
(null, '2023-11-06', 10, 250, 2500, 1, 3);
