
def achar_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    return palavra_invertida == palavra

palavra = "arara"

print(achar_palindromo(palavra))

aumento_vendas = 32.048701

print(f"O aumento das vendas nesse mes foi de %{aumento_vendas:.2f}")