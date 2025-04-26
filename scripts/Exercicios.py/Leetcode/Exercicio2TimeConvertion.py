import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    periodo = s[-2:]         # Pega os dois últimos caracteres (AM ou PM)
    hora = int(s[:2])        # Pega os dois primeiros caracteres como inteiro (hora)
    resto = s[2:-2]          # Pega o restante (minutos e segundos)

    if periodo == "AM":
        if hora == 12:
            hora = 0         # 12AM vira 00 no formato 24h
    else:  # PM
        if hora != 12:
            hora += 12       # Soma 12 se for PM (exceto se já for 12)

    return f"{hora:02d}{resto}"  # Retorna hora formatada com dois dígitos + o resto

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
