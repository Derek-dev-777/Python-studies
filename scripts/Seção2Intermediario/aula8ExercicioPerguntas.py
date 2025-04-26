
pontos = 0
perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "2", "3", "4"],
        "Resultado": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["10", "35", "20", "25"],
        "Resultado": "25",
    },
    {
        "Pergunta": "Quanto é 10+10?",
        "Opções": ["20", "50", "80", "100"],
        "Resultado": "20",
    }
]   

for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"]) # mostra todas as perguntas do dicionario
    print("") # da um espaço para ficar mais bonito
    opcoes = pergunta["Opções"]

    for i,opção in enumerate(opcoes): # esse for deixa as opções mais visivel no programa
        print(f"{i})",opção)
    
    escolha = input("Escolha uma opção: ")

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)


    if escolha.isdigit():
        escolha_int = int(escolha)  # aqui a gente trata para ver se foi digitado numero

    if escolha_int is not None: # se FOI digitado um numero
        if escolha_int >= 0 and escolha_int < qtd_opcoes: # confere se é maior q zero e menor q 3
            if opcoes[escolha_int] == pergunta["Resultado"]: 

                acertou = True
    if acertou:
        print("Acertou")
    else:
        print("Errou")
        
    

    

