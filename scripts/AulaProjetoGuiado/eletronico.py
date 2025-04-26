from log import log

class Eletronico():

    def __init__(self, nome):
        self.nome = nome
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True 

    def desligar(self):
        if self.ligado:
            self.ligado = False

class Smartphone(Eletronico):

    def ligar(self):
        super().ligar

    def desligar(self):
        super().desligar
        