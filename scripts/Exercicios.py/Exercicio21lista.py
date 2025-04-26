
pessoas = []

for i in range(5):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    nome = input("Digite seu nome: ")
    adicionar_dict = {"nome": nome,"idade": idade, "altura": altura}
    pessoas.append(adicionar_dict)
    print(*pessoas)

for pessoa in reversed(pessoas): # mostrar coisas ao contrario
    print(pessoa)