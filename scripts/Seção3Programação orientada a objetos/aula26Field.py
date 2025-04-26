
from dataclasses import dataclass,field
# field tem umas utilidades ai, tem q dar uma explorada
@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    nome: str = field(
        default='MISSING', repr=False # se não tiver atribuido algo, o field passa "missing"
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list) # aqui o field faz com que quando chamado gere uma lista vazia