'''

exemplo de como usar um for:

lista = ["Derek", "meneghel"]

for nomes in lista:
PARA nomes NA LISTA
    print(nome)    esse comando irá mostrar cada nome na lista,isso servindo para qualquer coisa
                    se fosse uma variavel qualquer, ele mostraria as letras do objeto ( os idex )

basicamente a parte de "nomes" é uma variavel que o proprio for vai criar, entao o nome pode variar...

for i in range(9999): # esse comando gira um looping de acordo com o numero dentro do range
     
'''

lista = ["Derek", "Meneghel"]
indices = range(len(lista)) #conta quantos indices tem dentro da lista, usando o range


for nomes in indices: # o "nomes" deve sera o numero deles no range da variavel acima
    print(nomes, lista[nomes])
    