-- consultas no pizzaria

use pizzaria;
-- seleciona todos os valores de todos os campos da tabela
select * from tb_pedido;
-- seleciona apenas o maior valor do campo `preco` da tabela
select max(preco) from tb_pedido;
-- seleciona apenas o menor valor do campo `preco` da tabela
select min(preco) from tb_pedido;
-- seleciona a soma de todos os valores do campo `preco` da tabela tb_pedido
select sum(preco) from tb_pedido;
-- seleciona todos os valores do campo `preco` da tabela pedido em ordem crescente (ASCendente)
select preco from tb_pedido order by preco asc;
-- seleciona todos os valores do campo `preco` da tabela pedido em ordem decrescente (DESCendente)
select preco from tb_pedido order by preco desc;

-- documentar group by

-- seleciona o somatório de todas as linhas de um campo filtrando por uma condicional
select sum(preco) from tb_pedido where preco < 100;

select nome, preco from tb_pedido inner join tb_cliente where nome like 'm%' order by nome asc;

-- inner join pode ser usado para fazer a junção de tabelas durante uma consulta, desde que todas estejam relacionadas
select nome, preco
from tb_cliente inner join tb_pedido
on tb_cliente.id_cliente = tb_pedido.id_cliente where preco in(45, 95, 120) order by nome desc;

select * from tb_cliente left join tb_pedido on tb_cliente.id_cliente=tb_pedido.id_cliente;
select * from tb_pedido where preco in(90, 100, 320);

-- 
select categoria, count(*) from tb_pizza group by categoria;
