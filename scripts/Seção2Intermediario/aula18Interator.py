# exemplo de iterable

# Uma lista é um iterable porque podemos percorrê-la com um for:

numeros = [1, 2, 3]  # Lista é um Iterable

for num in numeros:
    print(num)

#--------------------------------------------------
#exemplo iterator

# Podemos criar um Iterator usando iter() e avançar com next():

numeros = [1, 2, 3]  
it = iter(numeros)  # Criando um Iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # Erro! Acabou os itens


