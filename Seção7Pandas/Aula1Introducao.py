import pandas as pd

# Data frames = tabelas dentro do python ( lembrar disso ) exemplo abaixo:

vendas = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
        }

# A partir dos dados de vendas, iremos criar um dataframe
vendas_df = pd.DataFrame(vendas)
# print(vendas_df) # visualizando nosso dataframe

""" Podemos tambem importar um dataframe ( arquivos ) nesse caso vamos importar
 um arquivo em excel ( Vendas.xlsx ), exemplo abaixo:"""

vendas_df = pd.read_excel(r"C:\Users\kaver\OneDrive\Documentos\GitHub\Python-studies\Seção7Pandas\Vendas.xlsx")
#print(vendas_df)

''' Alguns metodos uteis para visualização nas tabelas
 - Head ( Mostra o tanto de linhas que você colocar no parenteses ) exemplo:'''
# print(vendas_df.head(10)) # mostra as 10 primeiras linhas de uma tabela

""" - Shape ( Mostra quantas linhas e colunas existem na tabela) exemplo:"""
#print(vendas_df.shape)

""" - Describe ( Faz um resumao da tabela com os dados numericos), por exemplo
 ele mostrara o preço medio dos produtos, a media de unidades que um comprador compra
 count, mean, min, 25%, 50%, 75%, max, std ( essas sao as infos )"""

#print(vendas_df.describe()) 

""" Podemos visualizar colunas especificas de uma tabela da seguinte maneira:"""

produtos = vendas_df["Produto"]
#print(produtos)

"""Caso queira visualizar 2 ou mais colunas em especifico, basta fazer assim"""
produtos2 = vendas_df[["Produto","ID Loja"]]
#print(produtos2)

"""Para localizar diversos itens especificos, usamos o .loc, que localiza o mesmo
com base no ID ou index da tabela ( codigo do produto, qualquer coisa unica)
Abaixo localizamos a linha 1 da tabela
"""
#print(vendas_df.loc[1])

"""Abaixo localizamos as linhas do 1 ao 5 da tabela"""

#print(vendas_df.loc[1:5])

"""Usando o mesmo comando, podemos localizar coisas com condições, por exemplo
eu quero localizar tudo relacionado a loja "Norte Shopping" """
# Quero que me mostre tudo onde o ID loja for igual a Norte Shopping

#print(vendas_df.loc[vendas_df["ID Loja"] == "Norte Shopping"])

"""Para buscar varias linhas e colunas em uma tabela, nós temos que ter em mente que
o comando loc ele funciona assim: .loc[linhas, colunas] ou seja
primeiro nós filtramos selecionamos quais as linhas que queremos mostrar, o exemplo
acima foi com as linhas em que o ID loja é igual a norte shopping, e depois
escolhemos quais colunas passaremos, exemplo abaixo:
"""
"""Mostre todas as linhas que o id loja for igual a norte shopping, e me mostre apenas as colunas
ID loja, Produto e Quantidade"""

#print(vendas_df.loc[vendas_df['ID Loja']== "Norte Shopping", ["ID Loja", "Produto","Quantidade"]])

"""Pegando uma valor em especifico, a linha 1, me mostre qual é o produto"""
#print(vendas_df.loc[1, "Produto"])

###############################################################################################################

"""Como criar colunas em uma tabela exemplo:"""

vendas_df["Comissão"] = vendas_df["Valor Final"] * 0.05
""" basicamente esse comando, caso ja exista uma coluna "Comissão", ele iria substitui-la, como não é o caso
ele cria uma coluna com a condição que foi passada (comissão é = a 5% do valor final)
ou seja, os ITENS dentro da coluna condição, vao ser iguais a 5% do valor final."""

#print(vendas_df)

"""é possivel criar uma coluna com um valor padrao tambem"""
vendas_df["Imposto"] = 0

"""O comando acima pode funcionar, mas em tabelas ENORMES, pode ser que gere erros, então o melhor jeito seria"""
vendas_df.loc[:,"Imposto"] = 0  # Todas as linhas dentro da coluna imposto vao ser igual a 0
# Lembre-se  .loc[Linhas, colunas]

"""Podemos mesclar dados de uma tabela por exemplo, nossa tabela vendas_df vai até novembro, e nós
queremos adicionar as vendas de dezembro tambem nessa tabela, como fazer?"""
# Primeiro atribuimos a mesma a uma variavel usando o pd.read
vendas_dezembro_df = pd.read_excel(r"C:\Users\kaver\OneDrive\Documentos\GitHub\Python-studies\Seção7Pandas\Vendas - Dez.xlsx")

# em vendas_df, concatenamos vendas_dezembro, ignore index é para reorganizar os indexs(ids)
# OBS tomar cuidado pois se o codigo for executado mais de uma vez, ele ira adicionar MAIS de uma vez
# os valores da tabela na vendas_df, ent o ideal é utilizar e apagar
#vendas_df = pd.concat([vendas_df, vendas_dezembro_df], ignore_index=True)

"""Como Excluir linhas e colunas no pandas"""
# Axis=1 é para colunas, axis=0 é para linhas, você passa a coluna ou a linha pelo index
vendas_df = vendas_df.drop(0, axis=0) # exclui a linha 0
vendas_df = vendas_df.drop("Imposto", axis=1) # exclui a coluna Imposto

"""Manipulando valores vazios nas tabelas"""
"""Primeiro vamos aprender a deletar linhas e colunas vazias """

vendas_df = vendas_df.dropna(how="all")# ele ira excluir todas as linhas e colunas completamente vazias
vendas_df = vendas_df.dropna(how="all",axis=1)# ele ira excluir todas as colunas que estao vazias

"""Agora vamos deletar linhas que tem ao menos 1 valor vazio"""
vendas_df = vendas_df.dropna() # ira deletar linhas que tem ao menos 1 valor vazio

"""Agora vamos preencher valores vazios"""
vendas_df["Comissão"] = vendas_df["Comissão"].fillna() # dentro do (), você passa o valor que preencherá as linhas

"""Preenchendo os valores da comissão com a media das outras comissoes"""

vendas_df["Comissão"] = vendas_df["Comissão"].fillna