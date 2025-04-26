numeros = []
numeros_par = []
numeros_impar = []
def par_impar(x):
    if x % 2 == 0:
        numeros_par.append(x)
    else:
        numeros_impar.append(x)


for i in range(20):
    numero_digitado = int(input(f" {i} - Digite um numero: "))
    numeros.append(numero_digitado)
    par_impar(numero_digitado)

print(f"numeros da lista total : {numeros}")
print(f"numeros pares: {numeros_par}")
print(f"numeros impares: {numeros_impar}")
