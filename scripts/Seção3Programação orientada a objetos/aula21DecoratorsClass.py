# Classes decoradoras, nessa aula levamos como ensinamento de que para um codigo limpo, podemos fazer uma classe
# que mantenha funções que vao se repetir em outras como exemplo do __repr__, e herda-las nas classes principais

class MyRepr:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr 

class Time(MyRepr):

    def __init__(self, nome):
        self.nome = nome



class Planeta(MyRepr):

    def __init__(self, nome):
        self.nome = nome



brasil = Time("Brasil")
portugal = Time("Portugal")

jupiter = Planeta("Jupiter")
netuno = Planeta("Netuno")
print(brasil)
print(portugal)
print(jupiter)
print(netuno)