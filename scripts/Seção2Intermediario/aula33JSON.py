
import json
from aula32ARQUIVOS import caminho_arquivo
# jason.dump sintaxe = (nome da variavel que quer botar no arquivo, nome do arquivo) assim você bota algo no arq
# jason.load(nome do arquivo), load serve para trazer algo do arquivo json de volta para o python   
pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open("aula33JSON.json", "w") as arquivo: # criando arquivo com .json
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) #ensure serve para formatar acentos etc
                                                        #ident serve para formatar o dict, deixando bonito no arq

with open("aula33JSON.json", "r", encoding="utf8") as arquivo:
    pessoa_json = json.load(arquivo)
    print(pessoa_json)