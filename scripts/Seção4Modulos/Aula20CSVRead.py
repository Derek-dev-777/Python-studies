import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / 'Teste1.csv'

with caminho_csv.open("r") as arquivo:
    leitor = csv.DictReader(arquivo) # um comando que lê os arquivos em forma de lista
    
    for linha in leitor:
        print(linha)
        print(linha["Nome"])
    