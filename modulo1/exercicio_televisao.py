tam_tv:float = float(input('informe o tamanho em polegadas: '))
preco_tv:float = float(input('quanto custa a tv? '))
if tam_tv >= 32 and preco_tv <= 1900.0:
    print("Oba pode comprar!")
else:
    print("Ih compra não...")