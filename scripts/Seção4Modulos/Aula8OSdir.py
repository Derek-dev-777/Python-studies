# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO') # um exemplo de caminho

for pasta in os.listdir(caminho): # para cada pasta dentro do caminho
    caminho_completo_pasta = os.path.join(caminho, pasta) # ai você tem q juntar o caminho + as pastas
    print(pasta) # aqui ele simplesmente printa as pastas

    #abaixo é uma verificação, pois temos arquivos q nao sao vistos e causam error nesse codigo
    if not os.path.isdir(caminho_completo_pasta): # se nao for o caminho completo
        continue

    # apos a verificação, ai você pode passar por dentro de cada arquivo dentro dessa pasta :)
    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)