entry:float = float(
    input('Olá por favor digite um número\nPara números com vírgula use ponto (.)\nsua resposta: ')
)
output:str = f"você escreveu {entry}"
if entry%5 == 0:
    output+='\no numero que você escreveu é um múltiplo de 5'
else:
    output+='\no número que você escreveu não é um múltiplo de 5'
print(output)