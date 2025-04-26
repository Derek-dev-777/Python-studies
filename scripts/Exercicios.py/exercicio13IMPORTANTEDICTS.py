from copy import deepcopy

def aumentar10(lista):
    for produto in lista:
        produto["preco"] *= 1.1


produtos = [

    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 3", "preco": 22.32},
    {"nome": "Produto 1", "preco": 10.11},
    {"nome": "Produto 4", "preco": 105.87},
    {"nome": "Produto 2", "preco": 69.90},
]
aumentar10(produtos)

novos_produtos = deepcopy(produtos) # primeira deepcopy

ordenado = sorted(novos_produtos, key=lambda nome: nome["nome"],reverse=True)

preco_ordenado = sorted(ordenado, key=lambda preco: preco["preco"])

for i in preco_ordenado:
    print(i)

