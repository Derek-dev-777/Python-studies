# super pode te ajudar a não sobrepor uma função em uma classe

class A:

    def metodo(self):
        print("A")

class B(A):

    def metodo(self):
        print("b")

class C(B):

    def metodo(self):
        super(C, self).metodo # essa função faz com que quando eu CHAME a função metodo pela classe C, ele tambem
                                # puxe a função metodo da classe B, pois ambas estao se sobrepondo
        super(B, self) # agora eu estou chamando a função pela classe B, mas da classe A tambem
        print("c")

# agora caso você tenha uma função __init__ na sua classe main, se você fizer o mesmo init em uma classe abaixo
#o python era sobrepor esse primeiro init, fazendo com que você perca os atributos da classe main etc
# então deve se fazer assim:

class oi:
    def __init__(self, nome):
        self.nome = nome

class tchau(oi):
    def __init__(self, nome, adeus):
        super().__init__(nome)  # aqui eu estou puxando o init principal para essa função para que eu não perca
        