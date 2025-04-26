# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
# ou seja, se eu atribuir uma classe a alguma variavel, eu posso simplesmente chama igual o codigo abaixo
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        


call1 = CallMe('23945876545')
call1("Derek")