-- Atividade: Criar Consultas

select sum(preco) from tb_pedido;

select max(preco) from tb_pedido;
select avg(preco) from tb_pizza;
select categoria, avg(preco) from tb_pizza group by categoria;
select categoria, avg(preco) from tb_pizza group by categoria having avg(preco);
select tipo_entrega, sum(preco) from tb_pedido group by tipo_entrega;
select nome, count(tb_pedido.id_pedido) from tb_pedido inner join tb_cliente group by nome order by count(id_pedido) asc;

-- select nome, count();

SELECT tb_cliente.nome, COUNT(tb_pedido.id_pedido) AS numero_pedidos
FROM tb_cliente
JOIN tb_pedido ON tb_cliente.id_cliente = tb_pedido.id_cliente
GROUP BY tb_cliente.nome
ORDER BY numero_pedidos;
