# Dict and set comprehension
# DICT comprehension exemplos ABAIXO

produto = {
    "nome": "Caneta Azul",
    "preço": 2.5,
    "categoria": "Escritorio",
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # isintance = se (o valor, for string faça tal.)
    for chave, valor in produto.items()
    if chave != "nome" # um filtro, adicionando apenas as chaves que forem diferente de "nome" 
} 

print(dc, sep="\n")
# ------------------------------------------------------------------------------------------------
#Set comprehension exemplos abaixo

set1 = {2 * i for i in range(10)}
print(set1)