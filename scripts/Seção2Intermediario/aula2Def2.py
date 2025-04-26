

def soma(*args):
    total = 0
    for numeros in args:
        total = total + numeros
    
    return total


soma1 = soma(1, 2, 3, 4, 5)
print(soma1)
soma2 = soma(5, 19, 28, 30)
print(soma2)