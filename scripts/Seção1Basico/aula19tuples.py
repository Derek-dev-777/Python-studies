
nome1, *resto = ["maria", "cenoura", "Derek"]
_, nome2, *_ = ["amor", "Abacate", "alface"] # os _ servem para guardar espaço na variavel, ignore
                                             # o asterisco serve para pegar todas os outros objetos na lista

print(nome1, resto)


#tuple sao listas mas sem cochetes, usar apenas quando nao for acontecer mudanças na lista  

lista = ["maria", "Derek"]
lista_enumerada = list(enumerate(lista)) # esse comando numera cada objeto na lista na ordem, (1,2,3 etc)

print(lista_enumerada)