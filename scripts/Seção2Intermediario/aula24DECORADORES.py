#Um exemplo de validação, as funções devem servir apenas para um proposito, entao se eu quisesse fazer uma validação

# isso seria um decorador.. agora pra que usar eu não faço ideia

def validarsoma(funcao, x, y):
    def valida():
        if x < 0 or y < 0:
            raise ValueError(" X e Y não podem ser numeros negativos")
        return funcao(x,y)
    return valida

def soma(x, y):
    return x + y


x = validarsoma(soma, 5, 10)()
print(x)