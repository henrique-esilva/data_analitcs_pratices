while True:
    temp=input('temperatura: ')
    if temp == 'sair':
        break
    temp=float(temp)
    if 38 <= temp < 39:
        print('tome um remedio')
    elif temp >= 39:
        print('procure um medico')
    elif temp < 38:
        print('nada de febre')