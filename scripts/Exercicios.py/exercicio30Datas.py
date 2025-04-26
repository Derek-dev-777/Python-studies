from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta


data_emprestimo = datetime.strptime('2022-12-20', '%Y-%m-%d')
data_emprestimo2 = ('%Y-%m-%d')
adicional_mes = relativedelta(months=1)
emprestimo = 1000000
parcelas = emprestimo / 60

for i in range(60):
    data_emprestimo += relativedelta(months=1)
    print(f"{data_emprestimo.strftime("%Y-%m-%d")} {parcelas:.3f}")