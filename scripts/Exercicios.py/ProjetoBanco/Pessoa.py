from abc import ABC,abstractmethod
from contas import ContaCorrente, ContaPoupança

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def alterar_idade(self):
        return self.idade
    @property
    def alterar_nome(self):
        return self.nome
    
    @alterar_idade.setter
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        return self.idade
    @alterar_nome.setter
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome
    
class Cliente(Pessoa, ContaCorrente, ContaPoupança):
    
    ...
