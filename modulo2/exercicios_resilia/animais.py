class Animal:
    def __init__(self, nome:str):
        self.nome = nome
    def falar(self):
        print(self.nome + ' faz ' + self.som)

class Gato(Animal):
    som = 'miau'

meu_gato = Gato('Romeu')

meu_gato.falar()
