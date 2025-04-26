# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.

from abc import ABC, abstractmethod
# para criar uma classe abstrata deve importar ABC, e coloca-la como herança na classe desejada
class Pessoa(ABC):
    @abstractmethod
    def _log(self, nome): ...

class Cliente(Pessoa):

    def _log(self, nome): # deve copiar exatamente o method 
        print(f"oi")

"""
RESUMÃO DE ABSTRACT METHOD:

você irá usar um metodo abstrato para indicar a outros desenvolvedores que TAL metodo não deve ser usado na TAL classe
para usar você deve em OUTRA classe, herdar a super class, copiar IGUALZINHO com os mesmos parametros a função
e ai sim dessa sub class você pode usar a função que foi dada como abstrata, resumindo novamente:

exemplo: você quer fazer um programa onde você ira calcular a area e perimetro de algumas formas geometricas,
você criaria uma função "formas" e criaria os metodos para calcular a area e perimetro nelas, deixando elas abstratas
POIS, voce , não tem inteção de calcular a area DA forma em sim, é apenas um escopo, ai sim você criaria outras classes
como "circulo", "quadrado" fazendo com que elas herdem de "forma" e você use os metodos perimetro e area dela.


abstrata = não use, herde-me em outra classe, ai sim use =)
"""

# exemplo de codigo abstrato

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)