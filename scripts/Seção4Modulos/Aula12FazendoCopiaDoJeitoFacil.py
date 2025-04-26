# os + shutil - Mover, copiar e renomear arquivos
# Mover|renomear - shutil.move  | os.rename
# Apagar - os.unlink()
# Apagar diretorio recursivamente -> shutil.rmtree
# COpiar Arvore recursivamente -> shutil.copytree
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~') # mostra o caminho da "home" do meu computador
AREA_DE_TRABALHO = os.path.join(HOME,"OneDrive", "Área de Trabalho") # junta minha home com minha area de trabalho
PASTA_CURRICULOS = os.path.join(AREA_DE_TRABALHO, "Curriculos")
NOVA_PASTA = os.path.join(AREA_DE_TRABALHO, "Nova Pasta Exemplo") #criando o caminho da nova pasta que quero criar

os.makedirs(NOVA_PASTA, exist_ok=True) # CRIA UMA NOVA PASTA, E O EXISTS OK É PRA VERIFICAÇÃO

shutil.copytree(PASTA_CURRICULOS,NOVA_PASTA, dirs_exist_ok=True) #faz a mesma coisa do codigo anterior só q facil