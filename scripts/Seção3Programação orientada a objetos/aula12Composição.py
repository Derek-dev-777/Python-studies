
class Cliente:

    def __init__(self, nome):

        self.nome = nome
        self.endereço = []

    def inserirEndereço(self, rua, numero):
        self.endereço.append(Endereço(rua, numero))

    def listar_endereço(self):
        for endereco in self.endereço:
            print(endereco.rua, endereco.numero)

class Endereço:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
cliente1 = Cliente("Derek")
cliente1.inserirEndereço("rua eponina", 295)
cliente1.listar_endereço()