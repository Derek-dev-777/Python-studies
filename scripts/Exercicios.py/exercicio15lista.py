
def calcularmedia(lista):
    soma = 0
    for nota in lista:
        soma += nota
    return soma / len(lista)



lista = []

for i in range(4):
    nota = float(input("Digite sua nota: "))
    lista.append(nota)

media = calcularmedia(lista)

print(f"A media das notas foi de {media}")
