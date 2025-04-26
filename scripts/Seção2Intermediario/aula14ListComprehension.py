# List compreehension

# você esta acostumado a fazer listas assim:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mas você pode fazer isso
# você pode passar QUALQUER logica na ESQUERDA, antes do for, basicamente você fala pro python
# "Na lista eu quero adicionar os numeros", então você começa a logica
#----------------------------------------------------------------------------------
# mapeamento com modificações na lista

lista2 = [numero for numero in range(11)]
print(lista2)

novos_produtos = [
    {"produto": "batata frita", "Preço": 5},
    {"produto": "tomate", "Preço": 2},
    {"produto": "oleo", "Preço": 7},
    {"produto": "sabao em po", "Preço": 12}
]
# lembrando que tudo é feito A ESQUERDA do for
produtos = [
    {**produto, "Preço": produto["Preço"] * 1.05} # aumenta o preço dos produtos em 5%
    if produto["Preço"] > 1 else {**produto} # faz uma codição para filtrar o aumento dos preços
        for produto in novos_produtos] 

print(*produtos, sep = "\n")

# ----------------------------------------------------------------------------------------------------

# Filtro de dados em list comprehension

lista_numeros = [numero for numero in range(10) if numero < 5] # o filtro vindo apos o for

print(lista_numeros)

teste = [
    (x, y) for x in range(3)
            for y in range(3)
]

print(teste)
"""
Resumo, mapeamento seria transferir uma lista para outra lista alterando ou não os valores dela
dando condições A ESQUERDA do for

já o filtro, seria o mesmo de filtrar essa transferencia de lista, usando IFs apos o for, montando toda a logica
em poucas linhas.
"""
