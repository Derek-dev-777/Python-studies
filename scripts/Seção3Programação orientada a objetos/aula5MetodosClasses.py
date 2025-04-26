# Metodos de classe e factories (fabricas)
# são metodos onde o "Self" será "cls", ou seja,
# ao invês de receber a instancia primeiro parametro,
#receberemos a propria classe

class Pessoa:

    ano_atual = 2024  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls): # exemplo 1,essa sintaxe ( cls e class method) fazem com que eu possa acessar este metodo
        print("hey")           # diretamente do objeto, por exemplo a baixo

    @classmethod
    def criar_idade_50(cls, nome): # exemplo 2damos um parametro para por o nome
        return cls(nome, 50) # no retorno, hard codamos a idade 50, podendo ser chamada assim: 
    
    @classmethod
    def criar_anonimo(cls, idade): # exemplo 3, parametro para idade, pois o nome eu irei hard codar
        return cls("anonimo", idade) # no retorno, hard codamos o nome, e a idade virá pelo usuario na chamada

p1 = Pessoa("derek", 20)
Pessoa.metodo_de_classe() # assim. exemplo 1 

p2 = Pessoa.criar_idade_50("Derek") # exemplo 2
print(p2.nome, p2.idade) #exemplo 2

p3 = Pessoa.criar_anonimo(25) #exemplo 3
print(p3.nome, p3.idade) #exemplo 3
