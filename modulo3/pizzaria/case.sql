SELECT nome, preco
CASE 
    when preco < 50 then 'valor baixo'
    when preco >55 then 'valor médio'
    else 'valor não informado'
end as resultado  FROM tb_pizza;
