# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

# aqui criamos um tipo chamado "direcoes", e nele atribuimos atributos como "ESQUERDA", "DIREITA"
direcoes = enum.Enum("direcoes", ["ESQUERDA", "DIREITA"]) 

# meios de chamar valores dentro de enum tipos
print(direcoes(1), direcoes["ESQUERDA"], direcoes.ESQUERDA)


def mover(direcao):
    if not isinstance(direcao, direcoes): # se a instancia colocada no parametro da função nao for direçoes.
        raise ValueError("Direção nao encontrada")
    
    print(f"movendo para {direcao}")


mover(direcoes.ESQUERDA)
mover(direcoes.DIREITA) # aqui chamamos nosso tipo direcoes
