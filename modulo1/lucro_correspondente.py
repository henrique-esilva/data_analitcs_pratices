produtos_precos={
    'ração-gato(kg)':25,
    'ração-cachorro(kg)':23,
    'osso-de-borracha':12,
}

produtos=tuple( produtos_precos.keys() )

for i in range(len(produtos)):
    print( "{}-{}".format(i+1,produtos[i]) )

preco=tuple(produtos_precos.values())[int(input('\nDigite o mumero correspondente ao produto: '))-1]

#lucro=float(input("digite sua margem de lucro\nexemplo: para 50% digite 50: "))

if preco > 20:
    lucro = 45
else:
    lucro = 30

preco_com_lucro=preco+(preco*lucro)/100

print(f'\nvalor com lucro: {preco_com_lucro}')