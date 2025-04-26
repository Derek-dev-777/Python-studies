# os + shutil - Mover, copiar e renomear arquivos
# Mover|renomear - shutil.move  | os.rename
# Apagar - os.unlink()
# Apagar diretorio recursivamente -> shutil.rmtree
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~') # mostra o caminho da "home" do meu computador
AREA_DE_TRABALHO = os.path.join(HOME,"OneDrive", "Área de Trabalho") # junta minha home com minha area de trabalho
PASTA_CURRICULOS = os.path.join(AREA_DE_TRABALHO, "Curriculos")
NOVA_PASTA = os.path.join(AREA_DE_TRABALHO, "Nova Pasta Exemplo") #criando o caminho da nova pasta que quero criar



os.makedirs(NOVA_PASTA, exist_ok=True) # CRIA UMA NOVA PASTA, E O EXISTS OK É PRA VERIFICAÇÃO

for curriculos in os.listdir(PASTA_CURRICULOS):
    caminho_origem = os.path.join(PASTA_CURRICULOS, curriculos)  # Caminho completo do arquivo
    caminho_destino = os.path.join(NOVA_PASTA, curriculos)  # Caminho destino

    shutil.copy(caminho_origem, caminho_destino)  # Agora sim, copia o arquivo certo
    print(f"Arquivo copiado: {curriculos}")




# essa aula permite que eu copie e manipule arquivos podendo escreve-los em diferentes formatos