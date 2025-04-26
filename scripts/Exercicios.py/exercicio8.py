# diversas funções baseadas em numeros dados pelo cliente

def somadotriplo(x, y):
    return (x * 3) + y

def produto_dobro(x, y):
    return (2 * x) * (y / 2 )

def terceirocubo(x):
    return x ** 3


while True:
    lista = []
    numero_int1 = int(input("Digite um numero inteiro: "))
    lista.append(numero_int1)
    numero_int2 = int(input("Digite outro numero inteiro: "))
    lista.append(numero_int2)
    numero_real = float(input("Agora digite um numero real ( float ): "))
    lista.append(numero_real)

    print(lista)

    primeiro_problema = produto_dobro(lista[0], lista[1])
    segundo_problema = somadotriplo(lista[0], lista[2])
    terceiro_problema  = terceirocubo(lista[2])

    print(f"Este é o produto do dobro com metade do segundo {primeiro_problema:.2f}")
    print(f"Essa é a soma do triplo do primeiro com o terceiro {segundo_problema:.2f}")
    print(f"Este é o cubo do terceiro numero {terceiro_problema:.2f}")
