# Combinations, Permutations e product
# combinação - ordem não importa - iteravel + tamanho do grupo (list(combination(variavel, numero de combinações)))
# Permutação - ordem importa
# produto -  Ordem importa e repete valores unicos

from itertools import combinations, permutations, product

pessoas = [
    "joao", "joana", "Derek", "vitoria"
]

camisetas = [
    ["preta", "branca"],
    ["m", "p", "g"],
    ["Masculina", "Feminina"],
]   
                                #grupo de 2, vc pode alterar esse valor para mudar os grupos
print(list(combinations(pessoas, 2)))

print(list(permutations(pessoas, 2))) # nesse ele repete grupos que ja foram ditos, mas com a ordem trocada

print(list(product(*camisetas)))