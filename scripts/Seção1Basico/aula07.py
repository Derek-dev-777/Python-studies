nome = input("Digite seu nome: ")
encontre_letra = input("Digite a letra que quer encontrar: ")

if encontre_letra in nome:
    print(f"{encontre_letra} esta em {nome}")

else:
    print(f"{encontre_letra} não esta em {nome}")