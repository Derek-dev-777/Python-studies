# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple 
# vc pode importar outras coisas de dataclasses tambem

@dataclass
class Pessoa: # ao inves de usar init, repr, bla bla, basta eu passar a variavel e q tipo eu quero dentro dela
    nome: str
    idade: int

    def __post_init__(self): # post init, ele inicia depois do init, ent vc pode fazer algo com isso talvez
        self.nome_e_idade = f"{self.nome} {self.idade}"


    @property
    def nome_e_sobrenome(self):
        return f'{self.nome} {self.idade}'
    
    @nome_e_sobrenome.setter
    def nome_e_sobrenome(self, valor): # você pode utilizar metodos como se fosse uma função padrao
        ...
if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Luiz', 30)
    print(p1 == p2)
    print(asdict(p1))