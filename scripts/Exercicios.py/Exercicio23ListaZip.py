
vetor1 = []
vetor2 = []

for i in range(10):
    numero1 = input(f"{i}- Digite um numero para o primeiro vetor: ")
    numero2 = input(f"{i}- Digite um numero para o segundo vetor: ")
    vetor1.append(numero1)
    vetor2.append(numero2)
    
print(list(zip(vetor1, vetor2)))