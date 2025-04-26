
lista = [355, "derek", True, 5643]
lista[1] = "Meneghel"
print(lista)
print(lista[1])

lista.append("Oi") # .append adiciona algo ao final da sua lista.
lista.pop() # esse comando remove o ultimo objeto da lista, ou oq estiver no indice dentro do parenteses
del lista[2] # deleta o objeto dentro da lista, evitar fazer isso quando a lista for muito grande pois lagga tudo
lista.clear(lista) # serve para limpar a lista desejada
lista.copy() # serve para copiar uma lista por inteira, podendo atribui-la em outra variavel/lista
lista.sort() #coloca a lista na ordem ( numeros etc)
lista.sort(reverse=True) # coloca a lista na ordem decrescente ( revertendo ela)