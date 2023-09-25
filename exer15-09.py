20*30
42/30
(94+2)*6-1

# 2 em Python realize a operação abaixo e exiba o resultado usando print

operations=[
    (80*94)/(10+55-90),
    (10-7)/(67*5),
    (12**4+5)*3+7,
    7%3**11*8-20-10/5+92
]
for i in operations:
    print(i)

def escreve_nome():
    "3 em Python, armazene seu nome em uma variável e exiba usando o comando print()"
    meuNome=input('escreva seu nome: ')
    print(meuNome)

def operacao_fixa():
    "4 usando o print, exiba o resultado de 3x-10y sendo que x recebe 10 e y recebe 2"
    x=10
    y=2
    print(3*x-10*y)

def media_dois_numeros():
    "5 em Python crie uma aplicação que calcule a média aritmética de duas entradas do usuário"
    x=input('digite um número')
    y=input('digite outro número')
    print('Sua média é %s'%((x+y)/2))

def salario_do_dia():
    "6 criar um programa que calcule quanto um usuário ganhará por dia em um mês de 30 dias"
    sal = float( input('Digite seu salário') )
    print('Seu ganho diário é de %f' % sal)

def dia_da_semana():
    "7 crie uma aplicação que receba uma sigla de um dia da semana e imprima o dia por extenso"
    semana={
        'dom': 'domingo',
        'seg': 'segunda-feira',
        'ter': 'terça-feira',
        'qua': 'quarta-feira',
        'qui': 'quinta-feira',
        'sex': 'sexta-feira',
        'sab': 'sábado',
    }
    response = input('Digite uma sigla de dia da semana: ').lower()
    print(semana[response])

def testes_logicos():
    __doc__="""8 usando testes booleanos, responda com True ou False sendo que:
    a = 2
    b = 5.0
    c = 20
    d = 9
    f = 9"""
    a=(
        False,
        True,
        False,
        True,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
    )
    for i in a: print(i)