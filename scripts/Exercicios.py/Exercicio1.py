#Exercicio fazer media de notas

notas = []

def media(colocarnotas):
    soma = 0 # variavel para acumular o valor da soma das notas
    for numero in colocarnotas: # para cada numero na lista de notas
        soma += numero     # faz a soma do acumulador + numero digitado, fazendo um looping 
        
    return soma / len(colocarnotas)

 
for i in range(4):
    digite_nota = input("Digite sua nota: ")
    digite_nota_int = int(digite_nota)
    notas.append(digite_nota_int)

print(f"Notas inseridas {notas}")

mostrar_media = media(notas)

print(f"sua media foi igual a {mostrar_media}")