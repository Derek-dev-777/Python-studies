

def converter(x):
    return (x * 9/5) + 32

while True:
    temperatura = input("Digite a temperatura em graus celsius: ")
    try:
        temperatura = int(temperatura)
        convertido = converter(temperatura)
        print(f"A sua temperatura convertida é igual a {convertido}")
    except ValueError:
        print("Algo deu errado, tente novamente")
