# Continuando do modulo anterior

#como criar uma pasta... basta passar o caminho do local onde se quer essa pasta
from pathlib import Path
caminho_pasta = Path.home() / "OneDrive" / "Área de Trabalho" / "Minha nova pasta"

caminho_pasta.mkdir(exist_ok=True) #.mkdir, cria uma pasta (diretorio), diferente do .touch que cria arquivo
# o exist_ok, é para caso seja executado dnv, para não ter problemas pois a pasta ja existe

#posso criar subpastas para essa pasta:

subpasta = caminho_pasta / "Subpasta"
subpasta.mkdir(exist_ok=True)

#e dentro dessa pasta irei criar um arquivo:

arquivo = subpasta / "Arquivo.txt"
arquivo.touch()
arquivo.write_text("isso é um teste")

# um exemplo com logica de como criar aquivos
files = caminho_pasta / "files"
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f"file_{i}.txt" # passando o caminho dos files, e enumerando eles de acordo com o range

    if file.exists():
        file.unlink()
    else:
        file.touch # uma pequena logica para não travar o pc, se o arquivo ja existir, apague ele, se não, crie

    with file.open("a+") as text_file:
        text_file.write("olá mundo")
        text_file.write(f"Eu sou o file_{i}")

print("\nArquivos na pasta 'files':")
for arquivo in files.iterdir(): #Lista tudo que tem na pasta (arquivos e pastas)
    if arquivo.is_file(): # se o arquivo for um file faça
        print(arquivo.name) 
        print(arquivo.read_text())