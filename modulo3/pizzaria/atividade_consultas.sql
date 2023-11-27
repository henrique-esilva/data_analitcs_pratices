-- Atividade: Criar Consultas

select sum(preco) from tb_pedido;

select max(preco) from tb_pedido;
select avg(preco) from tb_pizza;
select categoria, avg(preco) from tb_pizza group by categoria;
select categoria, avg(preco) from tb_pizza group by categoria having avg(preco);
select tipo_entrega, sum(preco) from tb_pedido group by tipo_entrega;
select nome, count(tb_pedido.id_pedido) from tb_pedido inner join tb_cliente group by nome order by count(id_pedido) asc;



SELECT tb_cliente.nome, COUNT(tb_pedido.id_pedido) AS numero_pedidos
FROM tb_cliente
JOIN tb_pedido ON tb_cliente.id_cliente = tb_pedido.id_cliente
GROUP BY tb_cliente.nome
ORDER BY numero_pedidos;

-- seleciona o preco total dos pedidos agrupados pelo nome da pizza
select tb_pizza.nome, sum(tb_pizza.preco) from tb_pedido inner join tb_pedido_pizza inner join tb_pizza on
(tb_pedido.id_pedido = tb_pedido_pizza.id_pedido) and
(tb_pizza.id_pizza = tb_pedido_pizza.id_pizza) group by tb_pizza.nome;

SELECT id_pizza, sum(preco)
FROM tb_pedido_pizza
INNER JOIN tb_pedido
ON tb_pedido_pizza.id_pedido = tb_pedido.id_pedido GROUP BY id_pizza;

-- filtrando apenas as pizzas ZERO LACTOSE
select tb_pizza.nome, sum(tb_pizza.preco), categoria from tb_pedido inner join tb_pedido_pizza inner join tb_pizza where
(tb_pedido.id_pedido = tb_pedido_pizza.id_pedido) and
(tb_pizza.id_pizza = tb_pedido_pizza.id_pizza) group by tb_pizza.nome having categoria = "Zero Lactose";
