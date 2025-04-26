while True:

    Palavra_secreta = "banana"
    letra_digitada = input(" Tente adivinhar a palavra secreta, digite uma letra: ")
    

    if letra_digitada.isalpha():
        ...
    else:
        print("Voce não digitou uma letra, tente novamente.")
        continue


    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in Palavra_secreta:
        print(f" Você acertou a letra {letra_digitada} está na palavra!")
        tentativa_de_acertar = input("Gostaria de tentar acertar a palavra completa? Digite sim: ").lower().startswith('s')

        if tentativa_de_acertar == False:
            continue
        
        if tentativa_de_acertar == True:
           palavra_completa = input("Digite a palavra completa: ")

        if palavra_completa == Palavra_secreta:
            print("Parabens você acertou a palavra secreta!")
            break
        else:
            print("Você errou a palavra secreta, tente novamente!")
        
            continue

    if letra_digitada not in Palavra_secreta:
        print("Infelizmente você errou, tente novamente.")
    
        continue

    
    sair = input("Deseja sair do programa? digite s: ").lower().startswith('s')

    if sair == True:
        break
