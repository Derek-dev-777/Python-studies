#converter metros em centimetros

def converter_metros(metros):
    return metros * 100
while True:
    metros = input("Digite os metros: ")
    try:
        metros_convertido = float(metros)
        convertido = converter_metros(metros_convertido)
        print(f"{metros} é igual a {convertido:.3f} centimetros")
    except ValueError:
        print("Você não digitou um numero")

    convertido = converter_metros(metros_convertido)
    
