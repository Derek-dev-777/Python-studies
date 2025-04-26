
nome = "Derek Meneghel"
peso = 62
altura = 1.80
imc = peso / (altura * altura)

print(nome, "Tem:", altura )
print("Pesa", peso, "KG, e seu IMC é de:", imc)

#tem como formatar string usando f antes da palavra

texto1 = f"meu nome é {nome}, tenho {peso} quilos e {altura:.2f} de altura"

print(texto1)

# ou então assim, usando o .format

texto2 = "meu nome é {}, peso {} quilos e tenho {} metros" .format(nome, peso, altura)
print(texto2)