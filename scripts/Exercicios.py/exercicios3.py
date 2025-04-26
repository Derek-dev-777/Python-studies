# calcular a area de um circulo

def calcular_area(valor):
    pi = 3.14
    try:
        raio_float = float(valor)
        conta = pi * (raio_float ** 2 )
        print(f"A area do seu circulo é igual a {conta:.2f}")
    except ValueError:
        print("Error, digite novamente")

while True:
    raio = input("Digite o raio para saber a area do circulo: ")
    calcular_area(raio)