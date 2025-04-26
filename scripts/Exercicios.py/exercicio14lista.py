lista = []
nome  = "Derek Meneghel"


for i in range(5):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

print(lista)

lista2 = []

for i in range(10):
    numero2 = float(input("Digite um numero: "))
    lista2.append(numero2)

print(lista2)
for item in reversed(lista2):
    print(item)