

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome


    def escrever(self):
        return f"{self.nome} está escrevendo"
    
escritor  = Escritor("Derek") # aqui estou atribuindo o nome do meu escritor
ferramentaescrever = FerramentaDeEscrever("Lapis") # aqui atribuo o nome da ferramenta 

escritor.ferramenta = ferramentaescrever # com o setter, eu digo que a minha ferramenta é igual a de cima

print(ferramentaescrever.escrever())
print(escritor.ferramenta.escrever())