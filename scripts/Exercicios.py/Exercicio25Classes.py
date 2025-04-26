

class Bola:

    def __init__(self, Cor, Circunferencia, Material):
        self.cor = Cor
        self.circunferencia = Circunferencia
        self.material = Material

    @classmethod
    def trocaCor(cls, nova_cor, circu, Material):
        return cls(nova_cor, circu, Material)


bola1 = Bola("Azul", 3, "Borracha")
print(bola1.cor, bola1.circunferencia, bola1.material)

bola1 = Bola.trocaCor("Vermelho", 4, "Borracha")
print(bola1.cor, bola1.circunferencia, bola1.material)
        