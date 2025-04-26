# Exercicio de escola, pegar nome dos alunos e fazer a media deles, mostrar separadamente


while True:

    def somarmedia(notas):
        soma = 0
        for i in notas:
            soma += i
        return soma / len(notas)
    

    escola = []
    notas = []

    for i in range(10):
        nome = input("Digite o nome do aluno: ")
        for i in range(4):
            nota = float(input("Digite a nota do aluno: "))
            notas.append(nota)
        media = somarmedia(notas)
        adicionar_dict = {"nome": nome, "nota": media}
        escola.append(adicionar_dict)

        notas.clear()
        print(escola)

    for i in escola:
        print(escola)

#escola_aluno = {"nome": "Ana", "nota": 10,}
#escola_aluno2 = {"nome": "derek", "nota": 5,}
#escola.append(escola_aluno)
#escola.append(escola_aluno2)
