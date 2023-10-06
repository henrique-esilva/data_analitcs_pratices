# 22/09/2023
def funcao(a:list,b:list):
    retornos=[]
    retornos.append(
        [x*y for x, y in zip(a,b)]
    )
    retornos.append([sum(a), sum(b)])
    a_ = a.copy()
    for i in a_:
        if i % 2 != 0: a.remove(i)
    b_ = b.copy()
    for i in b_:
        if i % 2 != 0: b.remove(i)
    return retornos

# lista1 = list(range(1,16))
# lista2 = list(range(15, 0,-1))

# print(funcao(lista1,lista2))

# print(lista1,lista2)

# 04/10/2023

lista1 = [10, 20, 30, 40]
lista2 = ['sapo', 'cobra', 'jacaré']
lista3 = [10, 20, ['sapo', 'jacaré']]

print(lista1[0:2])
print(lista1)
