palavras = ["python", "asimov", "código", "web", "programação"]

menor_palavra = palavras[0]
maior_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    elif len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print(f"A menor palavra é {menor_palavra}")
print(f"A maior palavra é {maior_palavra}")