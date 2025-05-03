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

# Podemos tambem importar um dataframe ( arquivos ) nesse caso vamos importar
# um arquivo em excel ( Vendas.xlsx )

vendas_df = pd.read_excel("Vendas.xlsx")
print(vendas_df)