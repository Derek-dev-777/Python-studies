hora = input("Digite a hora do momento atual: ")

try: # essa função checa se o usuario digitou um horario
    horaint = int(hora)
except:
    print("Você não digitou um horario.")


if horaint >= 0 and horaint <= 11:
    print("Bom dia")

elif horaint >= 12 and horaint <= 17:
    print("Boa tarde")

elif horaint >= 18 and horaint <= 23:
    print("Boa noite")