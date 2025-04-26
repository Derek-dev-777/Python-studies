import json

lista_original = []
lista_reserva = []
elemento_desfeito = []

while True:

    for coisas in lista_original:
            print(f"- {coisas}")
    print("Comandos: listar, desfazer, refazer")
    comando = input("Digite uma tarefa ou um comando: ").lower()


    if comando == "listar":
        for coisas in lista_original:
            print(coisas)

    elif comando == "desfazer":
        try:
           elemento_desfeito =  lista_original.pop()
           lista_reserva.append(elemento_desfeito)
        except:
            print("Não há elementos para desfazer")

    elif comando == "refazer":
        if lista_reserva:
            lista_original.append(lista_reserva.pop())
        else:
            (print("Não a itens para refazer"))

    else:
        lista_original.append(comando)


    with open("ExercicioListaTarefa.json", "w", encoding="utf8") as arquivo:
        json.dump(lista_original, arquivo, indent=2)
