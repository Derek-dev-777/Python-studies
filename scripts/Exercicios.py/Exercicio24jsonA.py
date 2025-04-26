import json
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def anoNascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa("Derek", 20)
print(p1.nome)
dados_p1 = vars(p1)
print(dados_p1)

with open("ExercicioDados.json", "w",) as arquivo:
    json.dump(dados_p1, arquivo, indent=2)


        