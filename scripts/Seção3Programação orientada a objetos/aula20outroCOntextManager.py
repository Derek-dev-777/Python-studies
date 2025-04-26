#Context manager de um jeito mais simples, tratando e fazendo a mesma função do anterior
# Context mamnager é um meio CERTO, de abrir e fechar arquivos, é uma função para que não ocorra erros

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding="utf8")
        yield arquivo
    except Exception as e:
        print("Ocorreu um error", e)
    finally:
        print("Fechando arquivo")
        arquivo.close

with my_open("aula20outroCOntextManager.txt", "w") as arquivo:
    arquivo.write("oi")
    arquivo.write("oi")
    arquivo.write("oi")