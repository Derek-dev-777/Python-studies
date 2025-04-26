
# dict, uma lista onde você da uma "chave" por exemplo o nome ali, e em seguida
# da um valor a ela ( "nome": "derek,")
pessoa = {
    "nome": "Derek",
    "sobrenome": "Meneghel",
    "Telefone": 13988491360, 
    "idade": 18,
}

print(pessoa["nome"]) # aqui eu chamei a chave nome, então o programa me responde o valor de nome

# para adicionar uma chave e um valor no meio do codigo:

pessoa["endereço"] = 'Rua eponina'
# del pessoa[o que quiser], serve para deletar uma chave
print(pessoa)