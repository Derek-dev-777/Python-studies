from functools import reduce

produtos = [

    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 3", "preco": 22.32},
    {"nome": "Produto 1", "preco": 10.11},
    {"nome": "Produto 4", "preco": 105.87},
    {"nome": "Produto 2", "preco": 69.90},
]

def funcao_do_reduce(acumulador, produto):
    return acumulador + produto["preco"]

total = reduce(
    funcao_do_reduce, # primeiro passa a função que vai ser aplicada
    produtos, # depois na lista, ou dicionario que sera aplicada ( produto )
    0 # aqui é o valor inicial da função ( acumulador)
)
# essa função faz magica, é dificil entender
print(total)