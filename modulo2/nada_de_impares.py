valores = list(range(0, 15))

for i in valores:
    if i % 2 != 0:
        valores.remove(i)

valores.sort()

print('total:', valores)
print("menor: %d\nmaior: %d" % (valores[0], valores[-1]))
