from pathlib import Path

caminho_projeto = Path()

print(caminho_projeto.absolute()) # mostra meu caminho absoluto, mas não chega até o meu arquivo atual
# um meio para chegar até o caminho inteiro é:

caminho_arquivo = Path(__file__) # agora eu tenho o caminho COMPLETO do meu arquivo, funcional em todos sistemas
print(caminho_arquivo)

print(caminho_arquivo.parent) # igual no roblox, parent é oq vem acima do arquivo atual, ent nesse caso seria a 
# seção modulos e quanto mais .parents eu colocar, mais ele vai subindo na hierarquia..

#agora para criar pastas ou arquivos, basta eu dar o ponto de partida que eu quero criar e adicionar, veja:

ideias = caminho_arquivo.parent / "ideias" # aqui eu estou criando um pasta chamado ideias, na seção
print(ideias)
print(ideias / "arquivo.txt") # aqui eu ja estaria criando um arquivo dentro dessa pasta

arquivo = Path.home() / "OneDrive" / "Área de Trabalho" / "Arquivo.txt"
arquivo.touch() # passando o caminho do arquivo acima, e usando o .touch, eu CRIO o arquivo no caminho indicado
arquivo.unlink() # eu deleto esse mesmo arquivo
arquivo.write_text("Ola Mundo") # dentro desse arquivo eu escrevo a frase passada, infelizmente é só uma linha
print(arquivo.read_text()) #read_text, mostrara no print o que estiver escrito dentro do meu arquivo


# para escrever coisas dentro do arquivo do jeito certo, temos que:

with open(arquivo, "a+") as file:
    file.write("oba oba")
    file.write("oba oba 2")

print(arquivo.read_text()) # leria oq estiver dentro do arquivo
                                                  