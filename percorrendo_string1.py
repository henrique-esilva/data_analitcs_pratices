texto='X-DSPAM-Confidence:0.8475'
inicio = texto.find(':')
fatia = texto[inicio+1:]
num = float(fatia)*100
print(num)