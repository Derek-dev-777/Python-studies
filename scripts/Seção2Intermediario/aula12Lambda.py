lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()

# essa linha de comando, LAMBDA serve como se fosse um DEF, mas em uma linha só e sem nome
# traduzindo fica, sorted = ordene, então passa o parametro LISTA, com a key=lambda para indicar uma função
# e o parametro dessa função sendo ITEM, então definindo esse parametro como "nome"/"sobrenome"
# assim ordenando 2 listas, um pelos nomes e a outra pelo sobrenome, uma função inteira em 1 linha
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)