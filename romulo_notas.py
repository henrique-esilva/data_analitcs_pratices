# recebe notas
"""nota1=float(input('digite a nota 1 '))
nota2=float(input('digite a nota 2 '))
nota3=float(input('digite a nota 3 '))"""

# recebe 3 entradas do usuário
notas = [float(input('digite a %dª nota: '%(i+1))) for i in range(3)]

# calcula médias
me=sum(notas)/len(notas)
ma=0
for i in range(len(notas)):
    ma+=notas[i]*(i+1)
ma=(ma+me)/7

conceptIndex=None
if   9<=ma:
    conceptIndex = 0
elif 7.5<=ma:
    conceptIndex = 1
elif 6<=ma:
    conceptIndex = 2
elif 4<=ma:
    conceptIndex = 3
elif 0<ma:
    conceptIndex = 4
elif 0==ma:
    conceptIndex = 5

# gabarito de conceitos
conceptSheet=['A', 'B', 'C', 'D', 'E', 'F']
situation=['reprovado','aprovado'][int(conceptIndex<=2)]

print('conceito: %s\nsituação: %s'%(conceptSheet[conceptIndex], situation))