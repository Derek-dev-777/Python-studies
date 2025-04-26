# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime,timedelta

fmt = "%d/%m/%Y %H:%M:%S"
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = data_fim - data_inicio # podemos fazer operações matematicas com datas, nos retornando em dias e horas]

print(delta.days, delta.seconds, delta.microseconds) # posso escolher o que eu quero q ele me retorne ( dias etc...)
print(delta.total_seconds()) # retorna o total de segundos da minha operação

delta2 = timedelta(days=10) # posso fazer uma soma de datas, passando dias,segundos,horas, semanas etc
print(data_fim + delta2) #irá adicionar 10 dias a mais na minha data, pode ser feito (menos tambem)
# em resumo "timedelta" serve para fazer diferença entre datas, seja somando ou subtraindo entre outros