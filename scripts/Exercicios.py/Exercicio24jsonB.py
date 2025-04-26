import json

with open("ExercicioDados.json", "r") as arquivo:
    pessoa1 = json.load(arquivo)
    print(pessoa1)