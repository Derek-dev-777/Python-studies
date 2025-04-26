# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): # esse metodo "representa" como o seu objeto vai ser mostrado quando chamado
        class_name = type(self).__name__
        return f"{class_name}(x={self.x}, y={self.y})"

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

print(p1)
print(p2)
print(repr(p2)) # OU VOCÊ SIMPLESMENTE USA ASSIM AO INVES DE ESCREVER NA MAAAAAAAAAAAO 


"""
Os métodos não são executados automaticamente ao criar um objeto, mas são chamados quando suas operações 
correspondentes ocorrem. Se quiser que algo rode automaticamente ao instanciar a classe, use __init__.
"""

