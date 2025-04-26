#Calcular quilos de peixe para o joao pescador

def multa(x):
    return x * 4

    
def calculo(kg):
    if kg - 50 <= 0:
        return 0
    else:
        return kg - 50

while True:
    qtd_kg = float(input("Digite a quantidade de quilos de peixe que o senhor pescou: "))
    passou_ou_nao_passou = calculo(qtd_kg)
    preço_multa = multa(passou_ou_nao_passou)

    if passou_ou_nao_passou > 0:
        print(f"o senhor deve pagar R${preço_multa:.2f} de multa")
    else:
        print("O limite de peso está dentre a lei, o senhor não pagará multa")
        
            