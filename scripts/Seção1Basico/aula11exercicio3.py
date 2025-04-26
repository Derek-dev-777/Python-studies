primeiro_nome = input("Digite seu primeiro nome")
letras = len(primeiro_nome) # checa quantas letras tem no nome

if letras <= 4:
    print("Seu nome é curto")

elif letras <= 6:
    print("Seu nome é normal")

elif letras >= 7:
    print("Seu nome é grande")
