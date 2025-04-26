# você pode adiar funções assim, imagine que você quer fazer uma soma de 2 numeros.
# seu cliente te enviou 1 numero só e você precisa deixar esse numero guardado em na função adiando ela
# e depois ele vem e te envia o outro numero

def somar(numero1):

    numero = numero1 # estou definindo uma variavel, o "numero" será o parametro que o usuario digitar
    def soma(numero2): # outra função para pegar o numero 2
        nonlocal numero # numero deixa de ser uma variavel local
        numero += numero2 # aqui eu somei o primeiro numero com o 2 numero que vai ser enviado
        return numero # retornamos o numero somado, para a função soma
    return soma # e aqui retornamos a a soma para a função principal "somar"

primeiro_numero = somar(5) # aqui eu guardei o primeiro numero, podendo ser algo que foi enviado bla bla

print(primeiro_numero(10)) # e aqui eu informei o segundo numero
    