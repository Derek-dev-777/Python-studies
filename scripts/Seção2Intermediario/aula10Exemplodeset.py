#Exemplo de uso de set

letras = set()

while True:
    letra = input("Digite uma letra")
    letras.add(letra.lower())

    if "l" in letras:
        print("Parabens você encontrou a letra misteriosa")
        break

    print(letras)