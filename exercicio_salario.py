#declara variaveis
salario_recebido:float
salario_minimo:float = 1350.0
quantos_salarios_minimos:float
#recebe entrada
salario_recebido=float(input('qual o salario do funcionario?\nR$'))
#calcula razao
quantos_salarios_minimos=salario_recebido/salario_minimo
#saida
print('A razao entre o salario recebido e o salario minimo e %f' % quantos_salarios_minimos)