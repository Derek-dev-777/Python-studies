
while True:
    numero1 = input("Digite um numero: ")
    numero2 = input("Digite outro numero: ")
    operador = input("Digite um operador (+-*/): ")
    numeros_verificados = None
    numero1_verificado = 0
    numero2_verificado = 0


    try:
        numero1_verificado = float(numero1)
        numero2_verificado = float(numero2)
        numeros_verificados = True

    except:
        numeros_verificados = None

    if numeros_verificados == None:
        print("Um dos numeros não foi descrito corretamente, tente novamente.")
        continue
    
    operador_verificado = "+-*/"

    if operador not in operador_verificado:
        print("O operador digitado não foi reconhecido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    if operador == "+":
        print(numero1_verificado + numero2_verificado)

    if operador == "-":
        print(numero1_verificado - numero2_verificado)

    if operador == "*":
        print(numero1_verificado * numero2_verificado)

    if operador == "/":
        print(numero1_verificado / numero2_verificado)

    sair = input("Deseja [s]air? ").lower().startswith("s")

    if sair == True:
        break