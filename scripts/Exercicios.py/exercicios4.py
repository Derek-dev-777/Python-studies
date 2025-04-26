#  calcular a area de um quadrad, e mostrar o dobro ao usuario
def calculardobro(largura, comprimento):
    return 2 * (largura * comprimento)



while True:
    metro_ou_centimetro = input("Você vai usar metros ou centimetros como medida? M ou C").lower().startswith("m")
    print(metro_ou_centimetro)
    if metro_ou_centimetro == True:
        comprimento = input("Digite o comprimento do seu quadrado em metros: ")
        largura = input("Digite a largura do seu quadrado em metros: ")
        try:
            comprimento = float(comprimento)
            largura = float(largura)
            dobro_da_area = calculardobro(comprimento, largura)
            print(f"o dobro da area do seu quadrado é igual a {dobro_da_area:.2f}")
        except ValueError:
            print("Error, algo deu errado tente novamente")
    else:
        comprimento = input("Digite o comprimento do seu quadrado em centimetros: ")
        largura = input("Digite a largura do seu quadrado em centimetros: ") 
        try:
            comprimento = float(comprimento)
            largura = float(largura)
            dobro_da_area = calculardobro(comprimento, largura)
            print(f"o dobro da area do seu quadrado é igual a {dobro_da_area:.2f}")
        except ValueError:
            print("Error, algo deu errado tente novamente")
