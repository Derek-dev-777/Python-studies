# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

from Aula10FormatandoBytes import formata_tamanho
import os
from itertools import count

caminho = r"C:\Users\kaver\OneDrive\Área de Trabalho\Python Scripts" # formatando o caminho
counter = count() # cria um countador

for root, dirs, files in os.walk(caminho): # diretorio(pastas), arquivos dentro das pastas, arquivos
    the_counter = next(counter) # inicializa o contador
    print(the_counter,root) # printa as pastas

    for dir_ in dirs: # e dentro de cada pasta, ele localiza os arquivos dentro delas
        print("     ", the_counter, dir_)

    for files_ in files:# e dentro de cada dirs, ele localiza os arquivos
        tamanho_arquivo_completo = os.path.join(root,files)
        stats = os.stat(tamanho_arquivo_completo)
        tamanho = stats.st_size
        print("     ", the_counter,files_,formata_tamanho(tamanho_arquivo_completo))

    #os.unlink(aqui dentro você coloca o caminho de algum arquivo)
    #o comando acima DELETA tudo que estiver no caminho colado, tem q tomar cuidado para usar

# resumo da aula, você pode navegar dentro das pastas usando o os.walk, basta seguir a semantica acima