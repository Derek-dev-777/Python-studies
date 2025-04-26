numero_usuario = input("Digite um numero: ")

try:
    numero_usuario_int = int(numero_usuario)
    print("Você digitou um numero inteiro")
except:
    print("O numero digitado não é um numero inteiro") # checagem para ver se o usuario digitou um numero ou uma string

par_impar = numero_usuario_int % 2 # formula para achar numeros pares ou impares

if par_impar >= 1:
    print(f"{numero_usuario_int} é impar")

else:
    print(f"{numero_usuario_int} é par") # checagem e conclusão se o numero é par ou impar