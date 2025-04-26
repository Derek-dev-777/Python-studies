
from pathlib import Path

caminho = Path.home() / "OneDrive" / "Área de Trabalho" / "Meus Textos"
caminho.mkdir(exist_ok=True)

for i in range(5):

    files = caminho / f"texto_{i}.txt"

    if files.exists:
        files.unlink
    
    files.touch

    with files.open("a+") as text_file:
        text_file.write(f"Este é o arquivo numero {i}")

print(f"Arquivos na pasta 'files': ")

for arquivos in caminho.iterdir():
    if arquivos.is_file():
        print(arquivos.name)
        print(arquivos.read_text())




        