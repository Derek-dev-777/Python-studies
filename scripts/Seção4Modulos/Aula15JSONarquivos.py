import os
import json

NOME_ARQUIVO = 'aula15.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(  # meio de fazer um caminho absoluto no python
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

print(CAMINHO_ABSOLUTO_ARQUIVO)

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, "w") as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2) # manda o que tem na variavel filme pro arquivo( dump )

with open(CAMINHO_ABSOLUTO_ARQUIVO, "r") as arquivo: # tras oq tem dentro do arquivo para meu terminal(load)
    filme_json = json.load(arquivo)
    print(filme_json)