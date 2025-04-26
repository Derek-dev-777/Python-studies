

class Multiplicar:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        print(*args, **kwds)
        return self.func(*args,**kwds)
        


@Multiplicar
def soma(x, y):
    return x + y


dois_mais_dois = soma(2,2)
print(dois_mais_dois)

#para usar uma decorator class, precisa-se usar a semantica igual a acima, e passar um call para a classe
# se não nao iria funcionar, ( se isso é util eu n tenho ideia)