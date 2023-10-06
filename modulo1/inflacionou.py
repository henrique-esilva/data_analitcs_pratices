alimentos = {
    'laranja': (12.0, 12.0),
    'limao': (18.0, 17.0),
    'abacaxi': (7.0, 9.0),
    'tomate': (10.0, 9.0)
}

resposta = input('Qual alimento você pretende consultar? ').lower()
if resposta in alimentos:
    valores = alimentos[resposta]
    if valores[0] > valores[1]:
        print('o preço diminuiu %.2f reais' % (valores[0]-valores[1]) )
    elif valores[0] < valores[1]:
        print('o preço aumentou R$%.2f' % (valores[1]-valores[0]) )
    elif valores[0] == valores[1]:
        print('o preço não se alterou')
else:
    print('infelizmente o item está indisponível')