
from zipfile import ZipFile
from pathlib import Path
import os
# CAMINHOS PARA USAR NO CODIGO

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_PASTA_ZIP = CAMINHO_RAIZ / "Aula27PastaZip" # caminho onde eu criarei meus arquivos
CAMINHO_COMPACTADO = CAMINHO_RAIZ / "Aula27_compactado.zip" # caminho onde os meus arquivos serao compactados
CAMINHO_DESEMPACOTADO = CAMINHO_RAIZ /"Aula27Desempacotando"

CAMINHO_PASTA_ZIP.mkdir(exist_ok=True) # crio a pasta dos arquivos
CAMINHO_DESEMPACOTADO.mkdir(exist_ok=True) # crio a pasta onde irei desempacotar
#------------------------------------------------------------------------------------------------------------

#   Função para criar os arquivos
def criar_arquivos(qtd, caminho):
    for i in range(qtd):
        novo_arquivo = caminho / f"arquivo{i}.txt"
        nome_arquivo = f"arquivo{i}.txt"

        if novo_arquivo.exists():
            novo_arquivo.unlink()
        else:
            novo_arquivo.touch()

        with open(novo_arquivo, "a+") as arquivo:
            arquivo.write(nome_arquivo)


criar_arquivos(10, CAMINHO_PASTA_ZIP) # criando os arquivos
#------------------------------------------------------------------------------------------------------------

#   Empacotando meus arquivos da pasta zip, no caminho compactado ( .zip)
#   Ou seja, todos os arquivos criados na pasta zip, vao ser compactados dentro deum arquivo.zip

with ZipFile(CAMINHO_COMPACTADO, "w") as zip:
    for roots, dirs, files in os.walk(CAMINHO_PASTA_ZIP):
        for file in files:
            
            zip.write(os.path.join(roots, file), file) 
#------------------------------------------------------------------------------------------------------------

# Desempacotando os arquivos que estão empacotados no .zip

with ZipFile(CAMINHO_COMPACTADO, "r") as zip:
    zip.extractall(CAMINHO_DESEMPACOTADO)



