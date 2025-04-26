
#exemplo de closure

def criar_saudacao(saudacao): # função principal de saudação
    def saudar(nome): # salvar o nome
        return f"{saudacao}, {nome}" # retornar essa frase para o "saudar"
    return saudar # retornar oque tiver em "saudar" para o "criar saudação"

criar_boa_noite = criar_saudacao("Boa noite")
criar_bom_dia = criar_saudacao("Bom dia")

for nome in ['Derek', 'Maria', 'Vitoria']:
    print(criar_bom_dia(nome))
    print(criar_boa_noite(nome))

