# percorre a string, escrevendo os caracteres um a um
nome='pedroncio'
for i in range(len(nome)):
    print(nome[i])
print()
for i in nome:
    print(i)

# secção de iteráveis
sentence:str='Contemple'
print(sentence[0:5])
print(sentence[0:4])
print(sentence[10:])
print(sentence[11:])

# percorrendo string ao contrário

# metodo 1
for i in reversed(sentence):
    print(i)
print()
# metodo 2
for i in sentence[::-1]:
    print(i)
print()
for i in range(len(sentence)-1, -1, -1):
    print(sentence[i])

print(sentence[0])