nome = input("Digite seu nome: ")
idade  = input("Digite sua idade: ")

if nome and idade:
    print(f"seu nome é: {nome}")
    print(f"seu nome invertido é: {nome[::-1]}") # mostra nome invertido basta por o -1

    if " " in nome: # Checa se o nome tem espaços ou não
        print(f"Seu nome tem espaços")
    else:
        print("seu nome nao contem espaços")
    
    print(f"Seu nome tem {len(nome)} letras") # a função len conta quantas letras tem no nome
    print(f"A primeira letra do seu nome é {nome[0]}") # essa digitação mostra a primeira letra do nome ( começa em 0 )
    print(f"A ultima letra do seu nome é {nome[-1]}") # essa digitação mostra a ultima letra do nome
else:
    print(" Você deixou os campos vazios")


    if idade.isdigit():
        ...