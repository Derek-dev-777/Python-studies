# # PyPDF2 para manipular arquivos PDF (Instalação)
 # PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
 # gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
 # dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
 # extrair texto e imagens, manipular metadados, e mais.
 # A documentação contém todas as informações necessárias para usar PyPDF2.
 # Link: https://pypdf2.readthedocs.io/en/3.0.0/
 # Ative seu ambiente virtual
 # pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
MEU_PDF = PASTA_RAIZ / "PdfBanco.pdf"
NOVOS_ARQUIVOS = PASTA_RAIZ / "Novos Arquivos"

NOVOS_ARQUIVOS.mkdir(exist_ok=True)

reader = PdfReader(MEU_PDF) # essa classe recebe um arquivo como parametro, os comandos estao na documentação

print(len(reader.pages))
page0 = reader.pages[0]

print(page0.extract_text())

imagem0 = page0.images[0]

#with open(NOVOS_ARQUIVOS / imagem0.name, 'wb') as fp:
    #fp.write(imagem0.data)

writer = PdfWriter()
writer.add_page(page0)

with open(NOVOS_ARQUIVOS / "page0.pdf", "wb") as fp:
    writer.write(fp)


for i, page in enumerate(reader.pages):
     writer = PdfWriter()
     with open(NOVOS_ARQUIVOS / f'page{i}.pdf', 'wb') as arquivo:
         writer.add_page(page)
         writer.write(arquivo) 