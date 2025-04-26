
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nacismento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa("Derek", 20)

ano_nascimento = p1.get_ano_nacismento()
print(ano_nascimento)
print(vars(p1))
print(p1.__dict__) # ambos os comandos, vars e dict mostram tudo que está salvo na sua classe de intancia

# Assim você poderia salvar esses dados em uma variavel:

dados_p1 = vars(p1)

print(dados_p1)

# não é possivel passar dados como p1 na linha 12, diretamente para uma lista, deve usar vars() antes ou dentro
        