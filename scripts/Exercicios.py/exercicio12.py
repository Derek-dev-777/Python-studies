# esse codigo aqui deu certo até certo ponto, mas quando envolveu uma logica de comparar galoes, cagou tudo
# falhei

import math

LATA_LITROS = 18
LATA_PRECO = 80
GALAO_LITROS = 3.6
GALAO_PRECO = 25

def precototal(x):
    return x * 80

def calcular_listros_usados(x):
    return x / 6

def lata_tinta18(litrosgastados):
    return math.ceil(litrosgastados / 18 )

def lata_tinta3(litrosgastados):
    return math.ceil(litrosgastados / 3.6)

def comparacao(litrosgastados):
    latas = litrosgastados / LATA_LITROS
    sobra = litrosgastados & LATA_LITROS
    galões = math.ceil(sobra / GALAO_LITROS)
    return int(galões), int(latas)



while True:
    tamanho_metros_quadrados = float(input("Digite os metros quadrados da area a ser pintada: "))
    quantos_litros_vai_usar = calcular_listros_usados(tamanho_metros_quadrados)
    latas_tinta =  lata_tinta18(quantos_litros_vai_usar)
    latas_mistura, galoes_mistura = comparacao(quantos_litros_vai_usar)

    print(f"com {tamanho_metros_quadrados}m², você irá usar {quantos_litros_vai_usar:.2f} litros de tinta.") 
    print("Cada lata de tinta, contem 18 litros e custa R$80,00 reais")
    print(f"e você precisará comprar {latas_tinta}, dando um total de: R${precototal(latas_tinta)} ")  
    print(f"Caso queira usar 2 tipos de galões você precisaria usar:")
    print(f"{latas_mistura} de 18L, e {galoes_mistura} de 3.6L")