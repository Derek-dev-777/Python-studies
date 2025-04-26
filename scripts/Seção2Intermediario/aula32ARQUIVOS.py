# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = "C:\\Users\\kaver\\OneDrive\\Área de Trabalho\\Python Scripts\\scripts\\Seção2Intermediario"
caminho_arquivo += "aula32.txt"


#arquivo = open(caminho_arquivo, "w")
#arquivo.close() # exemplo de sintaxe para abrir um arquivo
# a sintaxe abaixo funciona passando o caminho do arquivo, logo em seguida utilizando uma "key" que significa
#algo que esta la em cima w = escrita r = leitura etc etc
with open(caminho_arquivo, 'w+', encoding="utf-8") as arquivo: # as ( ai você escolhe como vai ser chamado esse arquivo)
    arquivo.write("Atenção\n") # write serve para escrever algo no arquivo
    arquivo.write("linha 2\n")
    arquivo.writelines(                 # writelines escreve multiplas linhas
        ("linha 3 \n", "linha 4 \n")
    ) 
    print("Arquivo fechando")

with open(caminho_arquivo, 'r') as arquivo: # R ja é comando de leitura
    print(arquivo.read())        # read le tudo que esta no arquivo
    print("Arquivo fechando")

# o W sempre quando executado, apaga tudo do arquivo e re-escreve com suas funções, tendo q tomar cuidado ao utilizar
#o A tambem sendo um comando de escrita, ele NÃO apaga oq ja estava no arquivo, ele adiciona no fim ( append )
# encoding é o estilo do teclado, UTF-8 seria o padrao para mostrar caracteres normal em strings

