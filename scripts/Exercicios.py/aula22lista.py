def quadrado(a):
    return a * a

def somar(a):
    soma = 0 
    for numero in a:
        soma += numero
    return soma
lista_A = []

for i in range(10):
    numero = int(input(f"{i}- Digite um numero: "))
    numero_ao_quadrado = quadrado(numero)
    lista_A.append(numero_ao_quadrado)
    print(lista_A)

somatoria = somar(lista_A)
print(f"Esta é a soma do quadrado dos numeros: {somatoria}")
