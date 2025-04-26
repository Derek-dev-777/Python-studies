# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def calcularsalario(x, y):
    return x * y

while True:
    ganho_hora = input("Digite quanto você ganha por hora: ")
    horas_trabalhadas = input("Agora digite quantas horas você trabalhou no mês: ")
    try:
        ganho_hora = float(ganho_hora)
        horas_trabalhadas = float(horas_trabalhadas)
        total = calcularsalario(ganho_hora, horas_trabalhadas)
        print(f"Seu salario do mês é de {total:.2f}")

    except ValueError:
        print("Error algo deu errado")