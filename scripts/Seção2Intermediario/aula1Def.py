
# Deve-se usar as funções para tarefas que vao se repitir frequentemente

def teste(nome1, nome2): # cria a função a adiciona os parametros para a mesma
    print(f"Ola {nome1} e {nome2}")


teste("Derek", "Vitoria") # executa a função criada, substituindo os parametros

'''

variaveis criadas dentro das funções, funcionam apenas para dentro das funções, elas não afetam o lado de fora
para fazer uma variavel funcionar  no script inteiro basta usar:
'''
x = 0

def mudarx():
    global x
    x = 11
    print(x)


mudarx()

# return serve para "retornar" algo dentro da função para salvar como variavel, e tambem encerra a função

def teste():
    return 1 + 1

soma = teste()
print(soma)