# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# poderiamos fazer assim :
def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2)) # aqui com a função "min", ele identificou qual a menor lista
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))
# OU SIMPLESMENTE FAZER ISSO AQUI

print(list(zip(l1, l2))) # 09/02/2025, aqui estou eu mostrando minha indiganção pro futuro programador derek