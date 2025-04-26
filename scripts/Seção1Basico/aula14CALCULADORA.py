


while True:
    numero1 = input("Digite um numero: ")
    numero2 = input("Digite outro numero: ")
    operador = input("Digite um operador (+-*/): ")
#    ^^ pergunta os dados ao usuario
    numeros_validos = None # flag para checar se os numeros sao validos
    num1 = 0
    num2 = 0

    try:
        num1= float(numero1)
        num2 = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Algo deu errado, desculpe.")
        continue

#    ^^^^^ função para checar se os numeros sao validos

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("O operador escolhido é invalido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
#   ^^^^ checa se o operador foi digitado certo
    print("Veja o resultado")

    if operador == "+":
        print(num1 + num2)
    if operador == "-":
        print(num1 - num2)
    if operador == "/":
        print(num1 / num2)
    if operador == "*":
        print(num1 * num2)
    sair = input("Quer sair? [s]sim ").lower().startswith("s")
    
    if sair == True:
        break
