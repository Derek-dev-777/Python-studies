
class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.lado1 = ladoA
        self.lado2 = ladoB

    def retornar_valor_lados(self):
        return f"lado A = {self.lado1}, lado B = {self.lado2}"
    
    def calcular_area(self):
        return self.lado1 * self.lado2
    
    def calcular_perimetro(self):
        return 2 * (self.lado1 + self.lado2)
    
    @property
    def mudar_valor(self):
        return self.lado1, self.lado2
    
    @mudar_valor.setter
    def mudar_valor(self, valores):
        self.lado1, self.lado2 = valores


meu_retangulo = Retangulo(5, 5)
print(meu_retangulo.retornar_valor_lados())

print(meu_retangulo.calcular_area())

print(meu_retangulo.calcular_perimetro())

meu_retangulo.mudar_valor = (11, 10)

print(meu_retangulo.retornar_valor_lados())

print(meu_retangulo.calcular_area())

print(meu_retangulo.calcular_perimetro())     