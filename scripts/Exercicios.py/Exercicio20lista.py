
lista_numeros = []

def soma_numeros(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma
    
def multiplicar_numeros(lista):
    soma = 1
    for i in lista:
        soma *= i
    return soma
    
for i in range(5):
    numero_digitado = int(input(f"{i} - Digite um numero: "))
    lista_numeros.append(numero_digitado)

multiplicacao = multiplicar_numeros(lista_numeros)
soma = soma_numeros(lista_numeros)

print(f"Esses são os numeros que você digitou: {lista_numeros}")
print(f"Essa é a soma de todos os numeros da lista: {soma}")
print(f"Essa é a multiplicação de todos os numeros da lista: {multiplicacao}")
