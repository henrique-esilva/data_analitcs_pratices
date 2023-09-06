# precisa ter cinco opções no mínimo 
# vamos coletar dados do usuário
# as respostas serão armazenadas
# pedir nome e idade
# fornecer opções de atendimento frequentes
# pedir uma breve descrição do problema caso o problema não esteja na lista de frequentes
# retornar os dados e respostas do usuário

pedidos = []
reclamacoes = []

dados={'name': '', 'lanche': '', 'endereço': ''}

def collect(message:str=''):
    return input(message)

def pedido(name:str=''):
    lanche = collect('')
    adress = collect('')
    pedidos.append( (name, lanche, adress) )

def reclamacao_pedido(name:str=''):
    a=[]
    adress = collect('digite seu endereço')
    for i in pedidos:
        if i[0] == name and i[2] == adress:
            a.append(i)
    print('pedidos encontrados com seu nome:')
    for i in range(len(a)):
        print("%d. %s" % i, a[i][1])
    response = collect('qual foi o lanche que você pediu?')
    reclamacoes.append( a[response] )

def primeiro_atendimento():
    name = collect('seu nome: ')
    while True:
        atend = collect('''
        escolha uma opção de atendimento:
        1. fazer um pedido
        2. meu pedido não chegou
        3. enviar sugestão
        4. dúvidas frequentes
        5. sair''')
        if atend.isnumeric():
            if int(atend) in range(1, 6):
                atend = int(atend)
                break
            else:
                print('digite um número válido')
        else:
            print('digite um número')
    return (name, atend-1)

def tratar_atendimento():
    response = primeiro_atendimento()
    (
        pedido,
        reclamacao_pedido
    )[response[1]](response[0])