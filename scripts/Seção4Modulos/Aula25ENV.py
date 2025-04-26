#Você pode criar uma variavel no proprio terminal ( variavel de ambiente )
# usando no seu terminal
# $env:senha = "Batata123"  ( exemplo de uma criação de senha pelo terminal )
# $env:senha ( se executado o comando, ele ira te mostrar a variavel "batata123")

# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example

# QUALQUER COISA REVISAR A AULA 301 DO CURSO
import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# print(os.environ)
print(os.getenv('BD_PASSWORD'))

senha = os.getenv("senha") # busca a variavel senha no env, e me retorna o valor dela

print(senha)