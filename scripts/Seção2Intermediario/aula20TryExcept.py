#Try, Except, else e finally

 #(Parte1) try e except para tratar exceções, você deve mencionar o nome do error para trata-lo
# exemplo da estrutura dos 4 tipos juntos

try: # tente
    print("Abrir arquivo")
    8/0
except ZeroDivisionError: # exceção de tal error, tendo q informar o erro ao programa
    print("Dividiu zero")
else: # executara caso o script n tenha nenhum erro
    print("não teve error")
finally: # SEMPRE executara oq estiver abaixo, mesmo dando erro, mesmo caindo o mundo, isso sempre vai aparecer
    print("Acabou")







# exemplos de except
try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError as error: # as error envia qual error deu para a variavel, podendo ser manipulada depois
    print('Nome b não está definido')
    print(error)
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception: # exception é o error absoluto, se não souber a causa pode usa-lo, tudo cai nele
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
