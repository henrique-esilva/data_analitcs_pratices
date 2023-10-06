pacientes = []
paciente = {'nome': '', 'altura': float(), 'peso': float()}
while True:
    hold = {}
    nome = input('nome: ')
    if nome == '':
        break
    hold['nome'] = nome
    hold['altura'] = float(input('altura: '))
    hold['peso'] = float(input('peso: '))
    pacientes.append(hold)

for i in pacientes:
    i['IMC'] = ( i['peso']/ i['altura']**2 )

print(pacientes)
