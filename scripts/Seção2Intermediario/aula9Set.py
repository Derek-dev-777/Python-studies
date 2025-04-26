"""
Set funciona como se fosse uma sacola de mercado, quando você quer jogar tudo la dentro
e depois você vai buscar oq estiver dentro, só nao aceita dados repetidos
essa é a diferença dele para uma lista ou um dicionario
"""
# baseado em diagrama de ven
# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

s1.add("Derek") # add adiciona um dado ao seu set, apenas 1 por vez
s1.update(("Meneghel", 1,2,3)) #update serve para adicionar mais de 1 dado ao meu codigo
s1.discard ("Meneghel") #discard elimina um valor no set, tendo que passar O valor ao inves do indice
s1.clear() # limpa todo aquele set


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # a barra UNE os dois sets, não repetindo numeros em comum dentre os sets
s3 = s1 & s2  # o & junta apenas os items que estão presentes em AMBOS os sets
s3 = s1 - s2  # mantem os items presentes APENAS do primeiro set informado (s1)
s3 = s1 ^ s2  # mostra os items que estão presentes EM comum em AMBOS