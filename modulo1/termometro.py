temperatura:float = float(input('Digite sua temperatura: '))

if temperatura > 38:
    print('você está com febre')
else:
    print('nada de febre')

if temperatura > 40:
    print('obs.: a temperatura é anormal! Procure um médico!')
