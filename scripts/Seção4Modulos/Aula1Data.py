# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone
#data_str_data = '2022/04/20 07:49:23'
#data_str_data = '20/04/2022'
#data_str_fmt = '%d/%m/%Y'

hora_atual = datetime.now(timezone("America/Sao_Paulo"))
# o comando date.timenow mostra a hora atual do seu computador, e se você quiser colocar uma timezone diferente
# basta colocar timezone(nome da timezone), você pode checar o nome da timezone no link la em cima

# data = datetime(2022, 4, 20, 7, 49, 23)
#data = datetime.strptime(data_str_data, data_str_fmt)
#print(data)

print(hora_atual.timestamp()) # o comando timestamp mostra os segundos contados desde 1981 até hoje...