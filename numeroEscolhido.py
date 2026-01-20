import random

class numeroEscolhido:
    def __init__(self):
        self.ganhou = False
        self.__numero = None
        self.define_numero()

    @property
    def get_numero(self):
        try :
            return self.__numero
        except AttributeError:
            raise AttributeError("Número não definido. Use o setter para definir um número.")

    def define_numero(self):
        self.__numero = random.randint(1, 100)

    def verificar_numero(self, chute):
        if chute < self.__numero:
            return "O número escolhido é maior!"
        elif chute > self.__numero:
            return "O número escolhido é menor!"
        else:
            self.ganhou = True
            return "Parabéns! Você acertou o número!"
    
    def ja_ganhou(self):
        return self.ganhou