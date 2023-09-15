import os
from listar import listar

# Lista para armazenar as informacoes do usuario e pedido


informacoes_pessoais = []
informacoes_pedido = []
info_endereco = []
info_pagamento = []

# Apresentação do nosso Bot


def apresentacao():
    print("-" * 40)
    saudacao = "\n "+"~"*3+"  O MELHOR SANDUÍCHE DA CIDADE  "+"~"*3
    print("~" * 8, "BEM VINDO AO SANDUREI", "~" * 8, saudacao)
    print("-" * 40)

# Começar o atendimento


def menu1():
    opcao = 0
    
    os.system('cls')
    print("\nÉ um prazer, " + nome, "vamos continuar com o seu atendimento!")
    listar(["Escolha seu Sanduiche", "Escolha sua Bebida", "Qual a Forma de Pagamento?", "Finalizar Pedido", "Sair"])
    opcao = str(input("Qual opção deseja? "))

    if opcao == "5":
        print("Saindo")
        os.system('cls')

    elif opcao == "4":
        print("Finalizado!")
        endereco()
        os.system('cls')

    elif opcao == "3":
        os.system('cls')
        listar(["Debito", "Crédito", "Pix", "Dinheiro"])
        pagamento = str(input("Qual opção deseja? "))
        info_pagamento.append(pagamento)
        return menu1()

    elif opcao == "2":
        os.system('cls')
        listar(["Suco de limão", "Suco de limão com morango", "Coca cola"])
        bebida = str(input("Qual opção deseja? "))
        informacoes_pedido.append(bebida)
        return menu1()

    elif opcao == "1":
        os.system('cls')
        listar(["Sanduiche de Carne Assada", "Sanduiche de Pernil", "Sanduiche de Rosbife"])
        sanduiche = str(input("Qual opção deseja? "))
        informacoes_pedido.append(sanduiche)
        return menu1()

    else:
        print("Opção inválida, selecione as opções.")
        return menu1()

# Coletando Informações sobre o Endereço


def endereco():
    print("Agora precisamos saber o seu endereço.")
    endereco1 = str(input("Qual o seu endereço? "))
    info_endereco.append(endereco1)
    bairro = str(input("Qual o seu Bairro? "))
    info_endereco.append(bairro)
    referencia = str(input("Qual o Ponto de Referencia? "))
    info_endereco.append(referencia)

    print("Valores na lista info_endereco:")
    
    print(f"Endereço: {info_endereco[0]}\nBairro: {info_endereco[1]}\nReferencia: {info_endereco[2]}")
    input("Correto? \n")
    print(informacoes_pedido)
    input("Correto?")
    print()


# Inicio
apresentacao()
nome = str(input("Seja bem vindo! Qual o seu nome? "))
informacoes_pessoais.append(nome)
menu1()
