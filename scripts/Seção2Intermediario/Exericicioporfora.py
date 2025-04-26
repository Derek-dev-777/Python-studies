import random

numero_aleatorio = random.randrange(0,100)
print(numero_aleatorio)
numero_tentativas  = 0
print("Tente adivinhar o numero aleatorio de 0 a 100")

while True:
    
    tentativa = input("Digite um numero: ")
    tentativa_int = None

    if tentativa.isdigit():
        tentativa_int = int(tentativa)
    
    if tentativa_int is not None:
        if tentativa_int > 100:
            print("Você digitou um numero maior que 100")
            
        if tentativa_int > numero_aleatorio:
            print("Tente um numero menor")
            numero_tentativas += 1
        elif tentativa_int < numero_aleatorio:
            print("Tente um numero maior")
            numero_tentativas += 1
        elif tentativa_int == numero_aleatorio:
            print("Parabens, Você acertou o numero exigido")
            print(f"Quantidade de tentativas {numero_tentativas}")
            break
    else:
        print("Você não digitou um numero.")

