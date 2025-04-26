# calcular peso ideal para homem e mulher

def calculohomem(x):
    return (72.7 * x) - 58

def calculomulher(x):
    return (62.1 * x) - 44.7

while True:
    mulher_ou_homem = input("Você é homem ou mulher? digite M para mulher e H para homem: ").lower().startswith("h")
    altura = float(input("Digite sua altura e vamos calcular seu peso ideal: "))
    if mulher_ou_homem == True:
        peso_ideal = calculohomem(altura)
        print(f"Seu peso ideal é de {peso_ideal:.2f}")
    else:
        peso_ideal = calculomulher(altura)
        print(f"Seu peso ideal é {peso_ideal:.2f}")