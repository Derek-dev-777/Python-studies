
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

meu_carro = Carro("Onix")
Fiat = Fabricante("Fiat")
motorseila = Motor("sei la")

meu_carro.fabricante = Fiat
meu_carro.motor = motorseila

print(meu_carro.nome, meu_carro.fabricante.nome, meu_carro.motor.nome)