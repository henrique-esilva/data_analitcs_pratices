salario_inicial:float = 1350
reajuste:float = 0.5

# calculando...
salario_final = salario_inicial + salario_inicial * reajuste
print( 'O novo salário é: R$%.2f' % salario_final )