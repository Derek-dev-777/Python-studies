"""
P8) Escreva um programa que escaneia um valor em ponto flutuante. Em seguida,
 escaneie um segundo número e some ao número anterior, salve e imprima essa soma.
  Enquanto o número digitado for diferente de 0 o programa deverá continuar a soma de forma infinita. 
	Ex: Se o usuário digitar 1 2 3 4 5 0   o resultado será 3 6 10 15

"""
soma = 0
numero_um = float(input("Digite um numero de ponto flutuante: "))
numero_dois = float(input("Digite um segundo numero: "))

while numero_dois != 0:
    numero_um += numero_dois

    print(f"{numero_um}")
    
    numero_dois = float(input("Digite um segundo numero: "))

    

print(f"Programa encerrado, total da soma foi: {numero_um}")
    
