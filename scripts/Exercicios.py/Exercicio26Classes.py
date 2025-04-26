
class Quadrado:

    def __init__(self, lado):
        self.lado = lado
        self.area = lado ** 2

    @property
    def mudar_valor_lado(self):
        return self.lado
    
    @mudar_valor_lado.setter
    def mudar_valor_lado(self, valor):
        self.lado = valor
        self.area = valor ** 2
    


quadrado1 = Quadrado(5)

print(quadrado1.lado)
print(quadrado1.area)

quadrado1.mudar_valor_lado = 10

print(quadrado1.lado)
print(quadrado1.area)
        