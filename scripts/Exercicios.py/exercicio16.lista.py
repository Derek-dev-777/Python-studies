
lista = []
vogais = ["a", "e", "i", "o", "u"]
consoante = 0
consoantes = []

for i in range(10):
    letra = str(input(f"{i} - Digite uma letra: ")).lower()
    print("")
    lista.append(letra)

for letra in lista:
    if letra in vogais:
        print(f"{letra} é uma vogal")
        print("")
    else:
        consoante += 1
        consoantes.append(letra)
        print(f"{letra} é uma consoante")
        print("")
print(f"Temos {consoante} consoantes em sua lista.!")
print(consoantes)



