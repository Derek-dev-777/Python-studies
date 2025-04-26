#Calculo de olerite

def descontoIR(x):
     final = x - (x * 11 / 100)

     return x - final

def descontoINSS(x):
     final = x - (x * 8 / 100)

     return x - final

def descontoSINDICATO(x):
     final = x - (x * 5 / 100)

     return x - final

def somaDescontos(salario, inss, ir, sindicato):
     soma = inss + ir + sindicato

     return salario - soma



def calcular_salario_mes(valorhoras, horastrabalhadas):
    return valorhoras * horastrabalhadas

while True:
    horas_trabalhadas = float(input("Digite quantas horas você trabalhou esse mês: "))
    quanto_ganha_hora = float(input("Agora digite quanto você ganha por hora: "))

    salario = calcular_salario_mes( horas_trabalhadas, quanto_ganha_hora)
    desconto_imposto_renda = descontoIR(salario)
    desconto_inss = descontoINSS(salario)
    desconto_sindicato = descontoSINDICATO(salario)
    liquido = somaDescontos(salario, desconto_sindicato, desconto_imposto_renda, desconto_inss)

    print(f"Salario bruto: {salario}")
    print(f"IR (11%): {desconto_imposto_renda}")
    print(f"INSS (8%): {desconto_inss}")
    print(f"Sindicato (5%): {desconto_sindicato}")
    print(f"Salario Liquido: {liquido}")