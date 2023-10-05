nomes = []
while True:
    resposta = input('Escreva seu nome: ')
    if resposta == '':
        break
    nomes.append(resposta)

for i in nomes:
    print('Muito bom conhecer você, ' + i + '!')

# reutilizando o código anterior, crie uma nova lista que armazene mais três nomes
# concatene com a anterior e verifique se os nomes dos facilitadores está na lista
# concatenada.
del(i)
facilitadores = ['simone', 'douglas', 'davi', 'cristiane']

nomes1 = [input('Escreva seu nome: ') for i in range(3)]
for i in (nomes+nomes1):
    if i.lower() in facilitadores:
        print("%s é o nome de um(a) facilitador(a)" % i)